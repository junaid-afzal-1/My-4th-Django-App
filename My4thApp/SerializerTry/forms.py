from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)



class PersonForm(forms.Form):
    name = forms.CharField(label='Person name',max_length=50)
    age = forms.IntegerField(label= 'Age',min_value=1)
    contact = forms.CharField(label='Ph no',max_length=15)



class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username', 'password1', 'password2')

        
    
