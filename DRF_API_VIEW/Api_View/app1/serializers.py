from rest_framework import serializers
from .models import Student
class stud_ser(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

