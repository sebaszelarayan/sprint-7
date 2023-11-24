from django.contrib import admin
from .models import Tarjeta
# Register your models here.
@admin.register(Tarjeta)
class TarjetaAdmin(admin.ModelAdmin):
    list_display =('numero','cvv','fecha_de_otorgamiento','fecha_de_expiracion','tipo_tarjeta','tarjeta','customer')