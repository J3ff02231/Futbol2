from django.shortcuts import render, redirect
from .models import Equipo
from .forms import EquipoForm

# Create your views here.

def lista_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, "equipos/lista.html", {"equipos": equipos})

def crear_equipo(request):
    if request.method == "POST":
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_equipos")
    else:
        form = EquipoForm()
    return render(request, "equipos/crear.html", {"form": form})
