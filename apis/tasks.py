import endpoints
from protorpc import remote

from models import Task


@endpoints.api(name="tasks", version="v1", description="Tasks API")
class TasksApi(remote.Service):
    @Task.method(user_required=True, path="task/create", name="create")
    def addTask(self, task):
        """Method to create/update a task."""
        task.author = endpoints.get_current_user()
        task.put()
        return task

    @Task.query_method(path="task/list", name="list",
                       query_fields=("limit", "order", "pageToken"))
    def listTasks(self, query):
        """Method to get tasks."""
        return query

    @Task.method(request_fields=("id",), path="task/delete/{id}",
                 http_method="DELETE", name="delete")
    def deleteTask(self, selectedTask):
        """Method to delete a task using its id."""
        if not selectedTask.from_datastore:
            raise endpoints.NotFoundException("Task not found")
        selectedTask.key.delete()
        return Task(title="Task deleted.")
