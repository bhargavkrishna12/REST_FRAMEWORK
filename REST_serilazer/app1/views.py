from django.shortcuts import render,HttpResponseRedirect
# Create your views here.
from.serializers import movie_serializer
from .models import Movies
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET','POST'])
def one(request):
    if request.method =='GET':
        model = Movies.objects.all()
        serializer = movie_serializer(model,many=True)
        return Response(serializer.data)
    if request.method =='POST':
        serializer=movie_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_208_ALREADY_REPORTED)

@api_view(['GET','PUT','DELETE'])
def two(request, pk=id):
    if request.method=='GET':
        try:
            movie = Movies.objects.get(id=pk)
        except Movies.DoesNotExist:
            return Response({'Error:''NotFound'},status=status.HTTP_404_NOT_FOUND)
        se = movie_serializer(movie)
        return Response(se.data)
    if request.method == 'PUT':
        movie = Movies.objects.get(pk=pk)
        serializer = movie_serializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status==status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    if request.method=='DELETE':
        movie = Movies.objects.get(pk=pk)
        movie.delete()
        return HttpResponseRedirect('/two',status=status.HTTP_204_NO_CONTENT)



