from rest_framework import serializers
from .models import Movies

class movie_serializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    def validate_name(self, name):
        if len(name)<2:
            return serializers.ValidationError('Name too short')
        else:
            return name

    def validate(self,data):
        if data['name'] == data['city']:
            return serializers.ValidationError('name is not equal to city')
        else:
            return data
    rate = serializers.IntegerField()
    city = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return Movies.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.rate = validated_data.get('rate', instance.rate)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance



