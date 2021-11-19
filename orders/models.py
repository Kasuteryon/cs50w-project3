from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categorias(models.Model):
    nombreCategoria = models.CharField(verbose_name="Nombre Categoría", max_length=25)

    def __str__(self):
        return f"{self.nombreCategoria}"

class OpcionMenu(models.Model):
    nombreOpcion = models.CharField(verbose_name="Nombre Opción", max_length=25)
    precio = models.FloatField(verbose_name="Precio Opcion")
    tamaño = models.CharField(verbose_name="Tamaño", max_length=35)
    idCategoria = models.ForeignKey(Categorias, on_delete=models.SET_NULL, null=True, blank=True)
    contador = models.IntegerField(verbose_name="Cantidad de Veces Adquirido", default=0)
    imagen = models.ImageField(upload_to='static/img', blank=True)

    def __str__(self):
        return f"{self.nombreOpcion} - {self.precio} - {self.tamaño} - {self.idCategoria} - Rank: {self.contador}"

class Toppings(models.Model):
    nombreTopping = models.CharField(verbose_name="Nombre del Topping", max_length=30)
    idCategoria = models.ForeignKey(Categorias, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nombreTopping} - {self.idCategoria}"

class Orden(models.Model):
    total = models.FloatField(verbose_name="Monto Total Orden")
    seCompleto = models.BooleanField(verbose_name="Orden Completa")
    idUSuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.total} - {self.idUSuario} - {self.seCompleto}"

class DetalleOrden(models.Model):
    idOrden = models.ForeignKey(Orden, on_delete=models.SET_NULL, null=True, blank=True)
    idOpcion = models.ForeignKey(OpcionMenu, on_delete=models.SET_NULL, null=True, blank=True)
    cantidad = models.IntegerField(verbose_name="Cantidad")
    subtotal = models.FloatField(verbose_name="Subtotal")

    def __str__(self):
        return f"{self.idOrden} - {self.idOpcion} - {self.cantidad} - {self.subtotal}"

class DetalleOrdenTopping(models.Model):
    idDetalleOrden = models.ForeignKey(DetalleOrden, on_delete=models.SET_NULL, null=True, blank=True)
    idTopping = models.ForeignKey(Toppings, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.idDetalleOrden} - {self.idTopping}"