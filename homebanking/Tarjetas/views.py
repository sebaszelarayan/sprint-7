from django.shortcuts import render

# Create your views here.

def Tarjetas(request):
    return render(request,'tarjetas.html')