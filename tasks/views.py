from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from tasks.models import Task
from tasks.serializers import TaskSerializer
from tasks.utils import api_response

# get all tasks
class TaskListView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many = True)
        return Response(serializer.data)
        # return api_response(
        #     message = "Get all tasks succesfully",
        #     data = serializer.data,
        #     http_status= status.HTTP_200_OK
        # )

# create new task
class TaskCreateView(APIView):
    def post(self, request):
        serializer = TaskSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
            # return api_response(
            #     message = "Task created succesfully",
            #     data = serializer.data,
            #     http_status=status.HTTP_201_CREATED
            # )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        # return api_response(
        #     message = "Failed to create task",
        #     data = serializer.errors,
        #     http_status= status.HTTP_400_BAD_REQUEST
        # )
        