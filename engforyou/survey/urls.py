from django.urls import path
from .views import survey_view
app_name = 'survey'

urlpatterns = [
    path('', survey_view, name='survey-view')
]