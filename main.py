import webapp2
import controllers.wq_user

app = webapp2.WSGIApplication([
    ('/', controllers.wq_user.HomePageHandler),
    ('/home', controllers.wq_user.HomePageHandler),
], debug=True)
