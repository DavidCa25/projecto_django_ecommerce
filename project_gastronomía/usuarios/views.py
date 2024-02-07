from django.http import HttpResponseRedirect
from django.shortcuts import render
from usuarios.models import Usuario
from django.views import generic
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from usuarios.forms import CustomAuthenticationForm, UsuarioCreationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login



class CreateView(generic.CreateView):
    model = Usuario
    template_name = "usuarios/usuarios_create.html"
    form_class = UsuarioCreationForm
    success_url = reverse_lazy("usuarios:usuarios_login")
    
    def form_valid(self, form):
        if form.cleaned_data['password1'] != form.cleaned_data['password2']:
            return self.form_invalid(form)

        response = super().form_valid(form)
        return response


class LoginView(generic.FormView):
    template_name = "usuarios/usuarios_login.html"
    form_class = CustomAuthenticationForm
    success_url = reverse_lazy("productos:producto_views")

    def form_valid(self, form):
        
        email = form.cleaned_data["username"] 
        password = form.cleaned_data["password"]
        user = authenticate(request=self.request, email=email, password=password)

        if user is not None:
            login(self.request, user)
            if user.tipoUsuario == "cliente":
                self.success_url = reverse_lazy("productos:producto_views")
            elif user.tipoUsuario == "vendedor":
                self.success_url = reverse_lazy("inventario:inventario_list")

        return HttpResponseRedirect(self.get_success_url())
        

@method_decorator(login_required, name='dispatch')
class PerfilView(generic.DetailView):
    model = Usuario
    template_name = "usuarios/usuarios_list.html"
    context_object_name = "usuarios_list"

    def get_object(self, queryset=None):
        
        if self.request.user.is_authenticated:
            return self.request.user
        else:
            
            return None
    
@method_decorator(login_required, name='dispatch')
class UpdatePerfilView(generic.UpdateView):
    model = Usuario
    template_name = "usuarios/usuarios_list.html"
    fields = ['nombre', 'apellido', 'email', 'direccion', 'telefono', 'password'] 
    success_url = reverse_lazy('usuarios:usuarios_list')


   


   


