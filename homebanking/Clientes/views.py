from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Cliente

# Create your views here.

def Clientes(request,customer_id):
    # Verificar si el usuario está autenticado
    if request.user.is_authenticated:
        cliente = get_object_or_404(Cliente,pk=customer_id)
        return render(request,'cliente.html',{'cliente':cliente})
    else:
        # Mostrar mensaje y redirigir a la página de registro o inicio de sesión
        messages.warning(request, 'Debe registrarse primero.')
        return redirect('/')
