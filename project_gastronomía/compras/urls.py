from . import views
from django.urls import path

app_name="compras"
urlpatterns = [
    path('comprar/', views.CompraView.as_view(), name='compras_list')
]