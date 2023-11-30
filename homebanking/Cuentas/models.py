from django.db import models
# Create your models here.
class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey("Clientes.cliente", on_delete=models.CASCADE)
    balance = models.IntegerField()
    iban = models.TextField()
    tipo_cuenta = models.ForeignKey("TipoCuenta", on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'cuenta'

class TipoCuenta(models.Model):
    tipo_cuenta_id = models.AutoField(primary_key=True, blank=True, null=False,)
    cuenta_name = models.TextField()
    moneda = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_cuenta'
