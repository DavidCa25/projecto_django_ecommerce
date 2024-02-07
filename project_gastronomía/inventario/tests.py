from django.test import TestCase
from django.urls import reverse
from inventario.models import Inventario
from ingredientes.models import Ingredientes

from usuarios.models import Usuario

class InventarioTestCase(TestCase):
    def setUp(self):

        self.usuario = Usuario.objects.create_user(
            email='testuser@example.com',
            password='testpassword',
            nombre='Test',
            apellido='User',
            tipoUsuario='cliente',  
            telefono='123456789',
            direccion='Dirección de prueba',
            imgUser=None, 
            is_active=True,
            is_staff=False
        )

  
        self.ingrediente = Ingredientes.objects.create(
            nombreIngrediente='Ingrediente de Prueba',
            descripcion='Descripción de prueba',
            precio=10.50,
            vendedor=self.usuario
        )


        self.inventario = Inventario.objects.create(
            nombreIngredienteInv=self.ingrediente,
            cantidad=50
        )

    def test_str_method(self):

        self.assertEqual(str(self.inventario), 'Ingrediente de Prueba - Cantidad: 50')

    def test_index_view(self):
 
        self.client.login(email='testuser@example.com', password='testpassword')

 
        response = self.client.get(reverse('productos:producto_views'))


        self.assertEqual(response.status_code, 200)


    def test_update_view(self):

        response = self.client.get(reverse('inventario:inventario_update', args=[self.inventario.id]))
        self.assertEqual(response.status_code, 200)


        response = self.client.post(reverse('inventario:inventario_update', args=[self.inventario.id]), {'cantidad': 30})
        self.assertEqual(response.status_code, 302)  

        
        self.inventario.refresh_from_db()
        self.assertEqual(self.inventario.cantidad, 30)