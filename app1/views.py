from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import Movie_Serializer
from .models import Movies_list
from .pagination import First_paginator_class
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class watch_list(ModelViewSet):
    queryset = Movies_list.objects.all()
    serializer_class = Movie_Serializer
    pagination_class = First_paginator_class
