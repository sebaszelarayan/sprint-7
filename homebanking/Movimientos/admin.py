from django.contrib import admin
from .models import Movimientos
# Register your models here.
@admin.register(Movimientos)
class MovimientoAdmin(admin.ModelAdmin):
    list_display =('movimiento','nro_cuenta','flag','monto','tipo_operacion','hora')