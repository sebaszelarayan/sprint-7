from django.db import models
from MarcaTarjeta.models import MarcaTarjeta
from Clientes.models import Cliente
# Create your models here.
class Tarjeta(models.Model):
    numero = models.AutoField(primary_key=True, blank=True, null=False)
    cvv = models.IntegerField(unique=True, blank=True, null=True)
    fecha_de_otorgamiento = models.IntegerField(blank=True, null=True)
    fecha_de_expiracion = models.IntegerField(blank=True, null=True)
    tipo_tarjeta = models.IntegerField(blank=True, null=True)
    tarjeta = models.ForeignKey(MarcaTarjeta, models.DO_NOTHING, blank=True, null=True)
    customer = models.OneToOneField(Cliente, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tarjeta'