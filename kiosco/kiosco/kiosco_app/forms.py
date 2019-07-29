from django import forms
from .models import Producto, Proveedor, Ingreso, Egreso


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields= ('codigo_producto', 'nombre','descripcion', 'precio_sugerido')


class ProveedorForm(forms.ModelForm):

    class Meta:
        model= Proveedor
        fields = ('nombre_prov','cuit','direccion','telefono')

class IngresoForm(forms.ModelForm):

    class Meta:
        model = Ingreso
        fields = ('producto','proveedor','cantidad','fecha')


class EgresoForm(forms.ModelForm):
    class Meta:
        model = Egreso
        fields = ('producto', 'cantidad', 'fecha')
