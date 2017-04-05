from django.contrib.auth.models import User
from django import forms
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
