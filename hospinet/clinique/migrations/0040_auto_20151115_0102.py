# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinique', '0039_auto_20151112_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afeccion',
            name='nombre',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
