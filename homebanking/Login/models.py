from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    customer_DNI_id = models.CharField(null=True, blank=True, max_length=10)