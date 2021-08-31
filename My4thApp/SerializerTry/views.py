from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import request
# Create your views here.



def mainS(request):
    #return HttpResponse('<H1>Hello Main SerializerTry</H1>')
    return render(request,'index.html')

