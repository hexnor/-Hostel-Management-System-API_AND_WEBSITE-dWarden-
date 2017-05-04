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
    choices = ((1, ("Search By Student Name")),
               (2, ("Search By Student Roll no")),
               (3, ("Search By Student Roll no And Year")),
               (4, ("Search by all the three filters")),
               )
    SearchType= forms.ChoiceField(choices=choices)

    def __init__(self, *args, **kwargs):
        super(SearchStudent, self).__init__(*args, **kwargs)
        self.fields['studentname'].label = "Enter Student Name"
        self.fields['studentyear'].label = "Enter Student Year"
        self.fields['studentrollno'].label = "Enter Student RollNo"
        self.fields['studentname'].help_text = "We want to be sure!"
    class Meta:
        model=Student
        fields = ['studentname','studentyear','studentrollno','SearchType']
