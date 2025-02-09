from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_historial, name='listar_historial'),
    path('crear/', views.crear_historial, name='crear_historial'),
    path('editar/<int:id>/', views.editar_historial, name='editar_historial'),
    path('eliminar/<int:id>/', views.eliminar_historial, name='eliminar_historial'),
]