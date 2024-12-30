"""Pages module"""
from flask import Blueprint
# from . import routes

pages_blueprint = Blueprint('pages', __name__)

from . import routes  # noqa: E402
