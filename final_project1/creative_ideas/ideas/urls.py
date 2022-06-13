from django.urls import path
from . import views



urlpatterns = [
    path("add", views.add_Business_idaea, name="add_Business_idea"),
    path("list", views.list_Business_idaea, name="list_Business_idea"),
    path("update/<business_id>", views.update_Business_idaea, name="update_Business_idea"),
    path("delete/<business_id>", views.delete_Business_idaea, name="delete_Business_idea"),
    path("add/comment", views.add_comment, name="add_comment"),
    path("list/comment", views.list_comment, name="list_comment"),
    path("delete/comment/<comment_id>", views.delete_comment, name="delete_comment"),
    path("add/offers", views.add_offers, name="add_offers"),
    path("list/offers", views.list_offers, name="list_offers"),
    path("update/offers/<offers_id>", views.update_offers, name="update_offers"),
    path("delete/offers/<offers_id>", views.delete_offers, name="delete_offers"),
    path("search/<idea>", views.search_ideas, name="search"),

]