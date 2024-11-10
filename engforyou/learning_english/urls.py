from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("times", views.times, name="times"),
    path("speaking", views.speaking, name="speaking"),
    path("verbs", views.verbs, name="verbs"),
    path("topics", views.topics, name="topics"),
    path("topics/<int:pk>/", views.detail_topic, name='detail_topic'),
    path("lessons", views.lessons, name="lessons"),
    path('lessons/<int:pk>/', views.detail_lesson, name='detail_lesson'),
    path('random/', views.random_url, name='random_url'),
    
]