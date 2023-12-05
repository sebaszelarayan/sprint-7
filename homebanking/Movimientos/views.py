from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Movimientos
# Create your views here.
@login_required
def Movimiento(request):
    movimiento=Movimientos.objects.all()
    return render(request,'movimientos.html',{'movimiento':movimiento})