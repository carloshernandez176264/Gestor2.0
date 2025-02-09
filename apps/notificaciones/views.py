from django.shortcuts import render, get_object_or_404, redirect
from .models import Notificacion
from .forms import NotificacionForm

def listar_notificaciones(request):
    notificaciones = Notificacion.objects.all()
    return render(request, 'listar_notificaciones.html', {'notificaciones': notificaciones})

def crear_notificacion(request):
    if request.method == 'POST':
        form = NotificacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_notificaciones')
    else:
        form = NotificacionForm()
    return render(request, 'crear_notificacion.html', {'form': form})

def editar_notificacion(request, id):
    notificacion = get_object_or_404(Notificacion, id=id)
    if request.method == 'POST':
        form = NotificacionForm(request.POST, instance=notificacion)
        if form.is_valid():
            form.save()
            return redirect('listar_notificaciones')
    else:
        form = NotificacionForm(instance=notificacion)
    return render(request, 'editar_notificacion.html', {'form': form})

def eliminar_notificacion(request, id):
    notificacion = get_object_or_404(Notificacion, id=id)
    notificacion.delete()
    return redirect('listar_notificaciones')