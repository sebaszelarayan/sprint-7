from django.contrib import admin
from .models import Prestamo
# Register your models here.
@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display =('loan_id','loan_type','loan_date','loan_total','customer_id')