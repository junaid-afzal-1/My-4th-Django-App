from django import http
from django.shortcuts import render
from django.http.response import Http404, HttpResponse,JsonResponse
from django.http import request
from .models import Doctor, Student,Person,Employe, Teacher
from .serializer import DoctorSerializer, StudentSerializer,PersonSerializer,EmployeSerializer, TeacherSerializer
from rest_framework.views import APIView, View
from rest_framework.response import Response
from rest_framework import status, generics,viewsets
# Create your views here.



def mainS(request):
    #return HttpResponse('<H1>Hello Main SerializerTry</H1>')
    return render(request,'index.html')



def return_person(request):
    person = Person.objects.all()
    person_ser = PersonSerializer(person,many = True)

    return JsonResponse(person_ser.data,safe=False)



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


    