from flask import jsonify
from .import pages_blueprint


@pages_blueprint.route('/')
def welcome():
    return jsonify({
        'message': 'Hello world'
    }), 200
