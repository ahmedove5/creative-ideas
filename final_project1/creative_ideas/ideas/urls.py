from django.urls import path
from . import views



urlpatterns = [
    path("add", views.add_profile, name="add_profile"),
    path("list", views.list_profile, name="list_profile"),
    path("update/<business_id>", views.update_profile, name="update_profile"),
    path("delete/<business_id>", views.delete_profile, name="delete_profile"),
    path("add/comment", views.add_comment, name="add_comment"),
    path("list/comment", views.list_comment, name="list_comment"),
    path("delete/comment/<comment_id>", views.delete_comment, name="delete_comment"),
    path("add/offers", views.add_offers, name="add_offers"),
    path("list/offers", views.list_offers, name="list_offers"),
    path("update/offers/<offers_id>", views.update_ofers, name="update_offers"),
    path("delete/offers/<offers_id>", views.delete_offers, name="delete_offers"),

]