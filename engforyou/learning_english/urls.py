from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("topics/<int:topic_id>/", views.detail, name="detail"),
]