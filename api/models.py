from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
# Create your models here.
class State(models.Model):
    statename = models.CharField(max_length=25,unique=True)

    def __str__(self):
        return self.statename


class College(models.Model):
    statename= models.ForeignKey(State, db_column='state',on_delete=models.CASCADE,to_field='statename')#used to_field to convert int to text must set unique to true for operation
    collegename = models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.collegename

class Hostel(models.Model):
    statename= models.ForeignKey(State, on_delete=models.CASCADE,to_field='statename')
    collegename= models.ForeignKey(College, on_delete=models.CASCADE,to_field='collegename')
    hostelname= models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.hostelname
class Branch(models.Model):
    statename= models.ForeignKey(State, on_delete=models.CASCADE,to_field='statename')
    collegename= models.ForeignKey(College, on_delete=models.CASCADE,to_field='collegename')
    hostelname = models.ForeignKey(Hostel, on_delete=models.CASCADE, to_field='hostelname')
    branchname= models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.branchname


class Student(models.Model):
    statename= models.ForeignKey(State, on_delete=models.CASCADE,to_field='statename')
    collegename= models.ForeignKey(College, on_delete=models.CASCADE,to_field='collegename')
    hostelname = models.ForeignKey(Hostel, on_delete=models.CASCADE,to_field='hostelname')
    studentname=models.CharField(max_length=20)
    studentrollno=models.CharField(max_length=20)
    BG = (
        (u'1', u'A+'),
        (u'2', u'O+'),
        (u'3', u'B+'),
        (u'4', u'AB+'),
        (u'5', u'A-'),
        (u'6', u'O-'),
        (u'7', u'B-'),
        (u'8', u'AB-'),
    )
    studentbldgp = models.CharField(max_length=3,choices=BG)
    studentroomnoprefix = models.CharField(max_length=3)
    AggregatePercentage=models.FloatField(default=0)
    studentroomno = models.CharField(max_length=20)
    def __str__(self):
        return self.studentname + " -- " + self.studentrollno + " -- " + self.studentbldgp + " -- " + self.studentroomnoprefix + " -- " + self.studentroomno

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
from django.contrib.auth.models import User
from django import forms

