from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Clientes.models import Cliente
from .models import *

# Create your views here.
@login_required
def Cuentas(request):
    cuenta = Cuenta.objects.all()
    tipo_cuenta = TipoCuenta.objects.all()
    cliente = Cliente
    return render(request,'cuentas.html',{'cuenta':cuenta,'cliente':cliente ,'tipo_cuenta':tipo_cuenta  })