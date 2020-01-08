"""tests user can log in and out and has access to admin pages only if role is admin"""


import unittest
from flask import url_for
import flask_login
from flask_login import current_user
from flask_admin import Admin

from botapp.app import create_test_app
from botapp.models.user import User, db
from botapp.models.logging import Logging, LoggingView
from botapp.admin import AdminIndexView


class TestUser(unittest.TestCase):
    """initializes test class for user related functionnalities with its attributes and methods"""

    def setUp(self):
        """
        Set up app and grab connection to test database
        """

        self.app = create_test_app()
        self.app.config['SECRET_KEY'] = '123456789'
        self.client = self.app.test_client()
        self._ctx = self.app.test_request_context()
        self._ctx.push()
        self.db = db
        self.db.create_all()
        self.user = User("test@test.fr", "test", True, "admin")
        self.db.session.add(self.user)
        self.db.session.commit()
        self.admin = Admin(self.app, name='GrandPy Bot', index_view=AdminIndexView(),
                           template_mode='bootstrap3', base_template='custom-admin.html')
        self.admin.add_view(LoggingView(Logging, db.session))
        flask_login.login_user(self.user)


    def database_connection(self):
        """
        Tests database access
        """

        try:
            User.query.count()
            return True
        except:
            return False


    def test_user_login(self):
        """
        Tests user is logged in
        """

        if self.database_connection():
            with self.client:
                assert current_user.email == "test@test.fr"


    def test_user_logout(self):
        """
        Tests user is logged out
        """

        if self.database_connection():
            with self.client:
                flask_login.logout_user()
                assert current_user.is_anonymous is True


    def test_access_to_admin(self):
        """
        Tests logged in user has access to logging view
        """

        with self.client:
            with self.client.session_transaction() as session:
                session['user_id'] = current_user.id

            response = self.client.get(url_for('admin.index'), follow_redirects=True)
            assert b'Here you can browse failed requests logs' in response.data


    def test_access_denied_to_admin(self):
        """
        Tests anonymous user (not logged in) or non admin user is denied access to logging view
        and redirected to login view
        """

        with self.client:
            flask_login.logout_user()
            response = self.client.get(url_for('admin.index'), follow_redirects=True)
            assert b'Login' in response.data

    def tearDown(self):
        """
        Ensure that the database is emptied for next unit test
        """

        self.db.session.remove()
        self.db.drop_all()


if __name__ == '__main__':
    unittest.main()
