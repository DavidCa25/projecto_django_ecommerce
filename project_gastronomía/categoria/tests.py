from django.test import TestCase
from .models import Categoria, CategoriaDieta

class CategoriaModelTest(TestCase):

    def test_str_method(self):
        categoria = Categoria(categoriaSabor='dulce', descripcion='Descripción de dulce')
        self.assertEqual(str(categoria), 'dulce')

    def test_default_value(self):
        categoria = Categoria(descripcion='Descripción sin sabor')
        self.assertEqual(categoria.categoriaSabor, 'dulce')

class CategoriaDietaModelTest(TestCase):

    def test_str_method(self):
        categoria_dieta = CategoriaDieta(categoriaDieta='mediterranea', descripcion='Descripción de mediterránea')
        self.assertEqual(str(categoria_dieta), 'mediterranea')
