from . import views
from django.urls import path



app_name="inventario"
urlpatterns = [
    path('', views.indexView.as_view(), name='inventario_list'),
    path('<int:pk>', views.UpdateView.as_view(), name='inventario_update'),
]