from . import views
from django.urls import path



app_name="usuarios"
urlpatterns = [
    path('', views.LoginView.as_view(), name='usuarios_login'),
    path('perfil/<int:pk>/', views.PerfilView.as_view(), name='usuarios_list'),
    path('<int:pk>/edit/', views.UpdatePerfilView.as_view(), name='usuarios_update'),
    path('new/', views.CreateView.as_view(), name='usuarios_create'),

]