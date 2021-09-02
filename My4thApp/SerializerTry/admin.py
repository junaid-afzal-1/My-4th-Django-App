from django.contrib import admin
from .models import Employe, Student,Person

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
        'age',
        'contact',
    ]









admin.site.register(Person,PersonAdmin)
admin.site.register(Student)
admin.site.register(Employe)



