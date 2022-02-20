from . import views
from django.urls import path
from rest_framework import routers

from .views import HackerView, SpeechView

# router = routers.DefaultRouter()
# router.register('api/hacker', HackerView.as_view())

urlpatterns = [
    path('hacker', HackerView.as_view()),
    path('speech', SpeechView.as_view()),
]
