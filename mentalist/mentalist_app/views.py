from django.shortcuts import render
from rest_framework import generics
from .serializers import HackerSerializer

from .models import Hacker


class HackerView(generics.ListCreateAPIView):
    queryset = Hacker.objects.all()
    serializer_class = HackerSerializer
