# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-21 02:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('preg_historial', '0002_auto_20200121_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amarilla',
            name='folio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='personal_data.Person'),
        ),
        migrations.AlterField(
            model_name='consultas',
            name='folio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='personal_data.Person'),
        ),
    ]
