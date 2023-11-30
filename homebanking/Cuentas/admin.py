from django.contrib import admin
from .models import  *
# Register your models here.
@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    list_display =('account_id','customer_id','balance','iban','tipo_cuenta_id')

@admin.register(TipoCuenta)
class TipoCuentaAdmin(admin.ModelAdmin):
    list_display =('tipo_cuenta_id','cuenta_name','moneda')