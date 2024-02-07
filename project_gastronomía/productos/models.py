from django.db import models
from categoria.models import Categoria, CategoriaDieta
from ingredientes.models import Ingredientes

class ProductoQuery(models.QuerySet):
    def visible(self):
        return self.filter(visible=True)

class ProductoFiltro(models.Manager):
    def get_queryset(self):
        return ProductoQuery(self.model, using=self._db)

    def filter_by_region(self, region):
        return self.get_queryset().filter(region__iexact=region)

    def filter_by_categoria_sabor(self, categoria):
        return self.get_queryset().filter(categoria__categoriaSabor__icontains=categoria)

    def filter_by_categoria_dieta(self, categoriaD):
        return self.get_queryset().filter(categoriaD__categoriaDieta__icontains=categoriaD)

class Producto(models.Model):
    TIPO_REGIONES_CHOICES = [
    ('aguascalientes', 'Aguascalientes'),
    ('baja_california', 'Baja California'),
    ('baja_california_sur', 'Baja California Sur'),
    ('campeche', 'Campeche'),
    ('coahuila', 'Coahuila'),
    ('colima', 'Colima'),
    ('chiapas', 'Chiapas'),
    ('chihuahua', 'Chihuahua'),
    ('ciudad_de_mexico', 'Ciudad de México'),
    ('durango', 'Durango'),
    ('guanajuato', 'Guanajuato'),
    ('guerrero', 'Guerrero'),
    ('hidalgo', 'Hidalgo'),
    ('jalisco', 'Jalisco'),
    ('estado_de_mexico', 'Estado de México'),
    ('michoacan', 'Michoacán'),
    ('morelos', 'Morelos'),
    ('nayarit', 'Nayarit'),
    ('nuevo_leon', 'Nuevo León'),
    ('oaxaca', 'Oaxaca'),
    ('puebla', 'Puebla'),
    ('queretaro', 'Querétaro'),
    ('quintana_roo', 'Quintana Roo'),
    ('san_luis_potosi', 'San Luis Potosí'),
    ('sinaloa', 'Sinaloa'),
    ('sonora', 'Sonora'),
    ('tabasco', 'Tabasco'),
    ('tamaulipas', 'Tamaulipas'),
    ('tlaxcala', 'Tlaxcala'),
    ('veracruz', 'Veracruz'),
    ('yucatan', 'Yucatán'),
    ('zacatecas', 'Zacatecas'),
]
    nombreProducto = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=200, default = "Sin Descripción")
    region = models.CharField(max_length=20, choices=TIPO_REGIONES_CHOICES, default="México")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)
    categoriaD = models.ForeignKey(CategoriaDieta, on_delete=models.CASCADE, default=1)
    ingredientes = models.ManyToManyField(Ingredientes)
    imgProducto = models.ImageField(upload_to='imgProductos', null=True)
    
    objects = ProductoFiltro()

    def __str__(self):
        return self.nombreProducto
    
