from django.contrib import admin
from .models import Direcciones
# Register your models here.
@admin.register(Direcciones)
class DireccionesAdmin(admin.ModelAdmin):
    list_display =('direccion_id','calle','numero','ciudad','provincia','pais')