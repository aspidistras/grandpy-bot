"""tests logging is made when requests to one or both API fail"""


import unittest

from botapp.grandpy_bot import GrandPyBot
from botapp.app import create_test_app
from botapp.views import db
from botapp.models.logging import Logging


class TestLogging(unittest.TestCase):
    """initializes test class for the logging with its attributes and methods"""

    def setUp(self):
        """
        Set up app and grab connection to test database
        """

        self.app = create_test_app()
        self.db = db
        self.db.create_all()
        self.bot = GrandPyBot("a")
        self.database_count = 0

    def database_connection(self):
        """
        Tests database access
        """

        try:
            self.database_count = Logging.query.count()
            return True
        except:
            return False

    def test_database_entry(self):
        """
        Tests if Logging instances are created when requests fail
        """

        if self.database_connection():
            self.bot.return_data()
            new_count = Logging.query.count()
            assert self.database_count + 2 == new_count

    def tearDown(self):
        """
        Ensure that the database is emptied for next unit test
        """

        self.db.session.remove()
        self.db.drop_all()


if __name__ == '__main__':
    unittest.main()
