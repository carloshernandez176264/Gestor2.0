from django.shortcuts import render, get_object_or_404, redirect
from .models import Historial
from .forms import HistorialForm

def listar_historial(request):
    historiales = Historial.objects.all()
    return render(request, 'listar_historial.html', {'historiales': historiales})

def crear_historial(request):
    if request.method == 'POST':
        form = HistorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_historial')
    else:
        form = HistorialForm()
    return render(request, 'crear_historial.html', {'form': form})

def editar_historial(request, id):
    historial = get_object_or_404(Historial, id=id)
    if request.method == 'POST':
        form = HistorialForm(request.POST, instance=historial)
        if form.is_valid():
            form.save()
            return redirect('listar_historial')
    else:
        form = HistorialForm(instance=historial)
    return render(request, 'editar_historial.html', {'form': form})

def eliminar_historial(request, id):
    historial = get_object_or_404(Historial, id=id)
    historial.delete()
    return redirect('listar_historial')