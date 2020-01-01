from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin


db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    role = db.Column(db.String(255))