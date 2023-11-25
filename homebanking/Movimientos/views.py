from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def Movimiento(request):
    return render(request,'movimientos.html') 