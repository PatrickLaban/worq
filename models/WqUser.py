from google.appengine.ext import ndb

class WqUser(ndb.Model):
    """stfu"""
    user = ndb.model.UserProperty()
    name = ndb.model.StringProperty()

        