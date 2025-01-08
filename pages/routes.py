from flask import send_from_directory
from . import pages_blueprint


@pages_blueprint.route('/')
def root():
    return send_from_directory("static", "index.html"), 200
