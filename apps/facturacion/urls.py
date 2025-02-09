from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_facturas, name='listar_facturas'),
    path('crear/', views.crear_factura, name='crear_factura'),
    path('editar/<int:id>/', views.editar_factura, name='editar_factura'),
    path('eliminar/<int:id>/', views.eliminar_factura, name='eliminar_factura'),
]