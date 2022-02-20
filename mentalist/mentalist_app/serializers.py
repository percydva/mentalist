from rest_framework import serializers
from .models import Hacker


class HackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hacker
        fields = ('id', 'nickname',)
