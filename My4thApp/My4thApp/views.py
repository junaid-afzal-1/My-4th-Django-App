from django.http import HttpResponse
from django.shortcuts import render

def web_main(request):
    #return HttpResponse('<h1>Welcome To Django Main Page</h1>')

    return render(request,'main_page.html')