from django.contrib import admin
from .models import Cliente
# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display =('customer_id','customer_name','customer_surname','customer_dni','dob','branch_id','direccion_id')