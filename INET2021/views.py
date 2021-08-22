from django.shortcuts import render
from .models import *
from django.db.models import Q
from .form import *
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
    if request.method == "POST":
        print(local.ac_cap)
        cap = CalculateCap(request.POST)
        if cap.is_valid():
            if cap.cleaned_data.get('option'):
                if local.ac_cap < local.max_cap:
                    local.ac_cap += 1
                    local.save()
                    print(local.ac_cap)
            else:
                if local.ac_cap > 0:
                    local.ac_cap -= 1
                    local.save()
    else:
        cap = CalculateCap()
    context = {
        'nomvre': local.nomvre,
        'max_cap': local.max_cap,
        'ac_cap': local.ac_cap,
        'direccion': local.address,
        'percentage': local.cal_percentage(),
        'form':cap,

    }
    return render(request, 'local_view.html' , context)

def Statistics_View(request, pk):
    local = Local.objects.get(pk = pk)
    context = {
    }
    return render(request, 'statistics.html' , context)