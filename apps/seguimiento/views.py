from django.shortcuts import render, get_object_or_404, redirect
from .models import Seguimiento
from .forms import SeguimientoForm

def listar_seguimientos(request):
    seguimientos = Seguimiento.objects.all()
    return render(request, 'listar_seguimientos.html', {'seguimientos': seguimientos})

def crear_seguimiento(request):
    if request.method == 'POST':
        form = SeguimientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_seguimientos')
    else:
        form = SeguimientoForm()
    return render(request, 'crear_seguimiento.html', {'form': form})

def editar_seguimiento(request, id):
    seguimiento = get_object_or_404(Seguimiento, id=id)
    if request.method == 'POST':
        form = SeguimientoForm(request.POST, instance=seguimiento)
        if form.is_valid():
            form.save()
            return redirect('listar_seguimientos')
    else:
        form = SeguimientoForm(instance=seguimiento)
    return render(request, 'editar_seguimiento.html', {'form': form})

def eliminar_seguimiento(request, id):
    seguimiento = get_object_or_404(Seguimiento, id=id)
    seguimiento.delete()
    return redirect('listar_seguimientos')