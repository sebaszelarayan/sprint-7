from django.contrib import admin
from .models import Empleado
# Register your models here.
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display =('employee_id','employee_name','employee_surname','employee_hire_date','employee_dni','branch_id','direccion_id')