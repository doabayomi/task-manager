from .import db
from typing import Optional


class User(db.Model):
    __tablename__ = 'users'

    # TODO: Probably make id a different data type like a string
    id: int = db.Column(db.String(255), primary_key=True)
    email: str = db.Column(db.String(255), unique=True, nullable=False)
    password: Optional[str] = db.Column(db.string(50),
                                        unique=True, nullable=False)
