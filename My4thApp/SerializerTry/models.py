from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    contact = models.CharField(max_length=15)

    


    def __str__(self):
        return self.name


class Student(Person):
    roll_no = models.CharField(max_length=5)
    section = models.CharField(max_length=1)
    cgpa = models.FloatField()
    semester = models.PositiveSmallIntegerField()


    def __str__(self):
        return (self.name + ' ' + self.roll_no)


class Employe(Person):
    salary = models.PositiveIntegerField()
    experience = models.PositiveIntegerField()

