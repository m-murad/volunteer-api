import endpoints
from protorpc import remote

from models import Task


@endpoints.api(name="tasks", version="v1", description="Tasks API")
class TasksApi(remote.Service):
    @Task.method(user_required=True, path="task/create", name="create")
    def addTask(self, task):
        """Method to create/update a task."""
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

    @Task.query_method(user_required=True, path="task/list/complete", name="list_complete",
                       query_fields=("limit", "pageToken"))
    def completedTasks(self, query):
        """Method to list all completed Tasks."""
        query = Task.query(Task.completed == True)
        return query

    @Task.query_method(user_required=True, path="task/list/incomplete", name="list_incomplete",
                       query_fields=("limit", "pageToken"))
    def incompletedTasks(self, query):
        """Method to list all incomplete Tasks."""
        query = Task.query(Task.completed == False)
        return query

    @Task.method(request_fields=("id",), path="task/set_complete/{id}",
                 http_method="POST", name="markComplete")
    def markComplete(self, selectedTask):
        """Method to mark a task complete using its id."""
        if not selectedTask.from_datastore:
            raise endpoints.NotFoundException("Task not found")
        selectedTask.completed = True
        selectedTask.put()
        return selectedTask
