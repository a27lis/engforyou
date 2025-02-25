from django.urls import path
from .views import (
    QiuzListView,
    quiz_view
)

app_name = 'quiz'

urlpatterns = [
    path('', QiuzListView.as_view(), name='main-view'),
    path('<pk>/', quiz_view, name='quiz-view'),
]
