from rest_framework import serializers
from .models import Movies_list

class Movie_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Movies_list
        fields = '__all__'
    # movie_name = serializers.CharField(max_length=100)
    # movie_loc = serializers.CharField(max_length=100)
    # movie_Release = serializers.DateTimeField()
    # ticket_cost = serializers.IntegerField()
    # movie_rating = serializers.IntegerField()
#
# def create(self,instance):
