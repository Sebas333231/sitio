from django.contrib import admin

# Register your models here.

from ventas.models import VentasAptos, Visita, comentarios

admin.site.register(VentasAptos)
admin.site.register(Visita)
admin.site.register(comentarios)