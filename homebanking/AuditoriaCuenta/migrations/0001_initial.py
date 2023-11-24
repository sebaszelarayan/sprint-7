# Generated by Django 4.2.7 on 2023-11-23 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuditoriaCuenta',
            fields=[
                ('old_id', models.AutoField(primary_key=True, serialize=False)),
                ('new_id', models.IntegerField(blank=True, null=True)),
                ('old_balance', models.IntegerField(blank=True, null=True)),
                ('new_balance', models.IntegerField(blank=True, null=True)),
                ('old_iban', models.TextField(blank=True, null=True)),
                ('new_iban', models.TextField(blank=True, null=True)),
                ('old_type', models.IntegerField(blank=True, null=True)),
                ('new_type', models.IntegerField(blank=True, null=True)),
                ('user_action', models.IntegerField(blank=True, null=True)),
                ('created_at', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'auditoria_cuenta',
                'managed': False,
            },
        ),
    ]