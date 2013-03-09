from google.appengine.ext import ndb
import webapp2
from google.appengine.api import users
from models.WqUser import WqUser
import jinja2
import os

base_paths = os.path.split(os.path.dirname(__file__))
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(base_paths[0]))

class BaseRequestHandler(webapp2.RequestHandler):

    def __init__(self, request, response):
        self.user = users.get_current_user()
        self.template_values = {}
        if self.user:
            url = users.create_logout_url('/')
            url_linktext = 'Log Out'
            user_name = self.user.email()
            WqUser.get_or_insert(user_name.lower(), parent=None, user=self.user, name=user_name)
        else:
            url = users.create_login_url('/account')
            url_linktext = 'Login With Your Existing Gmail Account'
            user_name = ""

        self.template_values['url'] = url
        self.template_values['url_linktext'] = url_linktext
        self.template_values['user_name'] = user_name

        super(BaseRequestHandler, self).__init__(request, response)


class IndexPageHandler(BaseRequestHandler):

    @ndb.toplevel
    def get(self):
        if self.user:
            # if we're already logged in, redirect them to the account page
            self.redirect('/account/')
            return
        else:
            template = jinja_environment.get_template('templates/home.html')
            self.response.out.write(template.render(self.template_values))

class HomePageHandler(BaseRequestHandler):

    @ndb.toplevel
    def get(self):
        template = jinja_environment.get_template('templates/home.html')
        self.response.out.write(template.render(self.template_values))


class AccountHandler(BaseRequestHandler):

    @ndb.toplevel
    def get(self):
        template = jinja_environment.get_template('templates/account/account.html')
        self.response.out.write(template.render(self.template_values))