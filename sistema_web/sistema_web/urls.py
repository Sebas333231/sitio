"""
URL configuration for sistema_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from principal.views import pagina, SignUpView, bienvenidos, detalleVenta, nuevaVenta, eliminar, editarventa
from principal.views import bienvenidos_dos, editarVisita, eliminar_visita, nuevaVisita, cards
urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('pagina', pagina, name="pagina"),
    path('hola', bienvenidos, name='hola'),
    path('informacion', cards, name='informacion'),
    path('visita', bienvenidos_dos, name='visita'),
    path('detalle_venta/<int:id>', detalleVenta),
    path('nueva_venta', nuevaVenta),
    path('editar_venta/<int:id>', editarventa),
    path('eliminar/<int:id>', eliminar),
    path('editar_visita/<int:id>', editarVisita),
    path('eliminar_visita/<int:id>', eliminar_visita),
    path('nueva_visita', nuevaVisita)
]
