from django.shortcuts import render, redirect, get_object_or_404

from apps.facturacion.forms import FacturaForm
from apps.facturacion.models import Factura


def listar_facturas(request):
    facturas = Factura.objects.all()
    return render(request, 'listar_facturas.html', {'facturas': facturas})


def crear_factura(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_facturas')
    else:
        form = FacturaForm()
    return render(request, 'crear_factura.html', {'form': form})


def editar_factura(request, id):
    factura = get_object_or_404(Factura, id=id)
    if request.method == 'POST':
        form = FacturaForm(request.POST, instance=factura)
        if form.is_valid():
            form.save()
            return redirect('listar_facturas')
    else:
        form = FacturaForm(instance=factura)
    return render(request, 'editar_factura.html', {'form': form})


def eliminar_factura(request, id):
    factura = get_object_or_404(Factura, id=id)
    factura.delete()
    return redirect('listar_facturas')


