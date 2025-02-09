from django.shortcuts import render, get_object_or_404, redirect
from .models import Reporte
from .forms import ReporteForm

def listar_reportes(request):
    reportes = Reporte.objects.all()
    return render(request, 'listar_reportes.html', {'reportes': reportes})

def crear_reporte(request):
    if request.method == 'POST':
        form = ReporteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_reportes')
    else:
        form = ReporteForm()
    return render(request, 'crear_reporte.html', {'form': form})

def editar_reporte(request, id):
    reporte = get_object_or_404(Reporte, id=id)
    if request.method == 'POST':
        form = ReporteForm(request.POST, instance=reporte)
        if form.is_valid():
            form.save()
            return redirect('listar_reportes')
    else:
        form = ReporteForm(instance=reporte)
    return render(request, 'editar_reporte.html', {'form': form})

def eliminar_reporte(request, id):
    reporte = get_object_or_404(Reporte, id=id)
    reporte.delete()
    return redirect('listar_reportes')