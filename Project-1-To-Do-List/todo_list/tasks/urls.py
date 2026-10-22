from django.urls import path
from . import views
app_name = "tasks"
urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("<int:task_id>/toggle/", views.toggle, name="toggle"),
    path("<int:task_id>/delete/", views.delete, name="delete"),
]
