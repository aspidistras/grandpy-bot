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
def init_sql_db():
    """sets cli command to init database"""
    init_db()
