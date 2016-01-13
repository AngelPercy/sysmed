# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0028_auto_20151208_1844'),
    ]

    operations = [
        migrations.RenameField(
            model_name='antecedente',
            old_name='abdomen_simetrico',
            new_name='abdomen_normal',
        ),
        migrations.RemoveField(
            model_name='antecedente',
            name='anormalida',
        ),
        migrations.AddField(
            model_name='antecedente',
            name='abdomen_anormal',
            field=models.BooleanField(default=False, verbose_name='ANORMALIDADES'),
        ),
    ]
