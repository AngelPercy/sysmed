# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imaging', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudioprogramado',
            name='calidad',
            field=models.CharField(max_length=100, verbose_name='CALIDAD:', blank=True),
        ),
        migrations.AddField(
            model_name='estudioprogramado',
            name='campo_pulmonar',
            field=models.CharField(max_length=200, verbose_name='CAMPO PULMONAR', blank=True),
        ),
        migrations.AddField(
            model_name='estudioprogramado',
            name='con_neumoconiosis',
            field=models.CharField(blank=True, max_length=1, choices=[(b'A', 'UNO 1/1'), (b'B', 'UNO 1/2'), (b'C', 'DOS 2/1'), (b'D', 'DOS 2/2'), (b'E', 'DOS 2/3'), (b'F', 'TRES 3/2'), (b'G', 'TRES 3/3'), (b'H', 'CUATRO A'), (b'I', 'CUATRO B'), (b'J', 'CUATRO C')]),
        ),
        migrations.AddField(
            model_name='estudioprogramado',
            name='conclu_radiograficas',
            field=models.CharField(max_length=100, verbose_name='CONCLUCIONES RADIOGRAFICAS', blank=True),
        ),
        migrations.AddField(
            model_name='estudioprogramado',
            name='hilios',
            field=models.CharField(max_length=100, verbose_name='HILIOS:', blank=True),
        ),
        migrations.AddField(
            model_name='estudioprogramado',
            name='mediastino',
            field=models.CharField(max_length=100, verbose_name='MEDIASTINO:', blank=True),
        ),
        migrations.AddField(
            model_name='estudioprogramado',
            name='n_rx',
            field=models.CharField(max_length=100, verbose_name='N\xb0 RX:', blank=True),
        ),
        migrations.AddField(
            model_name='estudioprogramado',
            name='normal',
            field=models.CharField(blank=True, max_length=1, choices=[(b'1', 'NORMAL 0/0'), (b'2', 'NORMAL CERO'), (b'3', 'SIN NEUMOCONIOSIS')]),
        ),
        migrations.AddField(
            model_name='estudioprogramado',
            name='senos',
            field=models.CharField(max_length=100, verbose_name='SENOS:', blank=True),
        ),
        migrations.AddField(
            model_name='estudioprogramado',
            name='silueta_cardiovascular',
            field=models.CharField(max_length=100, verbose_name='SILUETA CARDIOVASCULAR', blank=True),
        ),
        migrations.AddField(
            model_name='estudioprogramado',
            name='simbolo',
            field=models.CharField(max_length=100, verbose_name='SIMBOLOS:', blank=True),
        ),
        migrations.AddField(
            model_name='estudioprogramado',
            name='sospecha',
            field=models.CharField(blank=True, max_length=1, choices=[(b'4', 'SOSPECHA 1/O'), (b'5', 'SOSPECHA 1/0'), (b'6', 'IMG. RAD. EXPLOSION A POLVO')]),
        ),
    ]
