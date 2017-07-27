import endpoints

from apis import TasksApi
from apis import VolunteersApi


# List of APIs goes here.
app = endpoints.api_server([TasksApi, VolunteersApi])
