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
            new = Manager.objects.create(first_name=firstname,last_name=lastname)
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
        """print("hola")"""
        try:
            """print("1")"""
            hora = str(i) + ":00"
            local.time.get(hour=hora)
        except:
            """print("2")"""
            hora = str(i) + ":00"
            t = Time.objects.create(hour=hora, cant=0)
            local.time.add(t)
            local.save()

    current_hour = str(now.hour) + ":00"
    """try:
        print(local.time.filter(hour=current_hour))
        a = local.time.get(hour=current_hour)
    except:
        t = Time.objects.create(hour=current_hour,cant=0)
        local.time.add(t)
        local.save()"""
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

        """
        if cap.is_valid():
            if cap.cleaned_data.get('option'):
                if local.ac_cap < local.max_cap:
                    a.cant +=1
                    a.save()
                    print(a.cant)
                    local.ac_cap += 1
                    local.save()

                    if local.ac_cap == local.max_cap:
                        messages.warning(request, 'The store has reached its maxium capacity.')

            else:
                if local.ac_cap > 0:
                    local.ac_cap -= 1
                    local.save()
        """

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

@login_required(login_url='LoginView')
def Statistics_View(request):
    man = Manager.objects.get(first_name=request.user.first_name)
    local = Local.objects.filter(manager=man)
    try:
        a = local.time.all()
    except:
        nombre = "local de " + request.user.first_name
        loc = Local.objects.create(name=nombre,max_cap=10,ac_cap=0,address="None",manager=man)
    context = {
        'times':a,
    }
    return render(request, 'statistics.html' , context)