from . import views
from django.urls import path
from rest_framework import routers

from .views import HackerView

# router = routers.DefaultRouter()
# router.register('api/hacker', HackerView.as_view())

urlpatterns = [
    path('api/hacker', HackerView.as_view())
]
