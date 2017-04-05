from django.db import models
from api.models import Student
class HostelAllocation(models.Model):
    studentrollno=models.OneToOneField(Student, db_column='Roll No', on_delete=models.CASCADE, to_field='studentrollno',unique=True)
    studentchoice1=models.CharField(max_length=30,default=None)
    studentchoice2= models.CharField(max_length=30, default=None)
    studentchoice3= models.CharField(max_length=30, default=None)
    studentchoice4= models.CharField(max_length=30, default=None)
    studentchoice5= models.CharField(max_length=30, default=None)
    studentchoice6= models.CharField(max_length=30, default=None)
    studentchoice7= models.CharField(max_length=30, default=None)
    studentchoice8= models.CharField(max_length=30, default=None)
    studentchoice9= models.CharField(max_length=30, default=None)
    studentchoice10= models.CharField(max_length=30, default=None)

class FinalAllocatedList(models.Model):
    studentrollno=models.OneToOneField(Student, db_column='Roll No', on_delete=models.CASCADE, to_field='studentrollno',unique=True)
    roomallocated = models.CharField(max_length=30, default='NULL')
