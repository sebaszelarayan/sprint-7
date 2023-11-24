from django.contrib import admin
from .models import TipoCliente
# Register your models here.
@admin.register(TipoCliente)
class TipoClienteAdmin(admin.ModelAdmin):
    list_display =('tipo_id','tipo_name')