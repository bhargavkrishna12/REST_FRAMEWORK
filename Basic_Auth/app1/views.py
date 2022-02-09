from django.shortcuts import render

# Create your views here.

from .models import praveen
from .serializer import Bhargav_ser
from rest_framework.authentication import BasicAuthentication
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
class Student_view(ModelViewSet):
    queryset = praveen.objects.all()
    serializer_class = Bhargav_ser
    authentication_classes = [BasicAuthentication,]
    permission_classes = [IsAuthenticated,]