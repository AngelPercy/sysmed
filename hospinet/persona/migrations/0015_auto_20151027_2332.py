# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0014_auto_20151027_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='establecimiento',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='fecha_examen',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='persona',
            name='proyecto',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='tipo_identificacion',
            field=models.CharField(blank=True, max_length=1, choices=[(b'R', 'Documento de Identidad'), (b'L', 'Licencia'), (b'P', 'Pasaporte'), (b'T', 'Tarjeta de Identidad'), (b'N', 'Ninguno')]),
        ),
    ]
