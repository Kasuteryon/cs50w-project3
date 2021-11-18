from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categorias(models.Model):
    nombreCategoria = models.CharField(verbose_name="Nombre Categoría", max_length=25)

    def __str__(self) -> str:
        return super().__str__()

class OpcionMenu(models.Model):
    nombreOpcion = models.CharField(verbose_name="Nombre Opción", max_length=25)
    precio = models.FloatField(verbose_name="Precio Opcion")
    tamaño = models.CharField(verbose_name="Tamaño", max_length=35)
    idCategoria = models.ForeignKey(Categorias, on_delete=models.SET_NULL, null=True, blank=True)

class Toppings(models.Model):
    nombreTopping = models.CharField(verbose_name="Nombre del Topping", max_length=30)
    idCategoria = models.ForeignKey(Categorias, on_delete=models.SET_NULL, null=True, blank=True)

class Orden(models.Model):
    total = models.FloatField(verbose_name="Monto Total Orden")
    seCompleto = models.BooleanField(verbose_name="Orden Completa")
    idUSuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


class DetalleOrden(models.Model):
    idOrden = models.ForeignKey(Orden, on_delete=models.SET_NULL, null=True, blank=True)
    idOpcion = models.ForeignKey(OpcionMenu, on_delete=models.SET_NULL, null=True, blank=True)
    cantidad = models.IntegerField(verbose_name="Cantidad")
    subtotal = models.FloatField(verbose_name="Subtotal")

class DetalleOrdenTopping(models.Model):
    idDetalleOrden = models.ForeignKey(DetalleOrden, on_delete=models.SET_NULL, null=True, blank=True)
    idTopping = models.ForeignKey(Toppings, on_delete=models.SET_NULL, null=True, blank=True)
