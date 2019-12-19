from flask_sqlalchemy import SQLAlchemy
import logging as lg
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

# Create database connection object
db = SQLAlchemy(app)

class Logging(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    request = db.Column(db.String(200), nullable=False)
    null_api = db.Column(db.String(200), nullable=False)

    def __init__(self, request, null_api):
        self.request = request
        self.null_api = null_api

    

db.create_all()