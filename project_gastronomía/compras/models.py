from django.db import models
from ingredientes.models import Ingredientes
from usuarios.models import Usuario
from django.db.models import Sum
from carrito.models import Carrito

class Compra(models.Model):
    Id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    Id_ingredientes = models.ForeignKey(Ingredientes, on_delete=models.CASCADE, related_name="ingrediente_compra", default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    

    def __str__(self):
        return f"Compra de {self.Id_usuario.nombre} - {self.Id_ingredientes.nombreIngrediente} - {self.fecha_compra}"
    
   
   