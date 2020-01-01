import os
from flask import Flask
from flask_migrate import Migrate
from flask_admin.contrib import sqla
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user


db = SQLAlchemy()


class Logging(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    request = db.Column(db.String(200), nullable=False)
    null_api = db.Column(db.String(200), nullable=False)

    def __init__(self, request, null_api):
        self.request = request
        self.null_api = null_api


class LoggingView(sqla.ModelView):
    can_delete = False  # disable model deletion
    can_create = False
    can_edit = False
    column_searchable_list = ['request']
    column_filters = ['null_api']

    def is_accessible(self):
        return current_user.role == 'admin'
