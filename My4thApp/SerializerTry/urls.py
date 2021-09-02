from django.urls import path
from django.urls.conf import include
from . import views
from .views import EmployeView,EmployeViewSpecific


urlpatterns = [
    path('',views.mainS),
    path('person-list/',views.return_person),
    path('student-list/',views.return_student),
    path('employe-list/',EmployeView.as_view()),
    path('employe-list/<int:pk>/',EmployeViewSpecific.as_view()),
]