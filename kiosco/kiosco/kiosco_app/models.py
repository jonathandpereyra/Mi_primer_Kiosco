# Create your models here.
from django.db import models
from django.utils import timezone


class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    codigo_producto= models.CharField(max_length=100, unique=True)
    precio_sugerido= models.DecimalField(max_digits=10, decimal_places=2)

    def guardar(self):
        self.save()

    def eliminar(self):
        self.delete()

    def __str__(self):
        return self.nombre
