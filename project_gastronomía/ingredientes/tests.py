from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy
from ingredientes.models import Ingredientes
from usuarios.models import Usuario

class IngredientesTestCase(TestCase):
    def setUp(self):
        self.user = Usuario.objects.create_user(
            email='testuser@example.com',
            password='testpassword',
            nombre='John',
            apellido='Doe',
            tipoUsuario='cliente',
            telefono='123456789',
            direccion='Test Address'
        )
        self.ingrediente = Ingredientes.objects.create(
            nombreIngrediente='Test Ingredient',
            descripcion='Test Description',
            precio=10.0,
            disponibilidad=True,
            vendedor=self.user
        )

    def test_ingrediente_str(self):
        self.assertEqual(str(self.ingrediente), 'Test Ingredient')

    

    def test_user_str(self):
        self.assertEqual(str(self.user), 'testuser@example.com')
