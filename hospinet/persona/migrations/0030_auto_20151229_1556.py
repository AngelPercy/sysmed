# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0029_auto_20151214_2322'),
    ]

    operations = [
        migrations.CreateModel(
            name='PuestoTrabajo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('puesto', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.RemoveField(
            model_name='antecedentequirurgico',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='antecedentequirurgico',
            name='procedimiento',
        ),
        migrations.AddField(
            model_name='antecedentequirurgico',
            name='agente',
            field=models.CharField(max_length=40, verbose_name='AGENTE', blank=True),
        ),
        migrations.AddField(
            model_name='antecedentequirurgico',
            name='depatamento',
            field=models.CharField(max_length=40, verbose_name='DEPARTAMENTO', blank=120),
        ),
        migrations.AddField(
            model_name='antecedentequirurgico',
            name='emplea',
            field=models.ForeignKey(verbose_name='EMPLEADOR', blank=True, to='persona.Empleador', null=True),
        ),
        migrations.AddField(
            model_name='antecedentequirurgico',
            name='fecha_fin',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='antecedentequirurgico',
            name='fecha_inicio',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='antecedentequirurgico',
            name='horas_exposicion_dia',
            field=models.CharField(max_length=40, verbose_name='HORAS DE ESPISICION / DIA', blank=True),
        ),
        migrations.AddField(
            model_name='antecedentequirurgico',
            name='no',
            field=models.BooleanField(default=False, verbose_name='NO'),
        ),
        migrations.AddField(
            model_name='antecedentequirurgico',
            name='obs',
            field=models.CharField(max_length=200, verbose_name='OBSERVACIONES', blank=True),
        ),
        migrations.AddField(
            model_name='antecedentequirurgico',
            name='provincia',
            field=models.CharField(max_length=40, verbose_name='PROVINCIA', blank=120),
        ),
        migrations.AddField(
            model_name='antecedentequirurgico',
            name='riesgo',
            field=models.CharField(blank=True, max_length=1, verbose_name='RIESGO', choices=[(b'Q', 'QUIMICO'), (b'F', 'FISICO'), (b'E', 'ERGONOMICO'), (b'O', 'OTROS')]),
        ),
        migrations.AddField(
            model_name='antecedentequirurgico',
            name='rubro',
            field=models.CharField(max_length=100, verbose_name='RUBRO', blank=True),
        ),
        migrations.AddField(
            model_name='antecedentequirurgico',
            name='si',
            field=models.BooleanField(default=False, verbose_name='SI'),
        ),
        migrations.AddField(
            model_name='antecedentequirurgico',
            name='uso_epp_dia',
            field=models.CharField(max_length=40, verbose_name='USO DE EPP % / DIA', blank=True),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='desc_m',
            field=models.CharField(max_length=200, verbose_name='DESCRIPCION', blank=True),
        ),
        migrations.AddField(
            model_name='antecedentequirurgico',
            name='puesto_trabajo',
            field=models.ForeignKey(verbose_name='PUESTO DE TRABAJO', blank=True, to='persona.PuestoTrabajo', null=True),
        ),
    ]
