import webapp2
from google.appengine.api import users
from models.WqUser import WqUser
import jinja2
import os

base_paths = os.path.split(os.path.dirname(__file__))
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(base_paths[0]))

class HomePageHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
            user_name = user.email()
            WqUser.get_or_insert(user_name.lower(), parent=None, user=user, name=user_name)
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
            user_name = ""

        template_values = {
            'url': url,
            'url_linktext': url_linktext,
            'user_name': user_name,
        }

        template = jinja_environment.get_template('templates/index.html')
        self.response.out.write(template.render(template_values))