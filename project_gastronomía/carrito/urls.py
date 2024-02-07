from . import views
from django.urls import path

app_name="carrito"
urlpatterns = [
    path('ver_carrito_1/', views.CarritoView.as_view(), name='carrito_list'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='carrito_delete'),
]