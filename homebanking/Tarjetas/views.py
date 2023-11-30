
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Tarjeta
from Clientes.models import Cliente

# Create your views here.
@login_required
def Tarjetas(request):
    tarjetas = Tarjeta.objects.all()
    cliente = Cliente
    return render(request,'tarjetas.html',{'tarjetas':tarjetas,'cliente':cliente})