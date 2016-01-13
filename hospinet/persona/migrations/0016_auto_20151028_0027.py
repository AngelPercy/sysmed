# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0015_auto_20151027_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='antecedente',
            name='alcohol',
            field=models.CharField(blank=True, max_length=1, choices=[(b'N', 'NADA'), (b'P', 'POCO'), (b'H', 'HABITUAL'), (b'E', 'EXESIVO')]),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='artropatia',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='cirugia',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='coca',
            field=models.CharField(blank=True, max_length=1, choices=[(b'N', 'NADA'), (b'P', 'POCO'), (b'H', 'HABITUAL'), (b'E', 'EXESIVO')]),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='dm',
            field=models.BooleanField(default=False, verbose_name='DM:'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='h_col',
            field=models.BooleanField(default=False, verbose_name='H.Col:'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='h_tg',
            field=models.BooleanField(default=False, verbose_name='H.Tg:'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='hpb',
            field=models.BooleanField(default=False, verbose_name='HPB:'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='hta',
            field=models.BooleanField(default=False, verbose_name='HTA:'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='medicacion_actual',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='otros_b',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='prob_cv',
            field=models.BooleanField(default=False, verbose_name='Prob.CV:'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='problema_renal',
            field=models.BooleanField(default=False, verbose_name='PROBLEMA RENAL:'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='pt_columna',
            field=models.BooleanField(default=False, verbose_name='Pt.Columna:'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='ram',
            field=models.BooleanField(default=False, verbose_name='RAM:'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='sd_metabolico',
            field=models.BooleanField(default=False, verbose_name='Sd. Metab\xf3lico:'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='tabaco',
            field=models.CharField(blank=True, max_length=1, choices=[(b'N', 'NADA'), (b'P', 'POCO'), (b'H', 'HABITUAL'), (b'E', 'EXESIVO')]),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='asma',
            field=models.BooleanField(default=False, verbose_name='ASMA:'),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='cancer',
            field=models.BooleanField(default=False, verbose_name='C\xe1ncer:'),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='migrana',
            field=models.BooleanField(default=False, verbose_name='Migra\xf1a:'),
        ),
    ]
