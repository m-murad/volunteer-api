from google.appengine.ext import ndb

from endpoints_proto_datastore.ndb.model import EndpointsModel


class Task(EndpointsModel):

    _message_fields_schema = ('id', 'createdOn', 'author', 'title', 'description', 'dueDate', 'assigned', 'assignedTo',
                              'notes')

    createdOn = ndb.DateTimeProperty(auto_now_add=True)
    author = ndb.StringProperty()
    title = ndb.StringProperty()
    description = ndb.StringProperty()
    dueDate = ndb.StringProperty()
    assigned = ndb.BooleanProperty()
    assignedTo = ndb.StringProperty()
    notes = ndb.StringProperty()
    # TODO: Add 'required=True'
