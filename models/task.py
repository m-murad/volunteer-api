from google.appengine.ext import ndb

from endpoints_proto_datastore.ndb.model import EndpointsModel


class Task(EndpointsModel):

    _message_fields_schema = ('id', 'createdOn', 'author', 'lastUpdatedBy', 'title', 'description', 'dueDate',
                              'assigned', 'assignedTo', 'notes', 'completed')

    createdOn = ndb.DateTimeProperty(auto_now_add=True)
    author = ndb.UserProperty(auto_current_user_add=True)
    lastUpdatedBy = ndb.UserProperty(auto_current_user=True)
    title = ndb.StringProperty()
    description = ndb.StringProperty()
    dueDate = ndb.StringProperty()
    assigned = ndb.BooleanProperty()
    assignedTo = ndb.UserProperty()
    notes = ndb.StringProperty()
    completed = ndb.BooleanProperty(default=False)
    # TODO: Add 'required=True'
