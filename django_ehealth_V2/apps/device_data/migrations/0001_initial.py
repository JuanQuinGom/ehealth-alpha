# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-03-09 23:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personal_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dispositivos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_registro', models.IntegerField()),
                ('id_device', models.IntegerField()),
                ('fecha_registro', models.DateField()),
                ('presion_diastolica', models.IntegerField()),
                ('presion_sistolica', models.IntegerField()),
                ('pulso_cardiaco', models.IntegerField()),
                ('temperatura', models.IntegerField()),
                ('folio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='personal_data.Datos_Personas')),
            ],
        ),
    ]
