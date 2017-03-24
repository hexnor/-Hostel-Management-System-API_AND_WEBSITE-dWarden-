from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student, Hostel, State, College
from .serializers import StudentSerializer, CollegeSerializer, StateSerializer, HostelSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.http import JsonResponse
# source ~/apienv/bin/activate

# Create your views here.
class StateList(APIView):

    def get(self, request):
        if checkauth(request.META['HTTP_AUTHORIZATION'].__str__(),defaulttoken)==1:
            state = State.objects.all()
            serializer = StateSerializer(state, many=True)
            return Response(serializer.data)
        else:
            pass

    def post(self, request, format=None):
        if checkauth(request.META['HTTP_AUTHORIZATION'].__str__(), defaulttoken)==1:
            serializer = StateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
        else:
            pass

class CollegeList(APIView):
    def get(self, request):
        if checkauth(request.META['HTTP_AUTHORIZATION'].__str__(), defaulttoken)==1:
            college = College.objects.all()
            serializer = CollegeSerializer(college, many=True)
            return Response(serializer.data)
        else:
            pass

    def post(self, request, format=None):
        if checkauth(request.META['HTTP_AUTHORIZATION'].__str__(), defaulttoken)==1:
            serializer = CollegeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )

        else:
            pass


class Login(APIView):
    #print("hello")
    def get(self, request):
        pass
    def post(self,request,format=None):
        u = request.POST['username']
        p= request.POST['password']
        #print(u + "  " + p)
        #print("hello")
        userobj= authenticate(username=u, password=p)
       # print(userobj)
        p = {
            "status": "false",
            "token": "null"
        }

        headertoken=request.META['HTTP_AUTHORIZATION'].__str__()
        print(headertoken)
        if userobj is not None:
            token = Token.objects.get(user__username=u).__str__()
            print (token+"\n"+defaulttoken)
            if headertoken==defaulttoken:
                p['status'] = 'true'
                p['token'] = token
                return JsonResponse(p)
            else:
                p['status'] = 'false'
                p['token'] = 'Invalid_token'
                return JsonResponse(p)
        else:
            p['status'] = 'false'
            p['token'] = 'null'
            return JsonResponse(p)

class Register(APIView):
    def get(self, request):
        pass
    def post(self,request,format=None):
        username = request.POST['username']
        password= request.POST['password']
        email= request.POST['email']

        print(u + "  " + p)
        print("hello")
        userobj= authenticate(username=u, password=p)
       # print(userobj)
        p = {
            "status": "false",
            "token": "null"
        }

        headertoken=request.META['HTTP_AUTHORIZATION'].__str__()
        print(headertoken)
        if userobj is not None:
            token = Token.objects.get(user__username=u).__str__()
            print (token+"\n"+defaulttoken)
            if headertoken==defaulttoken:
                p['status'] = 'true'
                p['token'] = token
                return JsonResponse(p)
            else:
                p['status'] = 'false'
                p['token'] = 'Invalid_token'
                return JsonResponse(p)
        else:
            p['status'] = 'false'
            p['token'] = 'null'
            return JsonResponse(p)


class HostelList(APIView):
    def get(self, request):
        if checkauth(request.META['HTTP_AUTHORIZATION'].__str__(), defaulttoken)==1:
            hostel = Hostel.objects.all()
            serializer = HostelSerializer(hostel, many=True)
            return Response(serializer.data)

        else:
            pass

    def post(self, request, format=None):
        if checkauth(request.META['HTTP_AUTHORIZATION'].__str__(), defaulttoken)==1:
            serializer = HostelSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(

                    serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
        else:
            pass

class StudentList(APIView):

    def get(self, request):
        if checkauth(request.META['HTTP_AUTHORIZATION'].__str__(), defaulttoken) == 1:
            student = Student.objects.all()
            serializer = StudentSerializer(student, many=True)
            return Response(serializer.data)
        else:
            pass


    def post(self, request, format=None):
        if checkauth(request.META['HTTP_AUTHORIZATION'].__str__(), defaulttoken)==1:
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
        else:
            pass

# obj=College.class FilterCollegeByStateList(APIView):

defaulttoken='token 6d793111878d993460b68dcb78eb618adf20883c'
def checkauth(usertoken,databaseusertoken):
    if usertoken==databaseusertoken:
        return 1
    else:
        return 0
