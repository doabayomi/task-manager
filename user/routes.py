"""Authentication routes"""
from . import auth_blueprint
from models import db
from models.user import User

from flask import (
    current_app as app,
    request, jsonify, redirect, url_for
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
@auth_blueprint.route('/register', methods=['POST'])
def register():
    """Signs up a user"""
    with app.app_context():
        user_datastore: Datastore = app.extensions['security'].datastore
        email = request.form.get('email')
        password = request.form.get('password')

        # TODO: validation for email and password.
        user = user_datastore.create_user(email=email,
                                          password=hash_password(password))
        user_datastore.commit()
        return jsonify({
            'message': 'User created',
            'email': user.email})


@auth_blueprint.route('/login', methods=['POST'])
def login():
    """Logs a user in"""
    with app.app_context():
        user_datastore: Datastore = app.extensions['security'].datastore

        # TODO: update email and password collection logic for validation
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
            return jsonify({'message': 'Login successful'})
        else:
            return jsonify({'message': 'Login failed'}), 500


@auth_blueprint.route('/logout', methods=['POST'])
@auth_required()
def logout():
    """Logs out a user"""
    logout_user()
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
        # TODO: Email validation
        if request.form.get('email') is not None:
            new_email = request.form.get('email')

        with app.app_context():
            user = User.query.filter_by(email=user_in_session.email).first()
            if user:
                user.email = new_email
                db.session.commit()

        return jsonify({'message': 'Profile successfully created'})
