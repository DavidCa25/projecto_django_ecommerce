from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from compras.models import Compra
from carrito.models import Carrito
from django.db.models import Sum
from django.db import transaction

class CompraView(generic.ListView):
    template_name = "compras/compras_list.html"
    context_object_name = "compras_list"

    def get_queryset(self):
        return Compra.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_data'] = self.request.user
        return context
    
    

    

    



