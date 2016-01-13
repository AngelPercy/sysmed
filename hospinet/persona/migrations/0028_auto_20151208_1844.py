# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0027_auto_20151125_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antecedente',
            name='columna_vert_normal',
            field=models.BooleanField(default=False, verbose_name='COLUMNA VERTEBRAL NORMAL'),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='desc_n',
            field=models.CharField(max_length=200, verbose_name='DESCRIPCION', blank=True),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='torax_ectoscopia_normal',
            field=models.BooleanField(default=False, verbose_name=b'ECTOSCOPIA NORMAL'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='mostrar_en_cardex',
            field=models.BooleanField(default=False, verbose_name='Realizar Seguimiento'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='rtn',
            field=models.CharField(help_text='Deje en Blanco NO registre...!', max_length=200, null=True, verbose_name='Interfase', blank=True),
        ),
    ]
