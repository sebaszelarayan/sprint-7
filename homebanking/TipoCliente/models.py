from django.db import models

# Create your models here.
class TipoCliente(models.Model):
    tipo_id = models.AutoField(primary_key=True, blank=True, null=False)
    tipo_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_cliente'
