# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0017_auto_20151028_0136'),
    ]

    operations = [
        migrations.AddField(
            model_name='antecedente',
            name='biologico',
            field=models.BooleanField(default=False, verbose_name='BIOLOGICO'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='cancerigeno',
            field=models.BooleanField(default=False, verbose_name='CANCERIGENO'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='carga',
            field=models.BooleanField(default=False, verbose_name='CARGAS'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='metales',
            field=models.BooleanField(default=False, verbose_name='MENTALES'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='movimiento',
            field=models.BooleanField(default=False, verbose_name='MOVIMIENTO'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='mutagenico',
            field=models.BooleanField(default=False, verbose_name='MUTAGENICOS'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='otros_a',
            field=models.BooleanField(default=False, verbose_name='OTROS'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='pesados',
            field=models.BooleanField(default=False, verbose_name='PESADOS'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='polvo',
            field=models.BooleanField(default=False, verbose_name='POLVO'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='postula',
            field=models.CharField(max_length=200, verbose_name='PUESTO AL QUE POSTULA:', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='postura',
            field=models.BooleanField(default=False, verbose_name='POSTURA'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='repetitivo',
            field=models.BooleanField(default=False, verbose_name='REPETITIVO'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='ruido',
            field=models.BooleanField(default=False, verbose_name='RUIDO'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='segmentaria',
            field=models.BooleanField(default=False, verbose_name='SEGMENTARIA'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='solvente',
            field=models.BooleanField(default=False, verbose_name='SOLVENTE'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='temperatura',
            field=models.BooleanField(default=False, verbose_name='TEMPERATURA'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='turno_noche',
            field=models.BooleanField(default=False, verbose_name='TURNOS NOCHE'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='vibracion',
            field=models.BooleanField(default=False, verbose_name='VIBRACION'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='vibracion_total',
            field=models.BooleanField(default=False, verbose_name='VIBRACION TOTAL'),
        ),
    ]
