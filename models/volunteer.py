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


class ConfirmedVolunteer(EndpointsModel):
    _message_fields_schema = ("id", "applied_on", "confirmed_on", "confirmed_by", "name", "email", "sex", "city",
                              "country", "phone_no")

    applied_on = ndb.DateTimeProperty()
    confirmed_on = ndb.DateTimeProperty(auto_now_add=True)
    confirmed_by = ndb.StringProperty()
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    sex = ndb.StringProperty()
    city = ndb.StringProperty()
    country = ndb.StringProperty()
    phone_no = ndb.StringProperty()
