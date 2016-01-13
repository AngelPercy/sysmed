# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0003_auto_20151122_2350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultado',
            name='aptitud',
        ),
        migrations.RemoveField(
            model_name='resultado',
            name='ekg',
        ),
        migrations.RemoveField(
            model_name='resultado',
            name='espirometria',
        ),
        migrations.RemoveField(
            model_name='resultado',
            name='recomendaciones',
        ),
        migrations.RemoveField(
            model_name='resultado',
            name='toxicologico',
        ),
        migrations.AlterField(
            model_name='resultado',
            name='creatinina',
            field=models.CharField(help_text='VAL. NORMALES HOMBRES 0.7 - 1', max_length=100, verbose_name='CREATININA:', blank=True),
        ),
        migrations.AlterField(
            model_name='resultado',
            name='glucosa',
            field=models.CharField(help_text='VAL. NORMALES (70 - 110 MG % METOD)', max_length=100, verbose_name='GLUCOSA:', blank=True),
        ),
        migrations.AlterField(
            model_name='resultado',
            name='hdl',
            field=models.DecimalField(help_text='VAL. NORMALES (35 - 55 MG %)', null=True, verbose_name='HDL:', max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='resultado',
            name='ldl',
            field=models.DecimalField(help_text='VAL. NORMALES (< 130 MG %)', null=True, verbose_name='LDL:', max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='resultado',
            name='tgo',
            field=models.CharField(help_text='VAL. NORMALES HOMBRES < 38 U/LT', max_length=100, verbose_name='TGO:', blank=True),
        ),
        migrations.AlterField(
            model_name='resultado',
            name='tgp',
            field=models.CharField(help_text='VAL. NORMALES HOMBRES < 41 U/LT', max_length=100, verbose_name='TGP:', blank=True),
        ),
        migrations.AlterField(
            model_name='resultado',
            name='trigliceridos',
            field=models.CharField(help_text='VAL. NORMALES (MENOR DE 200 MG %)', max_length=100, verbose_name='TRIGLICERIDOS:', blank=True),
        ),
    ]
