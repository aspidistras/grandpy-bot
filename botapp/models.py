from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate
import os


db = SQLAlchemy()

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


def create_production_app():
    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)
    app.app_context().push()
    Migrate(app, db)
    return app


def create_test_app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'app.test_db')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    app.app_context().push()
    Migrate(app, db)
    return app
