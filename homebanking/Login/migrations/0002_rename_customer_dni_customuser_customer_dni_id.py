# Generated by Django 4.2.7 on 2023-11-28 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='customer_DNI',
            new_name='customer_DNI_id',
        ),
    ]
