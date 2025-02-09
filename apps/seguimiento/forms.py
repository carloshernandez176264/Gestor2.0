from django import forms
from .models import Seguimiento

class SeguimientoForm(forms.ModelForm):
    class Meta:
        model = Seguimiento
        fields = ['tarea', 'completada', 'fecha_limite']