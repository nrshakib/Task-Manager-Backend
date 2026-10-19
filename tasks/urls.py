from django.urls import path

from tasks import views

urlpatterns = [
    path('all-tasks/', views.TaskListView.as_view(), name = 'all-tasks'),
    path('task/<int:id>', views.TaskDetailView.as_view(), name = 'single-task'),
    path('task/create/', views.TaskCreateView.as_view(), name = 'create-task'),
    path('task/update/<int:id>', views.TaskUpdateView.as_view(), name = 'update task'),
]