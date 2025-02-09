from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_reportes, name='listar_reportes'),
    path('crear/', views.crear_reporte, name='crear_reporte'),
    path('editar/<int:id>/', views.editar_reporte, name='editar_reporte'),
    path('eliminar/<int:id>/', views.eliminar_reporte, name='eliminar_reporte'),
]