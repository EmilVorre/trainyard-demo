from django.urls import path
from trainyard_demo import views

urlpatterns = [
    path("", views.index),
    path("health", views.health),
]