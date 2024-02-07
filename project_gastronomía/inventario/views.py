from django.shortcuts import render
from django.views import generic
from inventario.models import Inventario
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
class indexView(generic.ListView):
    model = Inventario
    template_name = "inventario/inventario_list.html"
    context_object_name = "inventario_list"

    def get_queryset(self):
        return Inventario.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class UpdateView(generic.UpdateView):
    model = Inventario
    template_name = "inventario/inventario_list.html"
    fields = ['cantidad'] 
    success_url = reverse_lazy('inventario:inventario_list')
