from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def Tarjetas(request):
    return render(request,'tarjetas.html')