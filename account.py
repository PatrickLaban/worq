import webapp2
import controllers.wq_user

app = webapp2.WSGIApplication([
    ('/account/?', controllers.wq_user.AccountHandler),
], debug=True)