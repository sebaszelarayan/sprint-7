from django.shortcuts import render

# Create your views here.

def Prestamos(request):
    return render(request,'prestamos.html')