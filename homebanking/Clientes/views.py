from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Cliente

# Create your views here.
@login_required
def Clientes(request,customer_id):
    cliente = get_object_or_404(Cliente,pk=customer_id)
    return render(request,'cliente.html',{'cliente':cliente})

