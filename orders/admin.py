from django.contrib import admin
from .models import Categorias, CurrentOrder, DetalleOrdenTopping, Estado, Toppings, OpcionMenu, Orden, DetalleOrden 

admin.site.site_header = "Administrador Pizza"
admin.site.site_title = "Administrar"
admin.site.index_title = "Admin Pizza"

# Register your models here.
admin.site.register(Categorias)
admin.site.register(Toppings)
admin.site.register(OpcionMenu)
admin.site.register(Orden)
admin.site.register(DetalleOrden)
admin.site.register(Estado)
admin.site.register(DetalleOrdenTopping)
admin.site.register(CurrentOrder)