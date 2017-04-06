from django.shortcuts import render
from .models import HostelAllocation
from django.contrib import auth
# Create your views here.
def HostelAllotresult(request):
    u=auth.get_user(request)
    print(u.username)
    return render(request, 'ui/hostel.html')
