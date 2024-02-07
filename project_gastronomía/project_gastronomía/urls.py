from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include("usuarios.urls")),
    path('productos/', include("productos.urls")), 
    path('carrito/', include("carrito.urls")), 
    path('compras/', include("compras.urls")), 
    path('ingredientes/', include("ingredientes.urls")), 
    path('inventario/', include("inventario.urls")), 
    
    path('categoria/', include("categoria.urls"))
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

