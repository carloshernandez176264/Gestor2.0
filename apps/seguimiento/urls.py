from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_seguimientos, name='listar_seguimientos'),
    path('crear/', views.crear_seguimiento, name='crear_seguimiento'),
    path('editar/<int:id>/', views.editar_seguimiento, name='editar_seguimiento'),
    path('eliminar/<int:id>/', views.eliminar_seguimiento, name='eliminar_seguimiento'),
]