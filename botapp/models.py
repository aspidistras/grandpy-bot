from flask_sqlalchemy import SQLAlchemy
import logging as lg
from flask import Flask
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config')

# Create database connection object
db = SQLAlchemy(app)
migrate = Migrate(app, db) # this

class Logging(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    request = db.Column(db.String(200), nullable=False)
    null_api = db.Column(db.String(200), nullable=False)

    def __init__(self, request, null_api):
        self.request = request
        self.null_api = null_api

    

def init_db():
    db.drop_all()
    db.create_all()
