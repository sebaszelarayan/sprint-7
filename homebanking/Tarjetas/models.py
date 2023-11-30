from django.db import models

# Create your models here.
class Tarjeta(models.Model):
    numero = models.AutoField(primary_key=True, blank=True, null=False)
    cvv = models.IntegerField(unique=True, blank=True, null=True)
    fecha_de_otorgamiento = models.IntegerField(blank=True, null=True)
    fecha_de_expiracion = models.IntegerField(blank=True, null=True)
    tipo_tarjeta = models.IntegerField(blank=True, null=True)
    tarjeta = models.ForeignKey("MarcaTarjeta", on_delete=models.CASCADE)
    customer = models.ForeignKey("Clientes.cliente", on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'tarjeta'

class MarcaTarjeta(models.Model):
    tarjeta_id = models.AutoField(primary_key=True, blank=True, null=False)
    tarjeta_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'marca_tarjeta'