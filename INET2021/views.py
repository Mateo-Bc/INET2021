from django.shortcuts import render, redirect

from .form import CalculateCap
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('homeView')
    else:
        form = UserRegisterForm()

    context = {'form': form}

    return render(request, 'register.html', context)



def HomeView(request):
    locals = Local.objects.all()

    queryset = request.GET.get("buscar")
    if queryset:
        locals = Local.objects.filter(
            Q(name__icontains = queryset) |
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
    hora = Time.objects.create('01:00',0)
    local.time.add(hora)
    print(local.time)
    if request.method == "POST":
        cap = CalculateCap(request.POST)
        if cap.is_valid():
            if cap.cleaned_data.get('option'):
                if local.ac_cap < local.max_cap:

                    local.ac_cap += 1
                    local.save()

            else:
                if local.ac_cap > 0:
                    local.ac_cap -= 1
                    local.save()
    else:
        cap = CalculateCap()
    context = {
        'name': local.name,
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