from django.db import models

class Historial(models.Model):
    accion = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    detalles = models.TextField()

    def __str__(self):
        return f"{self.accion} - {self.fecha}"