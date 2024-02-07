from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy, reverse
from productos.models import Producto
from categoria.models import Categoria

class indexView(generic.ListView):
    template_name = "productos/producto_views.html"
    context_object_name = "producto_views"

    def get_queryset(self):
        return Producto.objects.all()
    
class indexViewCatalogo(generic.ListView):
    template_name = "productos/producto_viewsCatalogo.html"
    context_object_name = "producto_viewsCatalogo"

    def get_queryset(self):
        queryset = Producto.objects.all()

        region = self.request.GET.get('region')
        if region:
            queryset = Producto.objects.filter_by_region(region)

        categoria_sabor = self.request.GET.get('categoria_sabor')
        if categoria_sabor:
            queryset = Producto.objects.filter_by_categoria_sabor(categoria_sabor)

        categoria_dieta = self.request.GET.get('categoria_dieta')
        if categoria_dieta:
            queryset = Producto.objects.filter_by_categoria_dieta(categoria_dieta)

        return queryset
    

class detailView(generic.DetailView):
    model = Producto
    template_name = "productos/producto_detail.html"

    

    

    