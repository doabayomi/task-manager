"""Authentication routes"""
from . import auth_blueprint


@auth_blueprint.route('/signup')
def signup():
    pass


@auth_blueprint.route('/login')
def login():
    pass


@auth_blueprint.route('/logout')
def logout():
    pass


@auth_blueprint.route('/me')
def profile():
    pass
