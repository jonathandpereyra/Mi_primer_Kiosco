from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils import timezone

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.views.generic import FormView
from django.views.generic import ListView
from .forms import ProductoForm, ProveedorForm, IngresoForm, EgresoForm
from .models import Producto, Proveedor, Ingreso, Egreso
from .serializers import ProductoSerializer, UserSerializer, ProveedorSerializer, IngresoSerializer, EgresoSerializer


#PRODUCTO

class ProductoListView(ListView):
    model = Producto
    template_name = "kiosco/producto_list.html"

    def get_queryset(self):
        queryset = super(ProductoListView, self).get_queryset()
        queryset = queryset.order_by("-id")
        return queryset

class ProductoFormView(FormView):
    form_class = ProductoForm
    success_url = reverse_lazy('productos_list')
    template_name = "kiosco_app/producto_new.html"

    def form_valid(self, form):
        producto = form.save(commit=False)
        producto.save()
        return super(ProductoFormView, self).form_valid(form)

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer






#PROVEEDOR

class ProveedorListView(ListView):
    model = Proveedor
    template_name = "kiosco_app/proveedores_list.html"

    def get_queryset(self):
        queryset = super(ProveedorListView, self).get_queryset()
        queryset = queryset.order_by("-id")
        return queryset

class ProveedorFormView(FormView):
    form_class = ProveedorForm
    success_url = reverse_lazy('proveedores_list')
    template_name = 'kiosco_app/proveedor_new.html'

    def form_valid(self, form):
        proveedor = form.save(commit=False)
        proveedor.save()
        return super(ProveedorFormView, self).form_valid(form)

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer





#USUARIO

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().prefetch_related(
        "producto_set",
        "proveedor_set",
        "ingreso_set",
        "egreso_set"
    )
    serializer_class = UserSerializer





#INGRESO

class IngresoListView(ListView):
    model = Ingreso
    template_name = "kiosco_app/ingreso.html"

    def get_queryset(self):
        queryset = super(IngresoListView, self).get_queryset()
        queryset = queryset.order_by("-id")
        return queryset

class IngresoFormView(FormView):
    form_class = IngresoForm

    success_url = reverse_lazy('ingresos')
    template_name = "kiosco_app/ingreso_edit.html"

    def form_valid(self, form):
        ingresar = form.save(commit=False)
        ingresar.save()
        return super(IngresoFormView, self).form_valid(form)

class IngresoViewSet(viewsets.ModelViewSet):
    queryset = Ingreso.objects.all()
    serializer_class = IngresoSerializer





#EGRESO

class EgresoListView(ListView):
    model = Egreso
    template_name = "kiosco_app/egreso.html"

    def get_queryset(self):
        queryset = super(EgresoListView, self).get_queryset()
        queryset = queryset.order_by("-id")
        return queryset

class EgresoFormView(FormView):
    form_class = EgresoForm

    success_url = reverse_lazy('egresos')
    template_name = "kiosco_app/egreso_edit.html"

    def form_valid(self, form):
        egresar = form.save(commit=False)
        '''
        
        if Ingreso.cantidad >= Egreso.cantidad:
            Ingreso.cantidad = Ingreso.cantidad - Egreso.cantidad
            egresar.save()
        else:
            print("El stock es menor a la cantidad que desea sacar. Hay " + Ingreso.cantidad)
        '''
        egresar.save()
        return super(EgresoFormView, self).form_valid(form)

class EgresoViewSet(viewsets.ModelViewSet):
    queryset = Egreso.objects.all()
    serializer_class = EgresoSerializer







egreso_nuevo= login_required(EgresoFormView.as_view(), login_url="/admin/login")
egresos = EgresoListView.as_view()


ingreso_nuevo= login_required(IngresoFormView.as_view(), login_url="/admin/login")
ingresos = IngresoListView.as_view()


proveedor_new = login_required(ProveedorFormView.as_view(), login_url="/admin/login")
proveedores = ProveedorListView.as_view()



producto_new= login_required(ProductoFormView.as_view(), login_url="/admin/login")
productos = ProductoListView.as_view()

