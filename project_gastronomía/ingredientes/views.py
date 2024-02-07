from django.shortcuts import render
from ingredientes.models import Ingredientes
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib import messages



class CreateView(generic.CreateView):
    model = Ingredientes
    template_name = "ingredientes/ingredientes_agregar.html"
    fields = ['nombreIngrediente', 'descripcion', 'precio', 'disponibilidad', 'vendedor']
    success_url = reverse_lazy('ingredientes:ingredientes_agregar')
    

    
class UpdateView(generic.UpdateView):
    model = Ingredientes
    template_name = "ingredientes/ingredientes_agregar.html"
    fields = ['nombreIngrediente', 'descripcion', 'precio', 'disponibilidad', 'vendedor']
    success_url = reverse_lazy('ingredientes:ingredientes_agregar')

class DeleteView(generic.DeleteView):
    model = Ingredientes
    success_url = reverse_lazy('ingredientes:ingredientes_agregar')

    def get(model, request, *args, **kwargs):
        return model.delete(request, *args, **kwargs)