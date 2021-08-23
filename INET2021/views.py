from django.shortcuts import render, redirect

from .form import CalculateCap
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import datetime

# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
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

    current_hour = str(now.hour) + ":00"
    try:
        a = local.time.get(hour=current_hour)
    except:
        t = Time.objects.create(hour=current_hour,cant=0)
        local.time.add(t)
        local.save()
        a = local.time.get(hour=current_hour)

    if request.method == "POST":
        cap = CalculateCap(request.POST)
        if cap.is_valid():
            if cap.cleaned_data.get('option'):
                if local.ac_cap < local.max_cap:
                    a.cant +=1
                    a.save()
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
        'percentage': local.call_percentage(),
        'form':cap,

    }
    return render(request, 'local_view.html' , context)

def Statistics_View(request, pk):
    local = Local.objects.get(pk = pk)
    a = local.time.all()
    for i in a:
        print(type(i.hour.hour))
    print(local.time.all())
    context = {
        'times':a,
    }
    return render(request, 'statistics.html' , context)