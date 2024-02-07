from django.db import models
from usuarios.models import Usuario

class Ingredientes(models.Model):
    nombreIngrediente = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponibilidad = models.BooleanField(default=True)
    vendedor = models.ForeignKey(Usuario,  on_delete=models.CASCADE, related_name='ingredientes', default=1)

    def __str__(self):
        return self.nombreIngrediente
