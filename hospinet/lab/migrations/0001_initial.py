# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('descripcion', models.TextField()),
                ('archivo', models.FileField(upload_to=b'lab/results/%Y/%m/%d')),
                ('grupo_sanguineo', models.CharField(blank=True, max_length=100, verbose_name='GRUPO SANGUINEO:', choices=[(b'A', 'A'), (b'B', 'B'), (b'AB', 'AB'), (b'O', 'O')])),
                ('factor', models.CharField(blank=True, max_length=100, verbose_name='FACTOR:', choices=[(b'+', '+'), (b'-', '-')])),
                ('hemoglobina', models.DecimalField(null=True, verbose_name='HEMOGLOBINA:', max_digits=8, decimal_places=2)),
                ('hematocrito', models.DecimalField(null=True, verbose_name='HEMATOCRITO:', max_digits=8, decimal_places=2)),
                ('reaccion_serologicas', models.CharField(max_length=100, verbose_name='REACCION SEROLOGICAS:', blank=True)),
                ('orina', models.CharField(max_length=100, verbose_name='ORINA:', blank=True)),
                ('serie_blanca', models.CharField(max_length=100, verbose_name='SERIE BLANCA:', blank=True)),
                ('serie_roja', models.CharField(max_length=100, verbose_name='SERIE ROJA:', blank=True)),
                ('col_total', models.CharField(max_length=100, verbose_name='COL TOTAL:', blank=True)),
                ('hdl', models.DecimalField(help_text='VAL. NORMALES (35 - 55 MG %)', null=True, verbose_name='HDL:', max_digits=8, decimal_places=2)),
                ('ldl', models.DecimalField(help_text='VAL. NORMALES (< 130 MG %)', null=True, verbose_name='LDL:', max_digits=8, decimal_places=2)),
                ('vldl', models.DecimalField(null=True, verbose_name='VLDL', max_digits=8, decimal_places=2)),
                ('trigliceridos', models.CharField(help_text='VAL. NORMALES (MENOR DE 200 MG %)', max_length=100, verbose_name='TRIGLICERIDOS:', blank=True)),
                ('glucosa', models.CharField(help_text='VAL. NORMALES (70 - 110 MG % METOD)', max_length=100, verbose_name='GLUCOSA:', blank=True)),
                ('tgp', models.CharField(help_text='VAL. NORMALES HOMBRES < 41 U/LT', max_length=100, verbose_name='TGP:', blank=True)),
                ('tgo', models.CharField(help_text='VAL. NORMALES HOMBRES < 38 U/LT', max_length=100, verbose_name='TGO:', blank=True)),
                ('creatinina', models.CharField(help_text='VAL. NORMALES HOMBRES 0.7 - 1', max_length=100, verbose_name='CREATININA:', blank=True)),
                ('persona', models.ForeignKey(related_name='resultados', to='persona.Persona')),
            ],
            options={
                'permissions': (('lab', 'Permite al usuario administrar laboratorios'),),
            },
        ),
    ]
