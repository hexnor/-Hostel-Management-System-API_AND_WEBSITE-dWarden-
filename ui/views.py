from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from  django.contrib.auth.models import User
from api.models import TempVar
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

from .forms import UserForm, LoginForm, SearchBlood, SearchStudent


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
    username=''
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
            p = TempVar.objects.get(keyid=1)
            p.value=username
            p.save()
            return HttpResponseRedirect("/profile"+"?email=\'"+username+"\'")
        else:

            return HttpResponseRedirect("/ui/login")
from api.models import Student
from django.views import generic

class UserInfo(generic.ListView):
    model = Student
    context_object_name = 'student_info'
    username=''
    p = TempVar.objects.get(keyid="1")
    username=p.value
    queryset = Student.objects.filter(studentemailid=username) #add [:5]  to Get 5
    template_name = 'ui/personalinfo.html'




class UserBldsearch(View):
    form_class = SearchBlood
    template_name = 'ui/searchbloodgroup.html'

    ##for disaplaying form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    ##for processing form
    def post(self, request):
        studentbldgp = request.POST['studentbloodgp']
        p = TempVar.objects.get(keyid=2)
        p.value=studentbldgp
        p.save()
        p = TempVar.objects.get(keyid=2)
        print(p.value)
        return HttpResponseRedirect('bloodsearchresult')

class UserBldsearchResult(generic.ListView):
    model = Student
    context_object_name = 'student_info'
    # pk1 for user and pk2 for bloodgroup
    bloodgp=''
    bloodgp=TempVar.objects.get(keyid=2).value
    queryset = Student.objects.filter(studentbloodgp=bloodgp)  # add [:5]  to Get 5
    template_name = 'ui/searchbloodgroupresult.html'
class UserStusearch(View):
    form_class = SearchStudent
    template_name = 'ui/searchstudent.html'

    ##for disaplaying form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    ##for processing form
    def post(self, request):
        student = request.POST['studentname']
        p = TempVar.objects.get(keyid=3)
        p.value = student
        p.save()
        p = TempVar.objects.get(keyid=3)
        print(p.value)
        return HttpResponseRedirect('studentsearchresult')
class UserStusearchResult(generic.ListView):
    model = Student
    context_object_name = 'student_info'
    # pk1 for user and pk2 for bloodgroup
    student=''
    student=TempVar.objects.get(keyid=3).value
    queryset = Student.objects.filter(studentname__contains=student)  # add [:5]  to Get 5
    template_name = 'ui/searchstudentresult.html'


