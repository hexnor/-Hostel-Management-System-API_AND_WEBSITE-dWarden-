from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from api.config import authenticateuser
from .models import FinalAllocatedList
from api.models import Student
from django.contrib import auth
def HostelAllotresult(request):
    u=auth.get_user(request)
    d=Student.objects.filter(studentemailid=u.__str__())
    rollno=d[0].studentrollno
    var=FinalAllocatedList.objects.filter(studentrollno=rollno)
    if var.count()!=0:
        contents={
        'rollno':rollno,
        'roomallocated':var[0]
        }
    else:
        contents = {
            'rollno': rollno,
            'roomallocated': 'None'
        }
    return render(request, 'ui/hostel.html',{'contents':contents})


def allocate(choices, roll):
    status=False
    obj = FinalAllocatedList.objects.all()
    #checking for roll no and returning flase if found in hostelallocationlist
    if obj.filter(studentrollno=roll).count()==1:
        return False
    else:
        for i in choices:
            var=obj.filter(roomallocated=i)
            if var.count()==0:
                status=True
                FinalAllocatedList(roomallocated=i,studentrollno=roll).save()
                break
    return status


class Allot(APIView):

    def get(self, request):
        if authenticateuser.checkauth(request.META['HTTP_AUTHORIZATION'].__str__(), authenticateuser.defaulttoken) == 1:
            roll=request.GET['studentrollno']
            obj =FinalAllocatedList.objects.filter(studentrollno=roll)

            if obj.count()!=0:
                cv=obj.values('roomallocated')
                val=cv.first()
                val['studentrollno']=roll
                # room=val['roomallocated']
                # print(room)
                # p = {
                #     "rollno": "null"
                #
                # }
                # print(p)
                return JsonResponse(val)
            else:
                return JsonResponse({
                    "studentrollno":roll,
                    "roomallocated":"None"

                })




    def post(self, request, format=None):
        if authenticateuser.checkauth(request.META['HTTP_AUTHORIZATION'].__str__(), authenticateuser.defaulttoken) == 1:
            roll = request.POST['studentrollno']

            choices=[request.POST['choice1'],request.POST['choice2'],request.POST['choice3'],request.POST['choice4'],request.POST['choice5'],request.POST['choice6'],request.POST['choice7'],request.POST['choice8'],request.POST['choice9'],request.POST['choice10']]
            status=allocate(choices,roll)
            if status==True:
                return JsonResponse({"status":"Updated"})
            else:
                return JsonResponse({"status":"Notupdated"})