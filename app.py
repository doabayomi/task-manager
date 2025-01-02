"""Main flask app"""
from flask import Flask
from flask_security import Security, SQLAlchemyUserDatastore
from flask_security.models import fsqla_v3 as fsqla
from flask_restful import Api

from config import Config

from models import db
from resources import TaskResource


def create_app(config_object=Config):
    """Create app function to conform to factory pattern

    Args:
        config_object: Config class from config.py. Defaults to Config.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)

    # ? This two lines specifically set_db_info() has been forcing
    # ? the lines to be in a particular way on this create_app().
    # ? Could I fix it to avoid that NoneType error.
    db.init_app(app)
    fsqla.FsModels.set_db_info(db)

    # ! It is important that the models for authentication are
    # ! imported after set_db_info() or it'll break the code.
    # ! In fact, this applies to most things here.
    from models.user import User
    from models.role import Role
    # ? Role model could be possibly used for collaboration
    user_datastore = SQLAlchemyUserDatastore(db, User, None)
    security = Security(app, user_datastore)

    api = Api(app)
    api.add_resource(TaskResource, '/tasks', '/tasks/<int:task_id>')

    from user import auth_blueprint
    from pages import pages_blueprint
    app.register_blueprint(pages_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    with app.app_context():
        db.drop_all()  # ! For testing, should be deleted when deploying
        db.create_all()

    return app


if __name__ == '__main__':
    app = create_app(Config)
    app.run(debug=True)
