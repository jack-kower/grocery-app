from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("grocery-list/", views.grocery_list, name="grocery-list"),
    path("add-grocery", views.add_grocery, name="add-grocery")
]