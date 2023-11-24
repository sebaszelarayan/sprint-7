from django.db import models

# Create your models here.
class Movimientos(models.Model):
    movimiento = models.AutoField(primary_key=True)
    nro_cuenta = models.IntegerField()
    flag = models.TextField()
    monto = models.IntegerField()
    tipo_operacion = models.IntegerField()
    hora = models.TimeField()

    class Meta:
        managed = False
        db_table = 'movimientos'