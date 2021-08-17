from django.contrib import admin
from .models import *
# Register your models here.

class LocalAdmin(admin.ModelAdmin):
    list_display=['nomvre', 'max_cap', 'ac_cap', 'sum_hernesto', 'res_carlos']

admin.site.register(Local, LocalAdmin)