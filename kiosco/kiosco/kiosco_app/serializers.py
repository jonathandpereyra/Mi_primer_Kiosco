from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Producto, Proveedor, Ingreso, Egreso

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = [
            'nombre',
            'descripcion',
            'codigo_producto',
            'precio_sugerido',
        ]
class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = [
            'nombre',
            'cuit',
            'direccion',
            'telefono',
        ]

class IngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Ingreso
        fields = [
            'producto',
            'proveedor',
            'cantidad',
            'fecha'
        ]

class EgresoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Egreso
        fields = [
            'producto',
            'cantidad',
            'fecha'
        ]

class UserSerializer(serializers.ModelSerializer):
    productos = ProductoSerializer(many=True, source="producto_set")
    proveedores = ProveedorSerializer(many= True, source= "proveedor_set")
    ingresos = IngresoSerializer(many=True,source="ingreso_set")
    egresos = EgresoSerializer(many=True,source="egreso_set")
    custom_field = serializers.SerializerMethodField()

    class Meta:
        model = User
        fiels = [
            'productos',
            'proveedores',
            'ingresos',
            'egresos',
            'custom_field'
        ]
