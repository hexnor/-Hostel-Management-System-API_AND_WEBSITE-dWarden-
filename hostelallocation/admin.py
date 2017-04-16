from django.contrib import admin
from .models import FinalAllocatedList
class FinalAllocatedListAdmin(admin.ModelAdmin):
    list_display = ('studentrollno', 'roomallocated')
admin.site.register(FinalAllocatedList,FinalAllocatedListAdmin)
