from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_notificaciones, name='listar_notificaciones'),
    path('crear/', views.crear_notificacion, name='crear_notificacion'),
    path('editar/<int:id>/', views.editar_notificacion, name='editar_notificacion'),
    path('eliminar/<int:id>/', views.eliminar_notificacion, name='eliminar_notificacion'),
]