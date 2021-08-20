from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.

def HomeView(request):
    locals = Local.objects.all()

    queryset = request.GET.get("buscar")
    if queryset:
        locals = Local.objects.filter(
            Q(nomvre__icontains = queryset) |
            Q(address__icontains = queryset)
        ).distinct()

    if (queryset == None):
        queryset = ""

    context= {
        'locales': locals,
        'buscar': queryset,
    }
    return render(request, 'home.html' , context)

def Local_View(request, pk):
    local = Local.objects.get(pk = pk)
    context = {
        'nomvre': local.nomvre,
        'max_cap': local.max_cap,
        'ac_cap': local.ac_cap,
        'direccion': local.address,
        'percentage': local.percentage,

    }
    return render(request, 'local_view.html' , context)

def Statistics_View(request, pk):
    local = Local.objects.get(pk = pk)
    context = {
    }
    return render(request, 'statistics.html' , context)