from . import db
from datetime import datetime


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    # status = db.Column(db.String(100), nullable=False, default='todo')

    deadline = db.Column(db.DateTime(timezone=True), nullable=True)
    date_added = db.Column(db.DateTime(timezone=True),
                           default=datetime.utcnow(), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # ?: do I need a relationship back to the user
    user = db.relationship('User', back_populates='tasks')
