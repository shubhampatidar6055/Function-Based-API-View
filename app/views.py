from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from django.utils.decorators import method_decorator
# Create your views here.

@api_view(["POST", "DELETE", "GET", "PUT"])
def StudentAPI(request):
        
    if request.method == "POST":
        pythondata = request.data
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()   
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    elif request.method == "GET":
        pythondata = request.data
        id = pythondata.get("id")

        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        pythondata = request.data
        id = pythondata.get("id")
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=pythondata)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    elif request.method == "DELETE":
        pythondata = request.data
        id = pythondata.get("id")
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {"Message":"Data deleted sucessfully"}
        return Response(res)