from .models import Movies
from rest_framework import serializers

class movie_ser(serializers.Serializer):
    movie_id = serializers.IntegerField()
    movie_name = serializers.CharField(max_length=40)
    location = serializers.CharField(max_length=100)
