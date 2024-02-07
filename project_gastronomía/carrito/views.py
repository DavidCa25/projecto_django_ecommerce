from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy, reverse
from carrito.models import Carrito
from ingredientes. models import Ingredientes
from django.db import transaction
from django.db.models import Sum
from django.contrib import messages
from compras.models import Compra




class CarritoView(generic.ListView):
    template_name = "carrito/carrito_list.html"
    context_object_name = "carrito_list"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Carrito.objects.filter(Id_usuario=self.request.user)
        else:
            return Carrito.objects.none()

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                carrito = Carrito.objects.get(Id_usuario=request.user)
            except Carrito.DoesNotExist:
                carrito = None
            except Carrito.MultipleObjectsReturned:
                Carrito.objects.filter(Id_usuario=request.user).delete()
                carrito = None

            ingredientes_seleccionados = request.POST.getlist('ingredientes')

            with transaction.atomic():
                for ingrediente_id in ingredientes_seleccionados:
                    try:
                        ingrediente = Ingredientes.objects.get(id=ingrediente_id)

                        carrito_item, created = Carrito.objects.get_or_create(Id_usuario=request.user, Id_ingredientes=ingrediente)

                        if not created:
                            carrito_item.cantidad += 1
                            carrito_item.total += ingrediente.precio
                            carrito_item.save()
                        else:
                            carrito_item.cantidad = 1
                            carrito_item.total = ingrediente.precio
                            carrito_item.save()

                        
                        carrito_item.total = ingrediente.precio * carrito_item.cantidad

                    except Ingredientes.DoesNotExist:
                        print(f"Error: El ingrediente con id {ingrediente_id} no existe.")

           
            subtotal = sum(item.total for item in Carrito.objects.filter(Id_usuario=request.user))
            total = subtotal  

            return self.get(request, *args, **kwargs)
        else:
            return redirect('usuarios:usuarios_login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        
        subtotal = sum(item.total for item in context['carrito_list'])
        total = subtotal  

        context['subtotal'] = subtotal
        context['total'] = total

        return context

    

class DeleteView(generic.DeleteView):
    model = Carrito
    success_url = reverse_lazy('carrito:carrito_list')
    
    def get(model, request, *args, **kwargs):
        return model.delete(request, *args, **kwargs)
