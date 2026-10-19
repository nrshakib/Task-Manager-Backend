from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView

from tasks.models import Task
from tasks.serializers import TaskSerializer
from tasks.utils import api_response

# get all tasks
class TaskListView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many = True)
        return api_response(
            message = "Get all tasks succesfully",
            data = serializer.data,
            http_status= status.HTTP_200_OK
        )

# get single task
class TaskDetailView(APIView):
    def get(self, request, id):
        try:
            task = Task.objects.get(id = id)

        except Task.DoesNotExist:
            return api_response(
                message = "Taks not found",
                data = None,
                status_text = "Error",
                http_status=status.HTTP_404_NOT_FOUND
            )

        serializer = TaskSerializer(task)

        return api_response(
            message= "Task retrieved succesfully",
            data = serializer.data,
            status_text="Success",
            http_status=status.HTTP_200_OK
        )

# get single task
class TaskDetailView(APIView):
    def get(self, request, id):
        try:
            task = Task.objects.get(id = id)

        except Task.DoesNotExist:
            return api_response(
                message = "Taks not found",
                data = None,
                status_text = "Error",
                http_status=status.HTTP_404_NOT_FOUND
            )

        serializer = TaskSerializer(task)

        return api_response(
            message= "Task retrieved succesfully",
            data = serializer.data,
            status_text="Success",
            http_status=status.HTTP_200_OK
        )

# create new task
class TaskCreateView(APIView):
    def post(self, request):
        serializer = TaskSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return api_response(
                message = "Task created succesfully",
                data = serializer.data,
                http_status=status.HTTP_201_CREATED
            )
        return api_response(
            message = "Failed to create task",
            data = serializer.errors,
            http_status= status.HTTP_400_BAD_REQUEST
        )


# update task
class TaskUpdateView(APIView):
    def put(self, request, id):
        return self.update_task(request, id, partial = False)

    def patch(self, request, id):
        return self.update_task(request, id, partial = True)

    def update_task(seld, request, id, partial):
        try:
            task = Task.objects.get(id = id)

        except Task.DoesNotExist:
            return api_response(
                message = 'Task not found',
                data = None,
                status_text="Not found",
                http_status=status.HTTP_404_NOT_FOUND
            )

        serializer = TaskSerializer(task, data = request.data, partial = partial)

        if serializer.is_valid():
            serializer.save()
            
            return api_response(
                message = "Task updated succefully",
                data = serializer.data,
                status_text="Success",
                http_status=status.HTTP_200_OK
            )

        return api_response(
            message = "Task update failed",
            data = None,
            status_text="Failed",
            http_status=status.HTTP_400_BAD_REQUEST
        )

class TaskDeleteView(APIView):
    def delete(self, request, id):
        try:
            task = Task.objects.get(id = id)

        except Task.DoesNotExist:
            return api_response(
                message = 'Task not found',
                data = None,
                status_text="Not found",
                http_status=status.HTTP_404_NOT_FOUND
            )

        task.delete()

        return api_response(
            message = 'Task deleted succesfully',
            data = None,
            status_text="Success",
            http_status=status.HTTP_200_OK
        )       
