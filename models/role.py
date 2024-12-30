# from flask_security import RoleMixin
from . import db
from flask_security.models import fsqla_v3 as fsqla


class Role(db.Model, fsqla.FsRoleMixin):
    pass
