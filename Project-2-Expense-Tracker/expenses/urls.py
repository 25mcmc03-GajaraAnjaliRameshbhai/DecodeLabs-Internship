from django.urls import path
from . import views
app_name = "expenses"
urlpatterns = [path("", views.index, name="index"), path("add/", views.add, name="add"), path("<int:expense_id>/delete/", views.delete, name="delete")]
