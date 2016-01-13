# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0016_auto_20151028_0027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='antecedente',
            name='alcoholismo',
        ),
        migrations.RemoveField(
            model_name='antecedente',
            name='artritis',
        ),
        migrations.RemoveField(
            model_name='antecedente',
            name='cardiopatia',
        ),
        migrations.RemoveField(
            model_name='antecedente',
            name='colelitiasis',
        ),
        migrations.RemoveField(
            model_name='antecedente',
            name='colesterol',
        ),
        migrations.RemoveField(
            model_name='antecedente',
            name='colitis',
        ),
        migrations.RemoveField(
            model_name='antecedente',
            name='congenital',
        ),
        migrations.RemoveField(
            model_name='antecedente',
            name='diabetes',
        ),
        migrations.RemoveField(
            model_name='antecedente',
            name='gastritis',
        ),
        migrations.RemoveField(
            model_name='antecedente',
            name='general',
        ),
        migrations.RemoveField(
            model_name='antecedente',
            name='hepatitis',
        ),
        migrations.RemoveField(
            model_name='antecedente',
            name='hipertension',
        ),
        migrations.RemoveField(
            model_name='antecedente',
            name='hipertrigliceridemia',
        ),
        migrations.RemoveField(
            model_name='antecedente',
            name='nutricional',
        ),
        migrations.RemoveField(
            model_name='antecedente',
            name='obesidad',
        ),
        migrations.RemoveField(
            model_name='antecedente',
            name='otros',
        ),
        migrations.RemoveField(
            model_name='antecedente',
            name='rinitis',
        ),
        migrations.RemoveField(
            model_name='antecedente',
            name='sinusitis',
        ),
        migrations.RemoveField(
            model_name='antecedente',
            name='tiroides',
        ),
        migrations.RemoveField(
            model_name='antecedente',
            name='trigliceridos',
        ),
        migrations.RemoveField(
            model_name='antecedente',
            name='tuberculosis',
        ),
        migrations.AddField(
            model_name='fisico',
            name='expiracion_forzada',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='fisico',
            name='fc',
            field=models.CharField(max_length=100, verbose_name='FC:', blank=True),
        ),
        migrations.AddField(
            model_name='fisico',
            name='fr',
            field=models.CharField(max_length=100, verbose_name='FR:', blank=True),
        ),
        migrations.AddField(
            model_name='fisico',
            name='icc',
            field=models.CharField(max_length=100, verbose_name='ICC:', blank=True),
        ),
        migrations.AddField(
            model_name='fisico',
            name='imc',
            field=models.CharField(max_length=100, verbose_name='IMC:', blank=True),
        ),
        migrations.AddField(
            model_name='fisico',
            name='max_inspiracion',
            field=models.CharField(max_length=200, verbose_name='M\xe1x Inspiraci\xf3n:', blank=True),
        ),
        migrations.AddField(
            model_name='fisico',
            name='otros',
            field=models.CharField(max_length=200, verbose_name='OTROS', blank=True),
        ),
        migrations.AddField(
            model_name='fisico',
            name='pad',
            field=models.CharField(max_length=100, verbose_name='PAD:', blank=True),
        ),
        migrations.AddField(
            model_name='fisico',
            name='pas',
            field=models.CharField(max_length=100, verbose_name='PAS:', blank=True),
        ),
        migrations.AddField(
            model_name='fisico',
            name='perime_cadera',
            field=models.CharField(max_length=100, verbose_name='PER\xcdMETRO CADERA:', blank=True),
        ),
        migrations.AddField(
            model_name='fisico',
            name='perime_cintura',
            field=models.CharField(max_length=100, verbose_name='PER\xcdMETRO CINTURA:', blank=True),
        ),
        migrations.AddField(
            model_name='fisico',
            name='perime_torax',
            field=models.CharField(max_length=100, verbose_name='PER\xcdMETRO TOR\xc1XICO:', blank=True),
        ),
        migrations.AddField(
            model_name='fisico',
            name='saturacion',
            field=models.CharField(max_length=30, verbose_name='So2:', blank=True),
        ),
        migrations.AddField(
            model_name='fisico',
            name='talla',
            field=models.DecimalField(null=True, verbose_name='TALLA:', max_digits=5, decimal_places=2),
        ),
        migrations.AddField(
            model_name='fisico',
            name='temperatura',
            field=models.DecimalField(null=True, verbose_name='T\xb0 :', max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='fisico',
            name='peso',
            field=models.DecimalField(null=True, verbose_name='PESO:', max_digits=5, decimal_places=2),
        ),
    ]
