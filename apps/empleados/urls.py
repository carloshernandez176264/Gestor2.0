from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_empleados, name='listar_empleados'),
    path('crear/', views.crear_empleado, name='crear_empleado'),
    path('editar/<int:id>/', views.editar_empleado, name='editar_empleado'),
    path('eliminar/<int:id>/', views.eliminar_empleado, name='eliminar_empleado'),
]