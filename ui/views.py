from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from  django.contrib.auth.models import User

def index(request):
    return render(request,'ui/index.html')







from django.views.decorators.csrf import csrf_exempt
@csrf_exempt ##included as without this it will not allow
def profile(request):
    username = request.GET.get('username', None)
    rollno =request.GET.get('rollno',None)
    college=request.GET.get('college',None)
    branch=request.GET.get('branch',None)
    aggregatepercentage=request.GET.get('aggregatepercentage', None)
    roomalloted=request.GET.get('roomalloted', None)
    emailid=request.GET.get('email',None)
    content={
        'username':username,
        'rollno':rollno,
        'college':college,
        'branch':branch,
        'aggregatepercentage':aggregatepercentage,
        'roomallocated':roomalloted,
        'emailid':emailid
    }
    print(content['emailid'])
    return render(request,'ui/profile.html',{'content':content})


def api(request):
    return  render(request,'ui/api.html')


def about(request):
    return render(request, 'ui/about.html')

from .forms import UserForm,LoginForm
class UserFormView(View):
    form_class=UserForm
    template_name = 'ui/register.html'
    ##for disaplaying form
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    ##for processing form
    def post(self,request):
        # form = self.form_class(request.POST) ##we are taking  the data after post submit to this
        # if form.is_valid():
        #     user=form.save(commit=False)
        #     email=form.cleaned_data['email']
        #     password=form.cleaned_data['password']
        #     user.set_password(password)
        #     user.save()
        email = request.POST['username']
        password = request.POST['password']
        username = request.POST['email']
        print(username + "     " + email + "    " + password)
        try:
            obj = User.objects.create_user(username, email, password, is_staff=True)
        except:
            print("key Exist")

        return HttpResponse('Congratulation You Are Successfully Registered'
                            '\n'
                            '<a href="/ui/login">Click to login </a>')
class LoginNow(View):
    form_class=LoginForm
    template_name = 'ui/login.html'
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        username= request.POST['email']
        password = request.POST['password']
        # print(username+"   "+password)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:

            login(request, user)

            return HttpResponseRedirect("/profile"+"?email=\'"+username+"\'")
        else:

            return HttpResponseRedirect("/ui/login")