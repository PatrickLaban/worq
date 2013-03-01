import webapp2
import controllers.wq_user

app = webapp2.WSGIApplication([
    ('/', controllers.wq_user.HomePageHandler),
    ('/account', controllers.wq_user.AccountHandler),
], debug=True)