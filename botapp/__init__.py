"""imports the app"""


import os
from flask import Flask
from flask_migrate import Migrate

from botapp.views import app
from . import models

# Connect sqlalchemy to app
models.db.init_app(app)
