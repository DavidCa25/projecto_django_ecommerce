from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser


class UsuarioManager(BaseUserManager):
    def create_user(self, email, nombre, apellido, password=None, **extra_fields):
        if not email:
            raise ValueError('El campo de correo electrónico debe estar configurado.')
        email = self.normalize_email(email)
        usuario = self.model(email=email, nombre=nombre, apellido=apellido, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario
    
    def create_superuser(self, email, nombre, apellido, password=None, **extra_fields):
        usuario = self.create_user(email, nombre, apellido, password, **extra_fields)
        usuario.is_staff = True
        usuario.is_superuser = True
        usuario.save(using=self._db)
        return usuario
    
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            usuario = self.get(email=email)
            if usuario.check_password(password):
                return usuario
        except Usuario.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return self.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None
        
class Usuario(AbstractBaseUser):
    TIPO_USUARIO_CHOICES = [
        ('cliente', 'Cliente'),
        ('vendedor', 'Vendedor'),
    ]

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    tipoUsuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES, default='cliente')
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    imgUser = models.ImageField(upload_to="usuarios", null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido']

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.email