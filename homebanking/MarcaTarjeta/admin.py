from django.contrib import admin
from .models import MarcaTarjeta
# Register your models here.
@admin.register(MarcaTarjeta)
class MarcaTarjetaAdmin(admin.ModelAdmin):
    list_display =('tarjeta_id','tarjeta_name')