from django.shortcuts import render
from .models import Student
from .serializers import stud_ser
# Create your views here.
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST'])
def First(request):
    model = Student.objects.all()
    se = stud_ser(model,many=True)
    return Response(se.data)

class First_class(APIView):
    def get(self,request):
        model = Student.objects.all()
        se = stud_ser(model, many=True)
        return Response(se.data)
    def post(self,request):
        serializer = stud_ser(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class Detail_view(APIView):
    def put(self,request,id):
        model=Student.objects.get(id=id)
        se = stud_ser(data=request.data,instance=model)
        if se.is_valid():
            se.save()
        return Response(se.data)
    def delete(self,request):
        model = Student.objects.get(id=id)
        model.delete()
        return Response('/OKAY')






