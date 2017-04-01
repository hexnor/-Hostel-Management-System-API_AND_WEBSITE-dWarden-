from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from api import  views as apiview
from serve import show as fireitnow
from rest_framework.authtoken import views as tokenview
from django.contrib.auth import views as auth_views
urlpatterns = [
#### API PART ####
    url(r'^admin/', admin.site.urls,),
    url(r'^api/student$', apiview.StudentList.as_view(),name='apistudent'),
    url(r'^api/state$', apiview.StateList.as_view(),name='apistate'),
    url(r'^api/college$', apiview.CollegeList.as_view(),name='apicollege'),
    url(r'^api/hostel$', apiview.HostelList.as_view(),name='apihostel'),
    url(r'^api/branch$', apiview.BranchList.as_view(),name='apibranch'),
    url(r'^api/token$', tokenview.obtain_auth_token,name='apitoken'),
    url(r'^api/login$', apiview.Login.as_view(),name='apilogin'),
    url(r'^api/register$', apiview.Register.as_view(),name='apiregister'),
### WEB UI PART ###
    url(r'^$', fireitnow.home, name="home"),
    url(r'index.html$', fireitnow.home, name="homepage"),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
url(r'^api.html$', auth_views.login, {'template_name': 'api.html'}, name='api'),
   # url(r'^logout$', apiview.auth_views.logout, {'next_page' : '/login'},name='logout'),
    #url(r'^register$', apiview.UserFormView.as_view(),{'template_name': 'register.html'}, name='register'),
]
urlpatterns=format_suffix_patterns(urlpatterns)