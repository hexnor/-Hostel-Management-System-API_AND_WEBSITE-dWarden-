
from django.conf.urls import url
from django.contrib import admin
admin.site.site_header="Hostel Management System"
admin.site.site_title="Hostel Management System"

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

######################       API     PART  URLS          #################################
from rest_framework.urlpatterns import format_suffix_patterns
from api import  views as apiview
from rest_framework.authtoken import views as tokenview


urlpatterns+=[

    url(r'^meta$', apiview.display_meta, name='meta'),
    url(r'^api/student$', apiview.StudentList.as_view(),name='apistudent'),
    url(r'^api/state$', apiview.StateList.as_view(),name='apistate'),
    url(r'^api/college$', apiview.CollegeList.as_view(),name='apicollege'),
    url(r'^api/hostel$', apiview.HostelList.as_view(),name='apihostel'),
    url(r'^api/branch$', apiview.BranchList.as_view(),name='apibranch'),
    url(r'^api/token$', tokenview.obtain_auth_token,name='apitoken'),
    url(r'^api/login$', apiview.Login.as_view(),name='apilogin'),
    url(r'^api/register$', apiview.Register.as_view(),name='apiregister'),
    #url(r'^api/live$', apiview.Live.as_view(),name='apiregister')



]

######################       API     PART  URLS          #################################


from HmsApi import settings

######################      UI     PART  URLS    STARTS      #################################
from ui import views as uiview
urlpatterns+=[
url(r'^$', uiview.index,name='home'),
url(r'^index$', uiview.index,name='homepage'),
url(r'^api$', uiview.api,name='uiapi'),
url(r'^profile$', uiview.profile,name='profile'),
url(r'^about$', uiview.about,name='about'),
url(r'^ui/login$', uiview.LoginNow.as_view(), name='login'),
url(r'^ui/register$', uiview.UserFormView.as_view(), name='register'),
url(r'^action/info$', uiview.UserInfo.as_view(), name='info'),
url(r'^action/bloodsearch$', uiview.UserBldsearch.as_view(), name='bldsearch'),
url(r'^profile/update$', uiview.ProfileUpdate.as_view(), name='profileupdate'),
url(r'^action/studentsearch$', uiview.UserStusearch.as_view(), name='stusearch'),
# url(r'^action/studentsearchresult$', uiview.UserStusearchResult.as_view(), name='stusearch'),



]

######################       UI     PART  URLS  ENDS         #################################


######################       HOSTEL ALLOTMENT    PART  URLS   STARTS       #################################
from hostelallocation import views as hostelallocationview
urlpatterns+=[
url(r'^allotment/result$', hostelallocationview.HostelAllotresult, name='allotresult'),]

######################       HOSTEL ALLOTMENT  API  PART  URLS ENDS         #################################
urlpatterns+=[
url(r'^api/hostelallot$', hostelallocationview.Allot.as_view(), name='allotapi'),]