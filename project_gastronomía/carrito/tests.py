from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Carrito, Usuario
from ingredientes.models import Ingredientes


class CarritoViewTests(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            email='test@example.com',
            password='testpassword',
            nombre='John',
            apellido='Doe',
            tipoUsuario='cliente',
            telefono='123456789',
            direccion='Test Address'
        )
        self.ingrediente = Ingredientes.objects.create(nombreIngrediente='Ingrediente de Prueba', precio=10.00, disponibilidad=True,
            vendedor=self.usuario)
        self.carrito = Carrito.objects.create(Id_usuario=self.usuario, Id_ingredientes=self.ingrediente, cantidad=1, total=10.00)

    def test_carrito_view_authenticated(self):

        self.client.login(email='test@example.com', password='testpassword')
        response =  self.client.get(reverse('carrito:carrito_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ingrediente de Prueba')
        self.assertQuerysetEqual(
            response.context['carrito_list'],
            ['<Carrito: Carrito de test@example.com - Producto: Ingrediente de Prueba>']
        )

    def test_carrito_view_unauthenticated(self):
        # Prueba para la vista CarritoView sin usuario autenticado
        response = self.client.get(reverse('carrito:carrito_list'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Ingrediente de Prueba')   # Ajusta esto según el contenido que esperas cuando no hay elementos en el carrito

   


