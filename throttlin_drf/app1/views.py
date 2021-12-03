from django.shortcuts import render
from .serializers import movie_ser
from .models import Movies
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework.authentication import TokenAuthentication,BasicAuthentication
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle

class Movie(ModelViewSet):
    queryset  = Movies.objects.all()
    serializer_class = movie_ser
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]