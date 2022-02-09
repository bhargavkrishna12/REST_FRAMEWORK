from django.shortcuts import render

# Create your views here.
from.models import student_model
from .serializers import Student_ser
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly,IsAdminUser

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.viewsets import ModelViewSet

class Student_view(ModelViewSet):
    queryset = student_model.objects.all()
    serializer_class = Student_ser
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]