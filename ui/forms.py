from django.contrib.auth.models import User
from django import forms
from api.models import Student
##here we specify what fields to displayin the template specified in view
class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','email','password']

class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ['username', 'password']
class SearchBlood(forms.ModelForm):
    class Meta:
        model=Student
        fields = ['studentbloodgp']
class SearchStudent(forms.ModelForm):
    class Meta:
        model=Student
        fields = ['studentname']