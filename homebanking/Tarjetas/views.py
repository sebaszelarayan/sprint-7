
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Tarjeta,Cliente

# Create your views here.
@login_required
def Tarjetas(request,customer_id):
    # Verificar si el usuario está autenticado
    if request.user.is_authenticated:
        tarjetas = Tarjeta.objects.all()
        cliente = get_object_or_404(Cliente,pk=customer_id)
        return render(request,'tarjetas.html',{'tarjetas':tarjetas,'cliente':cliente})
    else:
        # Mostrar mensaje y redirigir a la página de registro o inicio de sesión
        messages.warning(request, 'Debe registrarse primero.')
        return redirect('/')