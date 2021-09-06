from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Doctor, Employe, Student,Person,Teacher

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
        'age',
        'contact',
    ]

class DoctorAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
        'level',
        'specility',

    ]



admin.site.register(Person,PersonAdmin)
admin.site.register(Student)
admin.site.register(Employe)
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Teacher)



