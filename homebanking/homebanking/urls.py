"""
URL configuration for homebanking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Login.views import *
<<<<<<< HEAD
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view(),name='register'),
    path('login/', LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
    path('', HomeView.as_view(),name='home'),
=======
from Movimientos.views import *
from Prestamos.views import *
from Clientes.views import *
from Cuentas.views import *
from Tarjetas.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Login,name='Login'),
    path('cliente/',Cliente,name='Cliente'),
    path('cuentas/',Cuentas,name = 'Cuentas'),
    path('prestamos/',Prestamos,name = 'Prestamos'),
    path('movimientos/',Movimiento,name = 'Movimientos'),
    path('tarjetas/',Tarjetas, name = 'tarjetas')
>>>>>>> e055a2cc45ec4b57e017123eabef0c82b12b44fd
]
