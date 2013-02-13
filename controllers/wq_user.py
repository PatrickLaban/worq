import webapp2
from google.appengine.api import users
import jinja2
import os

base_paths = os.path.split(os.path.dirname(__file__))
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(base_paths[0]))

class HomePageHandler(webapp2.RequestHandler):
    def get(self):
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {'url': url, 'url_linktext': url_linktext}

        template = jinja_environment.get_template('templates/index.html')
        self.response.out.write(template.render(template_values))