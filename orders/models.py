from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Categorias(models.Model):
    nombreCategoria = models.CharField(verbose_name="Nombre Categoría", max_length=25)

    def __str__(self):
        return f"{self.id} - {self.nombreCategoria}"

class OpcionMenu(models.Model):
    nombreOpcion = models.CharField(verbose_name="Nombre Opción", max_length=25)
    precio = models.FloatField(verbose_name="Precio Opcion")
    tamaño = models.CharField(verbose_name="Tamaño", max_length=35)
    idCategoria = models.ForeignKey(Categorias, on_delete=models.SET_NULL, null=True, blank=True)
    contador = models.IntegerField(verbose_name="Cantidad de Veces Adquirido", default=0)
    imagen = models.ImageField(upload_to='static/img', blank=True)
    top = models.IntegerField(verbose_name="Cantidad de Toppings")

    def __str__(self):
        return f"{self.nombreOpcion} - Precio: $ {self.precio} - Tamaño: {self.tamaño} - {self.idCategoria} - Rank: {self.contador} - Id: {self.id}"

class Toppings(models.Model):
    nombreTopping = models.CharField(verbose_name="Nombre del Topping", max_length=30)
    idCategoria = models.ForeignKey(Categorias, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nombreTopping} - {self.idCategoria}"

class Estado(models.Model):
    nombreEstado = models.CharField(verbose_name="Nombre Estado", max_length=25)

    def __str__(self):
        return f"{self.id} - {self.nombreEstado} "
        #return f"{self.id}"


class Orden(models.Model):
    total = models.FloatField(verbose_name="Monto Total Orden")
    fecha = models.DateTimeField(verbose_name="Fecha", default=datetime.now())
    idUSuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    estado = models.ForeignKey(Estado,  on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Orden N° {self.id} - Con Total: ${self.total} - Por: {self.idUSuario.first_name} {self.idUSuario.last_name} - En estado: {self.estado.nombreEstado}"

class DetalleOrden(models.Model):
    idOrden = models.ForeignKey(Orden, on_delete=models.SET_NULL, null=True, blank=True)
    idOpcion = models.ForeignKey(OpcionMenu, on_delete=models.SET_NULL, null=True, blank=True)
    cantidad = models.IntegerField(verbose_name="Cantidad")
    subtotal = models.FloatField(verbose_name="Subtotal")

    def __str__(self):
        return f"Id: {self.id} - {self.idOrden} - Opción: {self.idOpcion} - {self.cantidad} Unidades - ${self.subtotal}"

class DetalleOrdenTopping(models.Model):
    idDetalleOrden = models.ForeignKey(DetalleOrden, on_delete=models.SET_NULL, null=True, blank=True)
    idTopping = models.ForeignKey(Toppings, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.idDetalleOrden} - {self.idTopping}"

class CurrentOrder(models.Model):
    idUser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    idOrden = models.ForeignKey(Orden, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Orden Actual: {self.idOrden} por: {self.idUser.username}"