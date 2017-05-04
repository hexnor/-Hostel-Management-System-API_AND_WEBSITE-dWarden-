from django.db import models

class Usernamesave(models.Model):
    randomid=models.CharField(max_length=2,unique=True)
    username=models.CharField(max_length=32)

class Postlogin(models.Model):
    username=models.CharField(max_length=32)

class Notices(models.Model):
    title=models.CharField(max_length=60,unique=True)
    url=models.URLField(default="http://hmsonline.herokuapp.com")
    text=models.TextField(default="Notice is Empty")
    def __str__(self):
        return self.title