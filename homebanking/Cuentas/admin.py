from django.contrib import admin
from .models import Cuenta
# Register your models here.
@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    list_display =('account_id','customer_id','balance','iban','tipo_de_cuenta')