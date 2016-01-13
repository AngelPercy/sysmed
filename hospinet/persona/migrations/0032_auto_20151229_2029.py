# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0031_auto_20151229_2002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='antecedentequirurgico',
            old_name='fecha_fin',
            new_name='procedimiento',
        ),
        migrations.RemoveField(
            model_name='antecedentequirurgico',
            name='agente',
        ),
        migrations.RemoveField(
            model_name='antecedentequirurgico',
            name='depatamento',
        ),
        migrations.RemoveField(
            model_name='antecedentequirurgico',
            name='emplea',
        ),
        migrations.RemoveField(
            model_name='antecedentequirurgico',
            name='horas_exposicion_dia',
        ),
        migrations.RemoveField(
            model_name='antecedentequirurgico',
            name='no',
        ),
        migrations.RemoveField(
            model_name='antecedentequirurgico',
            name='obs',
        ),
        migrations.RemoveField(
            model_name='antecedentequirurgico',
            name='provincia',
        ),
        migrations.RemoveField(
            model_name='antecedentequirurgico',
            name='puesto_trabajo',
        ),
        migrations.RemoveField(
            model_name='antecedentequirurgico',
            name='riesgo',
        ),
        migrations.RemoveField(
            model_name='antecedentequirurgico',
            name='rubro',
        ),
        migrations.RemoveField(
            model_name='antecedentequirurgico',
            name='si',
        ),
        migrations.RemoveField(
            model_name='antecedentequirurgico',
            name='uso_epp_dia',
        ),
    ]
