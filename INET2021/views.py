from django.shortcuts import render, redirect

from .form import CalculateCap
from .models import *
from .forms import *
from django.db.models import Q  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
from django.db.models import F

# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            firstname = form.cleaned_data['first_name']
            lastname = form.cleaned_data['last_name']
            new = Manager.objects.create(first_name=firstname,last_name=lastname,username=username)
            new.save()

            messages.success(request, f'Usuario {username} creado')
            return redirect('login')
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
    now = datetime.datetime.now()
    local = Local.objects.get(pk = pk)

    for i in range(24):
        try:
            hora = str(i) + ":00"
            local.time.get(hour=hora)
        except:
            hora = str(i) + ":00"
            t = Time.objects.create(hour=hora, cant=0)
            local.time.add(t)
            local.save()

    current_hour = str(now.hour) + ":00"
    a = local.time.get(hour=current_hour)

    if request.method == "POST":
        cap = CalculateCap(request.POST)

        if "sum" in request.POST:
            if local.ac_cap < local.max_cap:
                a.cant += 1
                a.save()
                local.ac_cap += 1
                local.save()
            if local.ac_cap == local.max_cap:
                messages.warning(request, 'The store has reached its maxium capacity.')
        
        elif "res" in request.POST:
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
        'percentage': local.call_percentage(),
        'form':cap,
        'times':local.time.all(),
        'luse':local.manager.username,

    }
    return render(request, 'local_view.html' , context)