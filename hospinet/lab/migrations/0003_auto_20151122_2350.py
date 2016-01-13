# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0002_auto_20151028_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultado',
            name='factor',
            field=models.CharField(blank=True, max_length=100, verbose_name='FACTOR:', choices=[(b'+', '+'), (b'-', '-')]),
        ),
        migrations.AlterField(
            model_name='resultado',
            name='grupo_sanguineo',
            field=models.CharField(blank=True, max_length=100, verbose_name='GRUPO SANGUINEO:', choices=[(b'A', 'A'), (b'B', 'B'), (b'AB', 'AB'), (b'O', 'O')]),
        ),
        migrations.AlterField(
            model_name='resultado',
            name='hematocrito',
            field=models.DecimalField(null=True, verbose_name='HEMATOCRITO:', max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='resultado',
            name='hemoglobina',
            field=models.DecimalField(null=True, verbose_name='HEMOGLOBINA:', max_digits=8, decimal_places=2),
        ),
    ]
