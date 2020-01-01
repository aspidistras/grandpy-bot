"""imports the app"""

import os
from flask import Flask
from flask_migrate import Migrate

from botapp.views import app
from botapp.app import db, init_db
from botapp.models import logging, user


# Connect sqlalchemy to app
db.init_app(app)

@app.cli.command()
def init_db():
    init_db()

