"""Authentication routes"""
from . import auth_blueprint
from models import db
from models.user import User

from marshmallow import ValidationError
from schemas import UserSchema

from flask import (
    current_app as app,
    request, jsonify, redirect, url_for, render_template
)
from flask_security import SQLAlchemyUserDatastore as Datastore
from flask_security import (
    login_user, auth_required,
    current_user, UserMixin, logout_user
)
from flask_security.utils import hash_password


# * The authentication routes are implemented in an API like system
# * however as the case may be, it could be implemented in a page system
# * with redirects implemented on server-side.
@auth_blueprint.route('/register', methods=['POST', 'GET'])
def register():
    """Signs up a user"""
    if request.method == 'GET':
        return render_template('register.html')
    with app.app_context():
        user_datastore: Datastore = app.extensions['security'].datastore
        if request.is_json:
            user_data = request.get_json()
        else:
            user_data = request.form.to_dict()

        try:
            schema = UserSchema()
            valid_user_data = schema.load(user_data)
            email = valid_user_data['email']
            password = valid_user_data['password']
        except ValidationError as err:
            return jsonify({'message': 'Invalid input'}), 400

        user = user_datastore.find_user(email=email)
        if user is not None:
            return jsonify({'message': 'User already exists'}), 409

        user = user_datastore.create_user(email=email,
                                          password=hash_password(password))
        user_datastore.commit()
        return jsonify({
            'message': 'User created',
            'email': user.email})


@auth_blueprint.route('/login', methods=['POST', 'GET'])
def login():
    """Logs a user in"""
    if current_user.is_authenticated:
        return redirect(url_for('pages.dashboard'))

    if request.method == 'GET':
        return render_template('login.html')

    with app.app_context():
        user_datastore: Datastore = app.extensions['security'].datastore

        # TODO: update email and password collection logic for validation
        if request.is_json:
            data = request.get_json()
            email = data.get('email')
            password = data.get('password')
        else:
            email = request.form.get('email')
            password = request.form.get('password')

        user = user_datastore.find_user(email=email)
        if user is None:
            return jsonify({'message': 'User does not exist'}), 404

        password_is_valid = user.verify_and_update_password(password)
        if not password_is_valid:
            return jsonify({'message': 'Invalid password'}), 401

        if login_user(user):
            user_datastore.commit()
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'message': 'Login failed'}), 500


@auth_blueprint.route('/logout', methods=['POST', 'GET'])
@auth_required()
def logout():
    """Logs out a user"""
    logout_user()
    if request.method == 'GET':
        return redirect(url_for('auth.login'))
    return jsonify({'message': 'Logout successful'})


@auth_blueprint.route('/profile', methods=['GET', 'POST'])
@auth_required()
def profile():
    """Checks user profile"""
    user_in_session: UserMixin = current_user

    if request.method == 'GET':
        return jsonify({'email': user_in_session.email})
    elif request.method == 'POST':
        # ? Turns out there is no direct flask-security method for
        # ? updating user profiles.
        try:
            schema = UserSchema()
            user_data = schema.load(request.form.to_dict(), partial=True)
        except ValidationError as err:
            return jsonify(err.messages), 400

        if 'new_password' in user_data:
            hashed_new_password = hash_password(user_data['new_password'])
            user_data['password'] = hashed_new_password
            user_data.pop('new_password')

        with app.app_context():
            user = User.query.filter_by(email=user_in_session.email).first()
            if not user:
                return jsonify({'message': 'User not found'}), 404

            for field, value in user_data.items():
                setattr(user, field, value)
            db.session.commit()

        return jsonify({'message': 'Profile successfully updated'})
