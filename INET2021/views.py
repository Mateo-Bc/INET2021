from django.shortcuts import render
from .models import *

# Create your views here.

def HomeView(request):
    locals = Local.objects.all()
    context= {}
    return render(request, 'home.html' , context)

def Local_View(request, pk):
    local = Local.objects.get(pk = pk)
    context = {
        'nomvre': local.nomvre,
        'max_cap': local.max_cap,
        'ac_cap': local.ac_cap,

    }
    return render(request, 'local_view.html' , context)