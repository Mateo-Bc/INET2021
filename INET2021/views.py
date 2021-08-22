from django.shortcuts import render, redirect
from .models import *
from .forms import UserRegisterForm 
from django.db.models import Q
<<<<<<< HEAD
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

=======
from .form import *
>>>>>>> 7c844624b362da33c4a9df1aa2a2d594a9cd75f5
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