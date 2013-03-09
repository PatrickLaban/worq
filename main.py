import webapp2
import controllers.wq_user

app = webapp2.WSGIApplication([
    ('/', controllers.wq_user.IndexPageHandler),
    ('/home', controllers.wq_user.HomePageHandler),
], debug=True)
