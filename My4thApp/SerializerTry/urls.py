from collections import defaultdict
from django import urls
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from . import views
from .views import DoctorDetail, DoctorList, EmployeView,EmployeViewSpecific
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'teacher-list',views.TeacherViewSet,basename=None)




urlpatterns = [
    
    path('',views.mainS),
    path('person-list/',views.return_person),
    path('student-list/',views.return_student),
    path('employe-list/',EmployeView.as_view()),
    path('employe-list/<int:pk>/',EmployeViewSpecific.as_view()),
    path('doctor-list/',DoctorList.as_view()),
    path('doctor-list/<int:pk>/',DoctorDetail.as_view()),
    path("teacher-list/",include(router.urls)),
    path('form/',views.myform),
    path('add-name/',views.get_name),
    path('add-person/thanks/',views.thanks),
    path('send-m/', views.send_m),
    path('add-person/', views.insert_person),
    path('signup/', views.signup),
    path('signin/', views.signin),
    path('signout/', views.signout),
    path('reg/', views.reg),
]