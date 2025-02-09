from django.db import models

class Seguimiento(models.Model):
    tarea = models.CharField(max_length=100)
    completada = models.BooleanField(default=False)
    fecha_limite = models.DateField()

    def __str__(self):
        return self.tarea