from django.urls import path
from .views import resources

app_name = 'recomendations'

urlpatterns = [
    path("", resources, name="resources"),
]