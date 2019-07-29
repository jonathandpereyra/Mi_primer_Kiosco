# Create your models here.
from django.db import models
from django.utils import timezone

#Aqui estan todos los campos que se agregan y sus condiciones

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
        return f"{self.nombre}"


#Nombre, CUIT unico por proveedor, Direccion, telefono
class Proveedor(models.Model):
    nombre_prov = models.CharField(max_length=30)
    cuit = models.CharField(max_length=20, unique=True)
    direccion =  models.TextField(max_length=50)
    telefono =  models.CharField(max_length=20, unique=True)

    def guardar(self):
        self.save()

    def eliminar(self):
        self.delete()

    def __str__(self):
        return self.nombre_prov


#Producto relacionado, la cantidad de items que ingresan, la fecha y el proveedor
class Ingreso(models.Model):
    producto = models.ForeignKey('kiosco_app.Producto', on_delete= models.CASCADE)
    cantidad = models.PositiveIntegerField(max_length=4)
    fecha = models.DateTimeField(default=timezone.now)
    proveedor = models.ForeignKey('kiosco_app.Proveedor', on_delete= models.CASCADE)

    def guardar(self):
        self.save()

    def __str__(self):
        return f"Producto: {self.producto.__str__()}, Proveedor: {self.proveedor.__str__()}, Cantidad:{self.cantidad}"




class Egreso(models.Model):
    producto = models.ForeignKey('kiosco_app.Producto', on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    cantidad = models.PositiveIntegerField(max_length=4)

    def guardar(self):
        self.save()

    def __str__(self):
        return f"Producto: {self.producto.__str__()}, Cantidad:{self.cantidad}"

