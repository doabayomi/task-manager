from . import db
from datetime import datetime


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    deadline = db.Column(db.DateTime, nullable=True)
    date_added = db.Column(db.DateTime(timezone=True),
                           default=datetime.utcnow(), nullable=False)
