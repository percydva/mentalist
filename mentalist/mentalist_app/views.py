import json
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import HackerSerializer, SpeechSerializer
from .nlp_model import dblr, train
from .models import Hacker, Speech


class HackerView(generics.ListCreateAPIView):
    queryset = Hacker.objects.all()
    serializer_class = HackerSerializer


class SpeechView(generics.ListCreateAPIView):
    queryset = Speech.objects.all()
    serializer_class = SpeechSerializer

    def post(self, request):
        serializer = SpeechSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data['speech'])
            model = dblr.load_model()
            features = dblr.tokenize_text(serializer.data['speech'])
            prediction = model.predict(features)[0]
            print(prediction)
            return Response(data=prediction, status=status.HTTP_201_CREATED)
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

