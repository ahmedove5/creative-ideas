from django.urls import path
from . import views



urlpatterns = [
    path("add", views.add_profile, name="add_profile"),
    path("list", views.list_profile, name="list_profile"),
    path("update/<profile_id>", views.update_profile, name="update_profile"),
    path("delete/<profile_id>", views.delete_profile, name="delete_profile"),
    path("addcomm", views.add_comment, name="add_comment"),
    path("listcomm", views.list_comment, name="list_comment"),
    path("updatecomm/<comment_id>", views.update_comment, name="update_comment"),
    path("deletecomm/<comment_id>", views.delete_comment, name="delete_comment"),


    ]