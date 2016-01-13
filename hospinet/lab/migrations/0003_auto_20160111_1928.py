# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0002_auto_20151028_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultado',
            name='aptitud',
        ),
        migrations.RemoveField(
            model_name='resultado',
            name='col_total',
        ),
        migrations.RemoveField(
            model_name='resultado',
            name='creatinina',
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
            name='factor',
        ),
        migrations.RemoveField(
            model_name='resultado',
            name='glucosa',
        ),
        migrations.RemoveField(
            model_name='resultado',
            name='grupo_sanguineo',
        ),
        migrations.RemoveField(
            model_name='resultado',
            name='hdl',
        ),
        migrations.RemoveField(
            model_name='resultado',
            name='hematocrito',
        ),
        migrations.RemoveField(
            model_name='resultado',
            name='hemoglobina',
        ),
        migrations.RemoveField(
            model_name='resultado',
            name='ldl',
        ),
        migrations.RemoveField(
            model_name='resultado',
            name='orina',
        ),
        migrations.RemoveField(
            model_name='resultado',
            name='reaccion_serologicas',
        ),
        migrations.RemoveField(
            model_name='resultado',
            name='recomendaciones',
        ),
        migrations.RemoveField(
            model_name='resultado',
            name='serie_blanca',
        ),
        migrations.RemoveField(
            model_name='resultado',
            name='serie_roja',
        ),
        migrations.RemoveField(
            model_name='resultado',
            name='tgo',
        ),
        migrations.RemoveField(
            model_name='resultado',
            name='tgp',
        ),
        migrations.RemoveField(
            model_name='resultado',
            name='toxicologico',
        ),
        migrations.RemoveField(
            model_name='resultado',
            name='trigliceridos',
        ),
        migrations.RemoveField(
            model_name='resultado',
            name='vldl',
        ),
    ]
