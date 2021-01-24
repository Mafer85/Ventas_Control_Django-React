from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User

class Vendedor(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    c = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.user.username

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_categoria

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.FloatField()
    descripcion = models.CharField(max_length=200)
    existencias = models.IntegerField()
    categoria = models.ForeignKey(
        Categoria, null=True, blank=True, on_delete=models.CASCADE, related_name="categorias"
    )
    vendedor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Factura(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    nit_cliente = models.CharField(max_length=20)
    fecha = timezone.now()
    total = models.FloatField()

    def unique(self):
        return self.primary_key

class detalleFactura(models.Model):
    Factura_ID = models.ForeignKey(
        Factura, on_delete = models.CASCADE, related_name='numfactura'
    )
    producto = models.ForeignKey(
        Producto, on_delete=models.CASCADE, related_name='productos'
    )
    precio = models.FloatField()
    cantidad = models.IntegerField()
    subtotal = models.FloatField()

    def unique(self):
        return self.primary_key
