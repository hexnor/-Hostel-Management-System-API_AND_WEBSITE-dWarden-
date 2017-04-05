from django.contrib import admin
from .models import HostelAllocation,FinalAllocatedList
class HostelAllocationAdmin(admin.ModelAdmin):
    list_display = ('studentrollno','studentchoice1','studentchoice2','studentchoice3','studentchoice4'
                    , 'studentchoice5','studentchoice6','studentchoice7','studentchoice8','studentchoice9'
                    , 'studentchoice10')
admin.site.register(HostelAllocation,HostelAllocationAdmin)
class FinalAllocatedListAdmin(admin.ModelAdmin):
    list_display = ('studentrollno', 'roomallocated')
admin.site.register(FinalAllocatedList,FinalAllocatedListAdmin)