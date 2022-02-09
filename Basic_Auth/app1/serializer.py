from rest_framework import serializers
from app1.models import praveen
class Bhargav_ser(serializers.ModelSerializer):
    class Meta:
        model=praveen
        fields= "__all__"

