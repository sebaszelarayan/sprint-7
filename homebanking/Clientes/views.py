from django.shortcuts import render

# Create your views here.
def Cliente(request):
    return render(request,'cliente.html')