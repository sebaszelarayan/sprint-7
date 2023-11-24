from django.db import models

# Create your models here.
class MarcaTarjeta(models.Model):
    tarjeta_id = models.AutoField(primary_key=True, blank=True, null=False)
    tarjeta_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'marca_tarjeta'