# Generated by Django 3.1.6 on 2021-02-14 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yellow_data', '0002_auto_20210214_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos_amarillo',
            name='tipo_sangre',
            field=models.CharField(choices=[('A-', 'A-'), ('A+', 'A+'), ('B-', 'B-'), ('B+', 'B+'), ('AB-', 'AB-'), ('AB+', 'AB+'), ('O-', 'O-'), ('O+', 'O+')], default='O+', max_length=5),
        ),
    ]