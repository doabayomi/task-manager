"""Main flask app
"""
from flask import Flask, jsonify
# from typing import Dict

app = Flask(__name__)
# app.register_blueprint()


@app.route('/')
def index():
    """Gets index page

    Returns:
        Hello world message
    """
    message: dict[str, str] = {
        'message': 'Hello world'
    }
    return jsonify(message), 200
