"""defines the customized AdminIndexView with its methods for index access, login and logout"""


from flask import url_for, redirect, request
import flask_admin as admin
import flask_login as login
from flask_admin import helpers, expose

from botapp.models.user import LoginForm


class AdminIndexView(admin.AdminIndexView):
    """initializes customized index view to handle login and logout"""

    @expose('/')
    def index(self):
        """return admin index page"""

        if not login.current_user.is_authenticated:
            # redirects to login view if user isn't authenticated
            return redirect(url_for('.login_view'))
        return super(AdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        """handles user login"""

        # create LoginForm object
        form = LoginForm(request.form)

        if helpers.validate_form_on_submit(form):
            # get user and log him in
            user = form.get_user()
            login.login_user(user)

        if login.current_user.is_authenticated:
            return redirect(url_for('.index'))
        self._template_args['form'] = form
        return super(AdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        """handles user logout and redirects to admin index page"""
        login.logout_user()
        return redirect(url_for('.index'))
