"""Main flask app"""
from flask import Flask, jsonify
from auth import auth_blueprint
from pages import pages_blueprint
from config import Config
from models import db


def create_app(config_object=Config):
    """Create app function to conform to factory pattern

    Args:
        config_object: Config class from config.py. Defaults to Config.

    Returns:
        App instance
    """
    app = Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)
    app.register_blueprint(pages_blueprint)
    app.register_blueprint(auth_blueprint)
    return app


if __name__ == '__main__':
    app = create_app(Config)
    app.run(debug=True)
