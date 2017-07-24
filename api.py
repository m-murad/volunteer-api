import endpoints

from apis import TasksApi


# List of APIs goes here.
app = endpoints.api_server([TasksApi])
