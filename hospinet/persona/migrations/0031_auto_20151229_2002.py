# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0030_auto_20151229_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='antecedentequirurgico',
            name='fecha_inicio',
        ),
        migrations.AddField(
            model_name='antecedentequirurgico',
            name='fecha',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='antecedentequirurgico',
            name='fecha_fin',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
