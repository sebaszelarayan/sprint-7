from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from Clientes.models import Cliente

# Create your views here.

@login_required
def Prestamos(request):
    prestamos = Prestamo.objects.all()
    cliente = Cliente
    return render(request,'prestamos.html',{'prestamos':prestamos,'cliente':cliente})