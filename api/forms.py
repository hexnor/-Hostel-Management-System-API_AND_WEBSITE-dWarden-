from django.contrib.auth.forms import UserCreationForm
from .models import Student,College,Hostel,Branch,State
class UserForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ['username','first_name','last_name','email','password1','password2','is_staff']