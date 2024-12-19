"""Authentication routes"""
from . import auth_blueprint
from flask import current_app as app, request, jsonify
from flask_security import SQLAlchemyUserDatastore as Datastore
from flask_security import login_user, auth_required, UserMixin
from flask_security.utils import hash_password


@auth_blueprint.route('/register', methods=['POST'])
def register():
    with app.app_context():
        user_datastore: Datastore = app.extensions['security'].datastore
        email = request.form.get('email')
        password = request.form.get('password')

        # TODO: validation for email and password.
        user = user_datastore.create_user(email=email,
                                          password=hash_password(password))
        user_datastore.commit()
        return jsonify({'message': 'User created'})


@auth_blueprint.route('/login', methods=['POST'])
def login():
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


@auth_blueprint.route('/logout')
def logout():
    pass


@auth_blueprint.route('/me')
@auth_required()
def profile():
    pass
