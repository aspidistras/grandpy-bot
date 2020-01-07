"""tests user can log in and out and has access to admin pages only if role is admin"""


import urllib
import unittest
import re
import os
import requests
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import flask_login
from flask_login import current_user
from flask_admin import Admin

from botapp.grandpy_bot import GrandPyBot
from botapp.app import create_test_app
from botapp.models.user import User, db
from botapp.models.admin import AdminIndexView



class TestUser(unittest.TestCase):
    """initializes test class for user related functionnalities with its attributes and methods"""

    def setUp(self):
        """
        Set up app and grab connection to test database
        """

        self.app = create_test_app()
        self.app.config['SECRET_KEY'] = '12345678'
        self.client = self.app.test_client()
        self._ctx = self.app.test_request_context()
        self._ctx.push()
        self.db = db
        self.db.create_all()
        self.user = User("test@test.fr", "test", True, "admin")
        self.db.session.add(self.user)
        self.db.session.commit()


    def database_connection(self):
        try:
            User.query.count()
            return True
        except:
            return False


    def test_user_login(self):
        if self.database_connection():
            with self.client:
                flask_login.login_user(self.user)
                assert current_user.email == "test@test.fr"
    

    def test_user_logout(self):
        if self.database_connection():
            with self.client:
                flask_login.login_user(self.user)
                flask_login.logout_user()
                assert current_user.is_anonymous == True
                    

    def tearDown(self):
        """
        Ensure that the database is emptied for next unit test
        """

        self.db.session.remove()
        self.db.drop_all()


if __name__ == '__main__':
    unittest.main()
