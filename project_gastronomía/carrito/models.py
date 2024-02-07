from django.db import models
from ingredientes.models import Ingredientes
from usuarios.models import Usuario

class Carrito(models.Model):
    Id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=1)
    Id_ingredientes = models.ForeignKey(Ingredientes, on_delete=models.CASCADE, default=1)
    cantidad = models.PositiveIntegerField(default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Carrito de {self.Id_usuario.email} - Producto: {self.Id_ingredientes.nombreIngrediente}"

