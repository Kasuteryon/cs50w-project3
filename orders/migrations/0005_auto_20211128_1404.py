# Generated by Django 3.2.9 on 2021-11-28 20:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_orden_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreEstado', models.CharField(max_length=25, verbose_name='Nombre Estado')),
            ],
        ),
        migrations.RemoveField(
            model_name='orden',
            name='seCompleto',
        ),
        migrations.AlterField(
            model_name='orden',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 28, 14, 4, 34, 875778), verbose_name='Fecha'),
        ),
        migrations.AddField(
            model_name='orden',
            name='estado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.estado'),
        ),
    ]
