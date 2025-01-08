# from flask_security import UserMixin
from . import db
from flask_security.models import fsqla_v3 as fsqla


class User(db.Model, fsqla.FsUserMixin):
    tasks = db.relationship('Task', back_populates='user')
