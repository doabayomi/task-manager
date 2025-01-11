"""Pages module"""
from flask import Blueprint
# from . import routes

pages_blueprint = Blueprint('pages', __name__)

# Keep other imports below this line to prevent circular imports
from . import routes  # noqa: E402
