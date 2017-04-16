from django.db import models
from api.models import Student
class FinalAllocatedList(models.Model):
    studentrollno=models.CharField(max_length=30, db_column='Roll No',unique=True)
    roomallocated = models.CharField(max_length=30, default='NULL')
    def __str__(self):
        return self.roomallocated