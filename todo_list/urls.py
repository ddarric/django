from django.urls import path
from . import views


urlpatterns = [
    path("", views.main_page, name = "main_page"),
    path("<int:pk>/", views.task_details, name = "task_details"),
    path("delete/<int:pk>/", views.delete_task, name = "delete_task"),
]