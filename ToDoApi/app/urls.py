from django.urls import path
from .views import task_list_create, task_details
urlpatterns = [
    path('tasks/', task_list_create, name="tasks"),
    path('tasks/<int:pk>', task_details, name="tasks_details"),

]
