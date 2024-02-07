from django.db import models

class Categoria(models.Model):
    TIPO_CATEGORIAS_CHOICES = [
        ('dulce', 'Dulce'),
        ('salado', 'Salado'),
        ('amargo', 'Amargo'),
        ('ácido', 'Ácido'),
        ('picante', 'Picante'),
    ]
    categoriaSabor = models.CharField(max_length=20, choices=TIPO_CATEGORIAS_CHOICES, default='dulce')
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.categoriaSabor

class CategoriaDieta(models.Model):
    TIPO_CATEGORIASD_CHOICES = [
        ('mediterranea', 'Mediterranea'),
        ('vegetariana', 'Vegetariana'),
        ('Vegana', 'Vegana'),
        ('cetogénica', 'Cetogénica'),
        ('carnivoro', 'Carnivoro'),
    ]
    categoriaDieta = models.CharField(max_length=20, choices=TIPO_CATEGORIASD_CHOICES)
    descripcion = models.CharField(max_length=200)
   

    def __str__(self):
        return self.categoriaDieta
