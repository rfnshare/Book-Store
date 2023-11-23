from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="books"),
    path("<int:id>", views.show, name="book"),
    path("review", views.review, name="review"),
]
