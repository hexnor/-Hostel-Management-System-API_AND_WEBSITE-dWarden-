from django.db import models


##################### TOKEN STARTED ###########################
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
####################### Token Done ##############################


###################### API MODEL ################################

class State(models.Model):
    statename=models.CharField(max_length=30,unique=True)
    def __str__(self):
        return self.statename

class College(models.Model):
    statename=models.ForeignKey(State, db_column='state',on_delete=models.CASCADE,to_field='statename')
    collegename= models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.collegename

class Hostel(models.Model):
    statename=models.ForeignKey(State, db_column='state',on_delete=models.CASCADE,to_field='statename')
    collegename= models.ForeignKey(College, db_column='college',on_delete=models.CASCADE,to_field='collegename')
    hostelname = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.hostelname

class Branch(models.Model):
    statename=models.ForeignKey(State, db_column='state',on_delete=models.CASCADE,to_field='statename')
    collegename= models.ForeignKey(College, db_column='college',on_delete=models.CASCADE,to_field='collegename')
    hostelname = models.ForeignKey(Hostel, db_column='hostel', on_delete=models.CASCADE, to_field='hostelname')
    branchname = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.branchname


class Student(models.Model):
    statename=models.ForeignKey(State, db_column='state',on_delete=models.CASCADE,to_field='statename')
    collegename= models.ForeignKey(College, db_column='college',on_delete=models.CASCADE,to_field='collegename')
    hostelname = models.ForeignKey(Hostel, db_column='hostel', on_delete=models.CASCADE, to_field='hostelname')
    branchname = models.ForeignKey(Branch, db_column='branch', on_delete=models.CASCADE, to_field='branchname')
    studentname=models.CharField(max_length=30,blank=True)
    studentrollno=models.CharField(max_length=30, unique=True,blank=True)
    studentemailid=models.CharField(max_length=30,unique=True)
    studentpercentage=models.FloatField(max_length=30)
    studentbloodgp=models.CharField(max_length=5)
    studentyear=models.CharField(max_length=10,blank=True)
    studentroomno=models.CharField(max_length=30)
    candonateblood=models.CharField(max_length=20,default="no")
    def __str__(self):
        return self.studentrollno

###################### API MODEL ################################
class TempVar(models.Model):
    keyid=models.CharField(max_length=2,unique=True)
    value=models.CharField(max_length=32)
