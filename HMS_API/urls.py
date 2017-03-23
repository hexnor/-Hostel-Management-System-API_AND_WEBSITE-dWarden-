"""HMS_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from api import views as show
from rest_framework.authtoken import views as resview
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/student/', show.StudentList.as_view()),
    url(r'^api/state/', show.StateList.as_view()),
    url(r'^api/college/', show.CollegeList.as_view()),
    url(r'^api/hostel/', show.HostelList.as_view()),
    url(r'^api/token/', resview.obtain_auth_token),
    url(r'^api/login', show.Login.as_view()),
]
urlpatterns=format_suffix_patterns(urlpatterns)