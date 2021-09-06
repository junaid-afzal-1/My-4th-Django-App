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



class Doctor(Person):

    junior = 'Junior'
    senior  = 'Senior'
    choice_lvl = [
                    (junior,'Junior'),
                    (senior,'Senior')
                ]  

    heart = 'Heart Surgen'
    brain = 'Brain Surgen'

    choice_specility = [
                        (heart,'Heart Surgen'),
                        (brain,'Brain Surgen')
                        ]       


    level = models.CharField(max_length=20,choices= choice_lvl)
    specility = models.CharField(max_length=15,choices=choice_specility)




class Teacher(Person):
    Eng = 'English'
    Urdu = 'Urdu'
    Math = 'Math'

    choice = [
        (Eng, 'English'),
        (Urdu, 'Urdu'),
        (Math, 'Math'),

    ]

    subject = models.CharField(max_length=10,choices=choice,default=None)





