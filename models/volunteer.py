from google.appengine.ext import ndb

from endpoints_proto_datastore.ndb.model import EndpointsModel


class UnconfirmedVolunteer(EndpointsModel):

    _message_fields_schema = ("id", "applied_on", "name", "email", "sex", "city", "country", "phone_no")

    applied_on = ndb.DateTimeProperty(auto_now_add=True)
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    sex = ndb.StringProperty()
    city = ndb.StringProperty()
    country = ndb.StringProperty()
    phone_no = ndb.StringProperty()
