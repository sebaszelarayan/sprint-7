from django.contrib import admin
from .models import TipoCuenta
# Register your models here.
@admin.register(TipoCuenta)
class TipoCuentaAdmin(admin.ModelAdmin):
    list_display =('cuenta_id','cuenta_name','moneda')