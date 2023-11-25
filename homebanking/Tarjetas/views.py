
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Tarjeta,Cliente

# Create your views here.
@login_required
def Tarjetas(request,customer_id):
    tarjetas = Tarjeta.objects.all()
    cliente = get_object_or_404(Cliente,pk=customer_id)
    return render(request,'tarjetas.html',{'tarjetas':tarjetas,'cliente':cliente})