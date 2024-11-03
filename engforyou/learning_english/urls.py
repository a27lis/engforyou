from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("topics", views.topics, name="topics"),
    path("topics/<int:topic_id>/", views.detail, name="detail"),
]