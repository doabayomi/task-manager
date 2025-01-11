"""Application resources module"""
from flask_restful import Api

api = Api()

# Keep other modules import below this line to prevent circular imports
from .task import TaskResource  # noqa: E402
__all__ = ['api', 'TaskResource']
