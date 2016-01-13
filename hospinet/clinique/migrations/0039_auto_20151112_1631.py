# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinique', '0038_auto_20150623_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afeccion',
            name='nombre',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
    ]
