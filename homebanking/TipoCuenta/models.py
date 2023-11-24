from django.db import models

# Create your models here.
class TipoCuenta(models.Model):
    cuenta_id = models.AutoField(primary_key=True, blank=True, null=False)
    cuenta_name = models.TextField()
    moneda = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_cuenta'
