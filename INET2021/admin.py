from django.contrib import admin
from .models import *
# Register your models here.

class LocalAdmin(admin.ModelAdmin):
    list_display=['name', 'max_cap', 'ac_cap', 'manager', 'call_percentage']

class ManagerAdmin(admin.ModelAdmin):
    list_display=['first_name', 'last_name']

admin.site.register(Local, LocalAdmin)
admin.site.register(Manager, ManagerAdmin)