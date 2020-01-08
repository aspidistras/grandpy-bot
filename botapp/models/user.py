"""defines User model and Login Form"""


from wtforms import form, fields, validators
from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin


db = SQLAlchemy()


class User(db.Model, UserMixin):
    """initializes User object with its attributes to permit account creation and login"""

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    role = db.Column(db.String(255))

    def __init__(self, email, password, active, role):
        self.email = email
        self.password = password
        self.active = active
        self.role = role


class LoginForm(form.Form):
    """initializes LoginForm object with its attributes and methods
    to permit login and raise errors if login data doesn't match db data"""

    email = fields.StringField(validators=[validators.required()])
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self):
        """get user or return errors if user doesn't exist or pasword is wrong"""

        user = self.get_user()

        if user is None:
            raise validators.ValidationError('Invalid user')

        if user.password != self.password.data:
            raise validators.ValidationError('Invalid password')

    def get_user(self):
        """query user from database matching entered infos"""

        return db.session.query(User).filter_by(email=self.email.data).first()
