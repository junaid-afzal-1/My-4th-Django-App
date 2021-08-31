from django.shortcuts import render
from django.http.response import HttpResponse,JsonResponse
from django.http import request
from .models import Student
from .serializer import StudentSerializer
# Create your views here.



def mainS(request):
    #return HttpResponse('<H1>Hello Main SerializerTry</H1>')
    return render(request,'index.html')

def return_student(request):
    std = Student.objects.all()
    std_ser = StudentSerializer(std)

    return JsonResponse(std_ser.data,many=True)


