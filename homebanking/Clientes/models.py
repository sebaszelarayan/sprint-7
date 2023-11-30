from django.db import models

# Create your models here.
class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_DNI = models.OneToOneField("Login.CustomUser", on_delete=models.CASCADE)  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch = models.ForeignKey("Sucursal", on_delete=models.CASCADE)
    direccion = models.ForeignKey("Direcciones", on_delete=models.CASCADE)
    tipo_cliente = models.ForeignKey("TipoCliente", on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'cliente'

class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    direccion = models.ForeignKey("Direcciones", on_delete=models.CASCADE)


    class Meta:
        managed = False
        db_table = 'sucursal'

class TipoCliente(models.Model):
    tipo_cliente_id = models.AutoField(primary_key=True, blank=True, null=False)
    tipo_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_cliente'

class Direcciones(models.Model):
    direccion_id = models.AutoField(primary_key=True)
    calle = models.TextField()
    numero = models.IntegerField()
    ciudad = models.TextField()
    provincia = models.TextField()
    pais = models.TextField()

    class Meta:
        managed = False
        db_table = 'direcciones'
