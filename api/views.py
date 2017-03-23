from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student, Hostel, State, College
from .serializers import StudentSerializer, CollegeSerializer, StateSerializer, HostelSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

class Login(APIView):
    def get(self, request):
        pass
    def post(self,request,format=None):
        u = request.POST['username']
        p= request.POST['password']
        #print(username + "  " + password )

        userobj= authenticate(username=u, password=p)
        print(userobj)
        userid=User.objects.get(user=)

        if userobj is not None:
            token=  Token.objects.get(user_id=userid)

            return Response([{'status': 'true'}])
        else:
            return Response({'status': 'false'})
# Create your views here.
class StateList(APIView):
    def get(self, request):
        state = State.objects.all()
        serializer = StateSerializer(state, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


class CollegeList(APIView):
    def get(self, request):
        college = College.objects.all()
        serializer = CollegeSerializer(college, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CollegeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


class HostelList(APIView):
    def get(self, request):
        hostel = Hostel.objects.all()
        serializer = HostelSerializer(hostel, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HostelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


class StudentList(APIView):
    def get(self, request):
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

# server /state/college
# obj=College.class FilterCollegeByStateList(APIView):
#     def get(self,request):
