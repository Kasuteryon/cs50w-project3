from django.contrib import admin
from .models import Categorias, Estado, Toppings, OpcionMenu, Orden, DetalleOrden 

# Register your models here.
admin.site.register(Categorias)
admin.site.register(Toppings)
admin.site.register(OpcionMenu)
admin.site.register(Orden)
admin.site.register(DetalleOrden)
admin.site.register(Estado)