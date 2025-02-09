from django import forms
from .models import Historial

class HistorialForm(forms.ModelForm):
    class Meta:
        model = Historial
        fields = ['accion', 'detalles']