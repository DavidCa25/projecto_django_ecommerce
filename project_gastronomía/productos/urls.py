from . import views
from django.urls import path

app_name="productos"
urlpatterns = [
    path('', views.indexView.as_view(), name='producto_views'),
    path('catalogo/', views.indexViewCatalogo.as_view(), name='producto_viewsCatalogo'),
    path('<int:pk>/', views.detailView.as_view(), name='producto_detail'),
]