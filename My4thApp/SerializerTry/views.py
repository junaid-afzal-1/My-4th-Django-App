from django import http
import django
from django.contrib.auth import authenticate,login, logout
from django.shortcuts import render
from django.http.response import Http404, HttpResponse, HttpResponseRedirect,JsonResponse
from django.http import request
from .models import Doctor, Student,Person,Employe, Teacher
from .serializer import DoctorSerializer, StudentSerializer,PersonSerializer,EmployeSerializer, TeacherSerializer
from rest_framework.views import APIView, View
from rest_framework.response import Response
from rest_framework import status, generics,viewsets
from .forms import NameForm,PersonForm, UserForm
from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth.forms import AuthenticationForm




def myform(request):
    return render(request,'name.html')





def mainS(request):
    #return HttpResponse('<H1>Hello Main SerializerTry</H1>')
    return render(request,'index.html')



def return_person(request):
    person = Person.objects.all()
    person_ser = PersonSerializer(person,many = True)

    return JsonResponse(person_ser.data,safe=False)


def add_person(request):
    data = request.POST
    return HttpResponse(request, data)



def return_student(request):
    std = Student.objects.all()
    std_ser = StudentSerializer(std, many = True)

    return JsonResponse(std_ser.data,safe=False)

    


class EmployeView(APIView):
    ### return Json to front end
    def get(self,request):
        emp = Employe.objects.all()
        emp_ser = EmployeSerializer(emp,many = True)
        return Response({'Employe': emp_ser.data})


        
    #Front end to database
    def post(self,request):
        emp_name = request.data.get('name')

        emp_ser = EmployeSerializer(data=request.data)
        if emp_ser.is_valid():
            emp_ser.save()
            return Response({'Done': 'Employe {} saved successfully'.format(emp_name)})
        else:
            return Response(emp_ser._errors,status=status.HTTP_400_BAD_REQUEST)


    def create(self,validated_data):
        return Employe.objects.create(**validated_data)








class EmployeViewSpecific(APIView):
    def get(self,request,pk):
        emp = self.get_object(pk)
        emp_ser = EmployeSerializer(emp)
        return Response({'Employe': emp_ser.data})


    def get_object(self,pk):
        try:
            return Employe.objects.get(pk=pk)
        except Employe.DoesNotExist:
            raise Http404


    #Update Employe Record

    def put(self,request,pk):
        emp =self.get_object(pk)
        old_ser = EmployeSerializer(emp)
        s = {'Update Successfull': 'Employe: {} is updated to Employe: {}'.format(old_ser.data,request.data)}
        emp_ser = EmployeSerializer(emp,data = request.data)
        if emp_ser.is_valid():
            emp_ser.save()
            return Response(s)
        else:
            return Response(emp_ser.errors,status=status.status.HTTP_400_BAD_REQUEST)


    #Delete Employe Record
    def delete(self,request,pk):
        emp = self.get_object(pk)
        emp.delete()
        return Response('Record Delete Successfully',status=status.HTTP_204_NO_CONTENT)

   

class DoctorList(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()







def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            



            return HttpResponseRedirect('thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})


def thanks(request):
    return HttpResponse("<h1>Thanks for giving us time</h1>")



def send_m(request):
    send_mail(
    subject= 'test mail',
    message= 'mail from django',
    from_email= 'abc@gmail.com',
    recipient_list = ['junaidafzal7274@gmail.com']
    #fail_silently=False,
    )

    return HttpResponse('<H1>MAIL send</h1>')


def insert_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)

        ser = PersonSerializer(data =form.data)
        if ser.is_valid():
            p = Person()
            p.name = ser.data.get('name')
            p.age = ser.data.get('age')
            p.contact = ser.data.get('contact')

            p.save()
            return HttpResponse('<h1>Peron Add Successfully</h1>')

        else:
            return HttpResponse('<h1>Bad Response</h1>')
    
    else:
        form = PersonForm()

    return render(request, 'add_person.html', {'form': form})




def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)


        if user_form.is_valid():
            user_form.save()
            return render(request,'signin.html')

        else:
            return HttpResponse('<h1>Bad Response</h1>')
    
    else:
        form = UserForm()

    return render(request, 'signup.html', {'form': form})




def signin(request):
    if request.method == 'POST':


        form = AuthenticationForm(request=request,data = request.POST)
        if form.is_valid():
            usr_name = form.cleaned_data.get('username')
            usr_password = form.cleaned_data.get('password')
            user = authenticate(username = usr_name, password = usr_password)

            if user is not None:
                login(request,user)
                
                return HttpResponse('<h1>Welcome {}</h1>'.format(request.POST.get('username')))
            else:
                return HttpResponse('<h1>User {} Not Exist </h1>'.format(request.POST.get('username')))
        else:
            return HttpResponse('<h1>Invalid Input</h1>')
    else:
        form = AuthenticationForm()
        return render(request = request,
               template_name = "signin.html",
               context={"form":form})
                    



def reg(request):
    return render(request=request,template_name='registration.html')


def signout(request):

    user = request.user
    name = user.username
    logout(request)
    return HttpResponse('Good Bye {}'.format(name))