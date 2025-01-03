"""Authentication module"""
from flask import Blueprint

auth_blueprint = Blueprint('auth', __name__)

# Keep other imports below this line to prevent circular imports
from . import routes  # noqa: E402
