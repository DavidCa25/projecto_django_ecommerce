from django.test import TestCase
from django.urls import reverse
from .models import Producto
from django.contrib.auth.models import User
from categoria.models import Categoria, CategoriaDieta

class ProductoModelTest(TestCase):
    def setUp(self):
        # Asegúrate de tener categorías válidas creadas
        self.categoria = Categoria.objects.create(categoriaSabor='Test Sabor', descripcion='Descripción de prueba')
        self.categoria_dieta = CategoriaDieta.objects.create(categoriaDieta='Test Dieta', descripcion='Descripción de prueba')

        self.producto = Producto.objects.create(
            nombreProducto='Test Producto',
            descripcion='Descripción de prueba',
            region='aguascalientes',
            categoria=self.categoria,
            categoriaD=self.categoria_dieta
        )

    def test_str_method(self):
        self.assertEqual(str(self.producto), 'Test Producto')

class IndexViewTest(TestCase):
    def setUp(self):
        # Asegúrate de tener categorías válidas creadas
        self.categoria = Categoria.objects.create(categoriaSabor='Test Sabor', descripcion='Descripción de prueba')
        self.categoria_dieta = CategoriaDieta.objects.create(categoriaDieta='Test Dieta', descripcion='Descripción de prueba')

        self.producto = Producto.objects.create(
            nombreProducto='Test Producto',
            descripcion='Descripción de prueba',
            region='aguascalientes',
            categoria=self.categoria,
            categoriaD=self.categoria_dieta
        )

    def test_index_view(self):
        response = self.client.get(reverse('productos:producto_views'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'productos/producto_views.html')

    # Agrega más casos de prueba para verificar la funcionalidad de tu filtro


