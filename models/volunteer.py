from google.appengine.ext import ndb

from endpoints_proto_datastore.ndb.model import EndpointsModel


class Volunteer(EndpointsModel):
    _message_fields_schema = ("id", "applied_on", "confirmed", "confirmed_by", "name", "email", "sex", "city",
                              "country", "phone_no")

    applied_on = ndb.DateTimeProperty(auto_now_add=True)
    confirmed = ndb.BooleanProperty(default=False)
    confirmed_by = ndb.UserProperty()
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    sex = ndb.StringProperty()
    city = ndb.StringProperty()
    country = ndb.StringProperty()
    phone_no = ndb.StringProperty()

