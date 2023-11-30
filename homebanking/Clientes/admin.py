from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display =('customer_id','customer_name','customer_surname','customer_DNI_id','dob','branch_id','direccion_id','tipo_cliente_id')

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display=('branch_id','branch_number','branch_name','direccion_id')

@admin.register(TipoCliente)
class TipoClienteAdmin(admin.ModelAdmin):
    list_display =('tipo_cliente_id','tipo_name')

@admin.register(Direcciones)
class DireccionesAdmin(admin.ModelAdmin):
    list_display =('direccion_id','calle','numero','ciudad','provincia','pais')