from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm



class UsuarioCreationForm(UserCreationForm):
   

    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'email', 'password1', 'password2', 'tipoUsuario', 'telefono', 'direccion']
        

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = Usuario
        fields = ['email', 'password']
    
    