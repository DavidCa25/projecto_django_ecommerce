from django.db import models
from ingredientes.models import Ingredientes

class Inventario(models.Model):
    nombreIngredienteInv = models.ForeignKey(Ingredientes, on_delete=models.CASCADE, default=1)
    cantidad = models.PositiveIntegerField(default=0, verbose_name='Cantidad Disponible')

    def __str__(self):
        return f'{self.nombreIngredienteInv.nombreIngrediente} - Cantidad: {self.cantidad}'