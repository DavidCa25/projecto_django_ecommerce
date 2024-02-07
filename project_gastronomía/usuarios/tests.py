from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class UsuarioTests(TestCase):
    def setUp(self):
        self.user_data = {
            'nombre': 'John',
            'apellido': 'Doe',
            'email': 'john@example.com',
            'tipoUsuario': 'cliente',
            'telefono': '123456789',
            'direccion': '123 Main St',
        }
        self.password = 'secretpassword'

    def test_create_user(self):
        response = self.client.post(reverse('usuarios:usuarios_create'), {
            'nombre': self.user_data['nombre'],
            'apellido': self.user_data['apellido'],
            'email': self.user_data['email'],
            'tipoUsuario': self.user_data['tipoUsuario'],
            'telefono': self.user_data['telefono'],
            'direccion': self.user_data['direccion'],
            'password1': self.password,
            'password2': self.password,
        })

        # Verify that the creation was successful and redirected to the correct page
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('usuarios:usuarios_login'))

        # Verify that the user was created in the database
        user = get_user_model().objects.get(email=self.user_data['email'])
        self.assertEqual(user.nombre, self.user_data['nombre'])
        self.assertEqual(user.apellido, self.user_data['apellido'])
        self.assertEqual(user.tipoUsuario, self.user_data['tipoUsuario'])
        self.assertEqual(user.telefono, self.user_data['telefono'])
        self.assertEqual(user.direccion, self.user_data['direccion'])
        self.assertTrue(user.check_password(self.password))

    def test_login_user(self):
        user = get_user_model().objects.create_user(
            email='login@example.com',
            password=self.password,
            nombre='LoginName',
            apellido='LoginLastName',
        )

        response = self.client.post(reverse('usuarios:usuarios_login'), {
            'username': 'login@example.com',
            'password': self.password,
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('productos:producto_views'))
