from django.db import models

class Factura(models.Model):
    numero_factura = models.CharField(max_length=50, unique=True)
    cliente = models.CharField(max_length=100)
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Factura {self.numero_factura}"