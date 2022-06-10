from django.urls import path
from . import views



urlpatterns = [
    path("add", views.add_profile, name="add"),
    path("list", views.list_profile, name="list"),
    path("update/<profile_id>", views.update_profile, name="update"),
    path("delete/<profile_id>", views.delete_profile, name="delete"),
    path("add", views.add_comment, name="add"),
    path("list", views.list_comment, name="list"),
    path("update/<comment_id>", views.update_comment, name="update"),
    path("delete/<comment_id>", views.delete_comment, name="delete"),


    ]