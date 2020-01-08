"""Logging model and view defined"""


from flask import redirect, url_for, request
from flask_admin.contrib import sqla
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user


db = SQLAlchemy()


class Logging(db.Model):
    """defines the Logging model with its attributes to log app requests"""

    id = db.Column(db.Integer, primary_key=True)
    request = db.Column(db.String(200), nullable=False)
    null_api = db.Column(db.String(200), nullable=False)

    def __init__(self, api_request, null_api):
        self.request = api_request
        self.null_api = null_api


class LoggingView(sqla.ModelView):
    """defines the logging ModelView with its attributes and methods"""

    can_delete = False  # disable model deletion
    can_create = False
    can_edit = False
    column_searchable_list = ['request']
    column_filters = ['null_api']

    def is_accessible(self):
        """returns if user should have access or not to Logging View
        according to his role and if he is authenticated"""

        if current_user.is_authenticated and current_user.role == "admin":
            return True

        return False

    def inaccessible_callback(self, name, **kwargs):
        """defines what should be done if user doesn't have access to Logging View"""

        # redirect to login page if user doesn't have access
        return redirect(url_for('admin.index', next=request.url))
