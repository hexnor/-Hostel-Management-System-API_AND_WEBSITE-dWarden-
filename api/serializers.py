from rest_framework import serializers
from .models import Student,State,College,Hostel,Branch



class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields='__all__'

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields='__all__'

class HostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields='__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields='__all__'
class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields='__all__'

