# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultado',
            name='aptitud',
            field=models.CharField(max_length=100, verbose_name='APTITUD:', blank=True),
        ),
        migrations.AddField(
            model_name='resultado',
            name='col_total',
            field=models.CharField(max_length=100, verbose_name='COL TOTAL:', blank=True),
        ),
        migrations.AddField(
            model_name='resultado',
            name='creatinina',
            field=models.CharField(max_length=100, verbose_name='CREATININA:', blank=True),
        ),
        migrations.AddField(
            model_name='resultado',
            name='ekg',
            field=models.CharField(max_length=100, verbose_name='EKG:', blank=True),
        ),
        migrations.AddField(
            model_name='resultado',
            name='espirometria',
            field=models.CharField(max_length=100, verbose_name='ESPIRIMETRIA:', blank=True),
        ),
        migrations.AddField(
            model_name='resultado',
            name='factor',
            field=models.CharField(max_length=100, verbose_name='FACTOR:', blank=True),
        ),
        migrations.AddField(
            model_name='resultado',
            name='glucosa',
            field=models.CharField(max_length=100, verbose_name='GLUCOSA:', blank=True),
        ),
        migrations.AddField(
            model_name='resultado',
            name='grupo_sanguineo',
            field=models.CharField(max_length=100, verbose_name='GRUPO SANGUINEO:', blank=True),
        ),
        migrations.AddField(
            model_name='resultado',
            name='hdl',
            field=models.DecimalField(null=True, verbose_name='HDL:', max_digits=8, decimal_places=2),
        ),
        migrations.AddField(
            model_name='resultado',
            name='hematocrito',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=2),
        ),
        migrations.AddField(
            model_name='resultado',
            name='hemoglobina',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=2),
        ),
        migrations.AddField(
            model_name='resultado',
            name='ldl',
            field=models.DecimalField(null=True, verbose_name='LDL:', max_digits=8, decimal_places=2),
        ),
        migrations.AddField(
            model_name='resultado',
            name='orina',
            field=models.CharField(max_length=100, verbose_name='ORINA:', blank=True),
        ),
        migrations.AddField(
            model_name='resultado',
            name='reaccion_serologicas',
            field=models.CharField(max_length=100, verbose_name='REACCION SEROLOGICAS:', blank=True),
        ),
        migrations.AddField(
            model_name='resultado',
            name='recomendaciones',
            field=models.CharField(max_length=100, verbose_name='RECOMENDACIONES:', blank=True),
        ),
        migrations.AddField(
            model_name='resultado',
            name='serie_blanca',
            field=models.CharField(max_length=100, verbose_name='SERIE BLANCA:', blank=True),
        ),
        migrations.AddField(
            model_name='resultado',
            name='serie_roja',
            field=models.CharField(max_length=100, verbose_name='SERIE ROJA:', blank=True),
        ),
        migrations.AddField(
            model_name='resultado',
            name='tgo',
            field=models.CharField(max_length=100, verbose_name='TGO:', blank=True),
        ),
        migrations.AddField(
            model_name='resultado',
            name='tgp',
            field=models.CharField(max_length=100, verbose_name='TGP:', blank=True),
        ),
        migrations.AddField(
            model_name='resultado',
            name='toxicologico',
            field=models.CharField(max_length=100, verbose_name='TOXICOLOGICO:', blank=True),
        ),
        migrations.AddField(
            model_name='resultado',
            name='trigliceridos',
            field=models.CharField(max_length=100, verbose_name='TRIGLICERIDOS:', blank=True),
        ),
        migrations.AddField(
            model_name='resultado',
            name='vldl',
            field=models.DecimalField(null=True, verbose_name='VLDL', max_digits=8, decimal_places=2),
        ),
    ]
