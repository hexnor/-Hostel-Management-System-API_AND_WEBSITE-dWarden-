from django.template import  loader
from rest_framework import parsers, renderers
from django.http import HttpResponse
class show:
    def home(self):
        p=loader.get_template('index.html')
        return HttpResponse(p.render(self))
    def login(self):
        p = loader.get_template('login.html')
        return HttpResponse(p.render(self))