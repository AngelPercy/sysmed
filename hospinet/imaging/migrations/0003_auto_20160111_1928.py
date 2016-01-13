# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imaging', '0002_auto_20151115_0102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudioprogramado',
            name='calidad',
        ),
        migrations.RemoveField(
            model_name='estudioprogramado',
            name='campo_pulmonar',
        ),
        migrations.RemoveField(
            model_name='estudioprogramado',
            name='con_neumoconiosis',
        ),
        migrations.RemoveField(
            model_name='estudioprogramado',
            name='conclu_radiograficas',
        ),
        migrations.RemoveField(
            model_name='estudioprogramado',
            name='hilios',
        ),
        migrations.RemoveField(
            model_name='estudioprogramado',
            name='mediastino',
        ),
        migrations.RemoveField(
            model_name='estudioprogramado',
            name='n_rx',
        ),
        migrations.RemoveField(
            model_name='estudioprogramado',
            name='normal',
        ),
        migrations.RemoveField(
            model_name='estudioprogramado',
            name='senos',
        ),
        migrations.RemoveField(
            model_name='estudioprogramado',
            name='silueta_cardiovascular',
        ),
        migrations.RemoveField(
            model_name='estudioprogramado',
            name='simbolo',
        ),
        migrations.RemoveField(
            model_name='estudioprogramado',
            name='sospecha',
        ),
    ]
