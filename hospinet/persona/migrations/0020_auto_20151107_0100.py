# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0019_auto_20151031_0202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='alcoholismo',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='alergias',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='asma',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='cancer',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='colelitiasis',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='colitis',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='congenital',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='diabetes',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='dislipidemias',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='epoc',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='general',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='hipertension',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='migrana',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='nutricional',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='obesidad',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='sindrome_coronario_agudo',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='sinusitis',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='tabaquismo',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='tiroides',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='tuberculosis',
        ),
        migrations.AddField(
            model_name='antecedentefamiliar',
            name='con_importancia',
            field=models.BooleanField(default=False, verbose_name='CON IMPORTANCIA'),
        ),
        migrations.AddField(
            model_name='antecedentefamiliar',
            name='hermano',
            field=models.CharField(max_length=200, verbose_name='HERMANO:', blank=True),
        ),
        migrations.AddField(
            model_name='antecedentefamiliar',
            name='mama',
            field=models.CharField(max_length=200, verbose_name='MAMA:', blank=True),
        ),
        migrations.AddField(
            model_name='antecedentefamiliar',
            name='n_hijos',
            field=models.CharField(max_length=100, verbose_name='N\xb0 DE HIJOS:', blank=True),
        ),
        migrations.AddField(
            model_name='antecedentefamiliar',
            name='papa',
            field=models.CharField(max_length=200, verbose_name='PAPA:', blank=True),
        ),
        migrations.AddField(
            model_name='antecedentefamiliar',
            name='sin_importancia',
            field=models.BooleanField(default=False, verbose_name='SIN IMPORTANCIA'),
        ),
        migrations.AddField(
            model_name='antecedentefamiliar',
            name='vivos',
            field=models.BooleanField(default=False),
        ),
    ]
