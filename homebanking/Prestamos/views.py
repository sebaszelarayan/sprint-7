from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Prestamo

# Create your views here.

@login_required
def Prestamos(request):
    # Verificar si el usuario está autenticado
    return render(request,'prestamos.html')