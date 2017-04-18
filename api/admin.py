from django.contrib import admin
from .models import State,College,Hostel,Branch,Student,TempVar
################## ####### ADMIN VIEW ####################################
class StateAdmin(admin.ModelAdmin):
    list_display = ('statename',)
admin.site.register(State,StateAdmin)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('collegename','statename',)
admin.site.register(College,CollegeAdmin)
class HostelAdmin(admin.ModelAdmin):
    list_display = ('hostelname','collegename','statename',)
admin.site.register(Hostel,HostelAdmin)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('branchname','hostelname','collegename','statename')
admin.site.register(Branch,BranchAdmin)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('studentrollno','studentname','hostelname','collegename','studentemailid','studentroomno','studentyear','studentpercentage','studentbloodgp')
admin.site.register(Student,StudentAdmin)
# admin.site.register(TempVar)
################################### ADMIN VIEW ####################################
