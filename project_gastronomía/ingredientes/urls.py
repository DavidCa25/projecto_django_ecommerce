from . import views
from django.urls import path



app_name="ingredientes"
urlpatterns = [
    path('', views.CreateView.as_view(), name='ingredientes_agregar'),
    path('<int:pk>/edit/', views.UpdateView.as_view(), name='ingredientes_update'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='ingredientes_delete'),
]