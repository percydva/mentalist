from rest_framework import serializers
from .models import Hacker, Speech


class HackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hacker
        fields = ('id', 'nickname',)


class SpeechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speech
        fields = ('id', 'speech',)
