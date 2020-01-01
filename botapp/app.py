import os
from flask import Flask
from flask_migrate import Migrate

from botapp.models.logging import Logging, LoggingView, db


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

def init_db():
    db.drop_all()
    db.create_all()