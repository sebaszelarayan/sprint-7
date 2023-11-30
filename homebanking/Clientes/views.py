from django.shortcuts import render 
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.
@login_required
def ClientesView(request):
    direcciones = Direcciones.objects.all()
    suscursal = Sucursal.objects.all()
    tipo_cliente = TipoCliente.objects.all()
    cliente = Cliente
    return render(request,'cliente.html',{'direcciones':direcciones,'cliente':cliente,'sucursal':suscursal,'tipo_cliente':tipo_cliente})

