from django.shortcuts import render
from .models import *

# Create your views here.

def HomeView(request):
    locals = Local.objects.all()
    context= {
        'locales':locals,
    }
    return render(request, 'home.html' , context)

def Local_View(request, pk):
    local = Local.objects.get(pk = pk)
    context = {
        'nomvre': local.nomvre,
        'max_cap': local.max_cap,
        'ac_cap': local.ac_cap,
        'manager': local.manager

    }
    return render(request, 'local_view.html' , context)

def Statistics_View(request, pk):
    local = Local.objects.get(pk = pk)
    context = {
    }
    return render(request, 'statistics.html' , context)