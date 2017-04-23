from api.config import authenticateuser
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Student, Hostel, State, College, Branch
from .serializers import StudentSerializer, CollegeSerializer, StateSerializer, HostelSerializer,BranchSerializer

def display_meta(request):
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
class StateList(APIView):

    def get(self, request):
        if authenticateuser.checkauth(request.META['HTTP_AUTHORIZATION'].__str__(),authenticateuser.defaulttoken)==1:
            state = State.objects.all()
            serializer = StateSerializer(state, many=True)
            return Response(serializer.data)
        else:
            pass

    def post(self, request, format=None):
        if authenticateuser.checkauth(request.META['HTTP_AUTHORIZATION'].__str__(),authenticateuser.defaulttoken)==1:
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
        if authenticateuser.checkauth(request.META['HTTP_AUTHORIZATION'].__str__(),authenticateuser.defaulttoken)==1:
            college = College.objects.all()
            serializer = CollegeSerializer(college, many=True)
            return Response(serializer.data)
        else:
            pass

    def post(self, request, format=None):
        if authenticateuser.checkauth(request.META['HTTP_AUTHORIZATION'].__str__(),authenticateuser.defaulttoken)==1:
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
        #u= re.sub('[!@#$.]', '', u)
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
            print (token+"\n"+authenticateuser.defaulttoken)
            if headertoken==authenticateuser.defaulttoken:
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
        emailid = request.POST['username']
        password = request.POST['password']
        username = request.POST['emailid']
        #username = re.sub('[.!@#$]', '', username)
        updaterequired=request.POST['updaterequired']
        p = {

            "created": "false",
            "token": "null",
            "update":"false"#return false if no updatation done or return true if some updation done
        }
        try:
            if updaterequired == 'false':
                obj=User.objects.create_user(username,emailid,password,is_staff=True)
                p['created'] = 'true'
               # obj.email_user("Registered succesfully","Thanks For registering on Hostel Management System", from_email='yokeshrana@gmail.com', )
            elif updaterequired == 'true':
                p['created'] = 'true'
                obj = User.objects.get(username=username)
                print(obj)

                if username not in ['admin','default']:
                    obj.set_password(password)
                    obj.save()
                    p['update'] = 'updated'
                else:
                    p['update'] = 'cant update admin bro'

            p['token'] = Token.objects.get(user__username=username).__str__()

            return JsonResponse(p)
        except:
            return JsonResponse(p)



class HostelList(APIView):
    def get(self, request):
        if authenticateuser.checkauth(request.META['HTTP_AUTHORIZATION'].__str__(),authenticateuser.defaulttoken)==1:
            hostel = Hostel.objects.all()
            serializer = HostelSerializer(hostel, many=True)
            return Response(serializer.data)

        else:
            pass

    def post(self, request, format=None):
        if authenticateuser.checkauth(request.META['HTTP_AUTHORIZATION'].__str__(),authenticateuser.defaulttoken)==1:
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
        if authenticateuser.checkauth(request.META['HTTP_AUTHORIZATION'].__str__(),authenticateuser.defaulttoken)==1:
            student = Student.objects.filter(studentrollno=request.GET['studentrollno'])
            serializer = StudentSerializer(student, many=True)
            return Response(serializer.data)
        else:
            pass


    def post(self, request, format=None):
        if authenticateuser.checkauth(request.META['HTTP_AUTHORIZATION'].__str__(),authenticateuser.defaulttoken)==1:
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

class BranchList(APIView):
    def get(self, request):
        if authenticateuser.checkauth(request.META['HTTP_AUTHORIZATION'].__str__(),authenticateuser.defaulttoken)==1:
            branch = Branch.objects.all()
            serializer = CollegeSerializer(branch, many=True)
            return Response(serializer.data)
        else:
            pass

    def post(self, request, format=None):
        if authenticateuser.checkauth(request.META['HTTP_AUTHORIZATION'].__str__(),authenticateuser.defaulttoken)==1:
            serializer = BranchSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )

        else:
            pass

