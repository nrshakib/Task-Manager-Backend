from django.urls import path

from tasks import views

urlpatterns = [
    path('all-tasks/', views.TaskListView.as_view(), name = 'all-tasks'),
    path('task/create/', views.TaskCreateView.as_view(), name = 'create-task'),
]