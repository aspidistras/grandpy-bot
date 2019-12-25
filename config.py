import os
import psycopg2


# Database initialization
if os.environ.get('DATABASE_URL') is None:
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    conn = psycopg2.connect(os.environ['DATABASE_URL'], sslmode='require')

SQLALCHEMY_TRACK_MODIFICATIONS = False

