from django.urls import path

from . import views

urlpatterns = [
    path("histories", views.Histories.as_view(), name="histories")
]