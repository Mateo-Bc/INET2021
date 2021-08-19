from django.contrib import admin
from .models import *
# Register your models here.

class LocalAdmin(admin.ModelAdmin):
    list_display=['nomvre', 'max_cap', 'ac_cap', 'manager']

class ManagerAdmin(admin.ModelAdmin):
    list_display=['nomvre',]

admin.site.register(Local, LocalAdmin)
admin.site.register(Manager, ManagerAdmin)