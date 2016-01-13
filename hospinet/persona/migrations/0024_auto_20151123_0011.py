# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0023_auto_20151122_2350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estilovida',
            name='archivo',
        ),
        migrations.AddField(
            model_name='persona',
            name='duplicado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='persona',
            name='mostrar_en_cardex',
            field=models.BooleanField(default=False),
        ),
    ]
