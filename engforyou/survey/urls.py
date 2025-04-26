from django.urls import path
from .views import survey_view, save_learning_profile
app_name = 'survey'

urlpatterns = [
    path('', survey_view, name='survey-view'),
    path('save/', save_learning_profile, name='save_learning_profile'),
]