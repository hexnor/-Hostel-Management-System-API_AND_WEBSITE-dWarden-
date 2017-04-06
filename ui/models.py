from django.db import models

class Usernamesave(models.Model):
    randomid=models.CharField(max_length=2,unique=True)
    username=models.CharField(max_length=32)

