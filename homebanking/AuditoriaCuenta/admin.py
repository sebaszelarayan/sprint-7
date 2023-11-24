from django.contrib import admin
from .models import AuditoriaCuenta
# Register your models here.
@admin.register(AuditoriaCuenta)
class AuditoriaCuentaAdmin(admin.ModelAdmin):
    list_display =('old_id','new_id','old_balance','new_balance','old_iban','new_iban','old_type','new_type','user_action','created_at')