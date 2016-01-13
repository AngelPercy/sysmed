# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0020_auto_20151107_0100'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluacionAudiometrica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_examen', models.DateField(default=datetime.date.today, verbose_name='FECHA DE EXAMEN:')),
                ('empresa', models.CharField(max_length=200, verbose_name='EMPRESA:')),
                ('ocupacion', models.CharField(max_length=200, verbose_name='OCUPACION:')),
                ('anos_trabajo', models.CharField(max_length=200, verbose_name='A\xd1OS DE TRABAJO:')),
                ('tiempo_exposicion', models.CharField(max_length=200, verbose_name='TIEMPO DE EXPOSICION A RUIDO (8 HR):')),
                ('apresiacion_ruido', models.CharField(blank=True, max_length=1, verbose_name='APRECIACION DEL RUIDO:', choices=[(b'I', 'MUY INTENSO'), (b'M', 'MODERADO'), (b'O', 'NO MOLESTO')])),
                ('audiometria_ante', models.CharField(max_length=200, verbose_name='AUDIOMETRIA ANTERIOR:')),
                ('resul_audiomet', models.CharField(max_length=200, verbose_name='RESULTADOS DE AUDIOMETRIA:')),
                ('antecedentes', models.CharField(max_length=200, verbose_name='ANTECEDENTES:')),
                ('med_ototoxicos', models.BooleanField(default=True, verbose_name='MEDICINA OTOTOXICOS:')),
                ('meningitis', models.BooleanField(default=True, verbose_name='MENINGITIS:')),
                ('sarampion', models.BooleanField(default=True, verbose_name='SARAMPION')),
                ('parotiditis', models.BooleanField(default=True, verbose_name='PAROTIDITIS:')),
                ('buceo', models.BooleanField(default=True, verbose_name='BUCEO:')),
                ('exp_quimico', models.BooleanField(default=True, verbose_name='EXP. QUIMICO:')),
                ('discotecas', models.BooleanField(default=True, verbose_name='DISCOTECAS:')),
                ('trauma_acustico', models.BooleanField(default=True, verbose_name='TRAUMA ACUSTICO:')),
                ('expos_laboral_ruido', models.BooleanField(default=True, verbose_name='EXPOS. LABORAL AL RUIDO:')),
                ('tec', models.BooleanField(default=True, verbose_name='TEC:')),
                ('armas_fuego', models.BooleanField(default=True, verbose_name='USO DE ARMAS DE FUEGO:')),
                ('audifonos', models.BooleanField(default=True, verbose_name='AUDIFONOS:')),
                ('tapones', models.CharField(blank=True, max_length=1, verbose_name='TAPONES:', choices=[(b'A', 'A VECES'), (b'B', 'SIEMPRE'), (b'C', 'NUNCA')])),
                ('orejeras', models.CharField(blank=True, max_length=1, verbose_name='OREJERAS:', choices=[(b'A', 'A VECES'), (b'B', 'SIEMPRE'), (b'C', 'NUNCA')])),
                ('algodones', models.CharField(blank=True, max_length=1, verbose_name='ALGODONES:', choices=[(b'A', 'A VECES'), (b'B', 'SIEMPRE'), (b'C', 'NUNCA')])),
                ('sistomatologia', models.CharField(max_length=200)),
                ('viaje_reciente', models.BooleanField(default=True, verbose_name='VIAJE RECIENTE < 6 HORAS:')),
                ('exp_recien_ruid18', models.BooleanField(default=True, verbose_name='EXPOSICION RECIENTE A RUIDOS (18 HORAS)')),
                ('acutenos', models.BooleanField(default=True, verbose_name='ACUTENOS:')),
                ('hipoacusia', models.BooleanField(default=True, verbose_name='HIPOACUSIA:')),
                ('otalgia', models.BooleanField(default=True, verbose_name='OTALGIA:')),
                ('enf_tra_respiratorio', models.BooleanField(default=True, verbose_name='ENF. DEL TRACTO RESPIRATORIO ACTUAL:')),
                ('secresion_otica', models.BooleanField(default=True, verbose_name='SECRECION OTICA')),
                ('vertigo', models.BooleanField(default=True, verbose_name='VERTIGO:')),
                ('garganta_normal', models.BooleanField(default=False, verbose_name='GARGANTA NORMAL')),
                ('garganta_anormal', models.BooleanField(default=False, verbose_name='GARGANTA ANORMAL')),
                ('oido_normal', models.BooleanField(default=False, verbose_name='OIDO NORMAL')),
                ('oido_anormal', models.BooleanField(default=False, verbose_name='OIDO ANORMAL')),
                ('otoscopia_od', models.BooleanField(default=False, verbose_name='OTOSCOPIA O.D.:')),
                ('otoscopia_oi', models.BooleanField(default=False, verbose_name='OTOSCOPIA O.I.:')),
                ('diapaz_od_250hz', models.BooleanField(default=False, verbose_name='DIAPAZONES OIDO DERECHO 250 Hz:')),
                ('diapaz_od_500hz', models.BooleanField(default=False, verbose_name='DIAPAZONES OIDO DERECHO 500 Hz')),
                ('diapaz_od_1000hz', models.BooleanField(default=False, verbose_name='DIAPAZONES OIDO DERECHO 1000 Hz')),
                ('diapaz_oi_250hz', models.BooleanField(default=False, verbose_name='DIAPAZONES OIDO IZQUIERDO 250 Hz')),
                ('diapaz_oi_500hz', models.BooleanField(default=False, verbose_name='DIAPAZONES OIDO IZQUIERDO 500 Hz')),
                ('diapaz_oi_1000hz', models.BooleanField(default=False, verbose_name='DIAPAZONES OIDO IZQUIERDO 1000 Hz')),
                ('logoaudi_der_umbral', models.BooleanField(default=False, verbose_name='LOGOAUDIOMETRIA DERECHO')),
                ('logoaudi_der_discrim', models.BooleanField(default=False, verbose_name='LOGOAUDIOMETRIA XX')),
                ('logoaudi_der_ucmlc', models.BooleanField(default=False, verbose_name='LOGOAUDIOMETRIA XX')),
                ('logoaudi_der_uducl', models.BooleanField(default=False, verbose_name='LOGOAUDIOMETRIA')),
                ('logoaudi_izq_umbral', models.BooleanField(default=False, verbose_name='LOGOAUDIOMETRIA')),
                ('logoaudi_izq_discrim', models.BooleanField(default=False, verbose_name='LOGOAUDIOMETRIA')),
                ('logoaudi_izq_ucmlc', models.BooleanField(default=False, verbose_name='LOGOAUDIOMETRIA')),
                ('logoaudi_izq_uducl', models.BooleanField(default=False, verbose_name='LOGOAUDIOMETRIA')),
                ('medico', models.CharField(max_length=200)),
                ('concluciones', models.TextField()),
                ('persona', models.OneToOneField(to='persona.Persona')),
            ],
        ),
    ]
