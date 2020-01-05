import os
from flask import Flask, redirect, url_for, request
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
        if current_user.is_authenticated and current_user.role == "admin":
            return True
        else:
            return False

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('admin.index', next=request.url))
