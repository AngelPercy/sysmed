# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0021_evaluacionaudiometrica'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluacionaudiometrica',
            name='persona',
        ),
        migrations.RemoveField(
            model_name='estilovida',
            name='cafe',
        ),
        migrations.RemoveField(
            model_name='estilovida',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='estilovida',
            name='cantidad_cafe',
        ),
        migrations.RemoveField(
            model_name='estilovida',
            name='cerveza',
        ),
        migrations.RemoveField(
            model_name='estilovida',
            name='consume_drogas',
        ),
        migrations.RemoveField(
            model_name='estilovida',
            name='consume_tabaco',
        ),
        migrations.RemoveField(
            model_name='estilovida',
            name='consumo_diario_tabaco',
        ),
        migrations.RemoveField(
            model_name='estilovida',
            name='dieta',
        ),
        migrations.RemoveField(
            model_name='estilovida',
            name='drogas',
        ),
        migrations.RemoveField(
            model_name='estilovida',
            name='inicio_consumo_tabaco',
        ),
        migrations.RemoveField(
            model_name='estilovida',
            name='licor',
        ),
        migrations.RemoveField(
            model_name='estilovida',
            name='numero_comidas',
        ),
        migrations.RemoveField(
            model_name='estilovida',
            name='otros',
        ),
        migrations.RemoveField(
            model_name='estilovida',
            name='tipo_de_comidas',
        ),
        migrations.RemoveField(
            model_name='estilovida',
            name='tipo_de_tabaco',
        ),
        migrations.RemoveField(
            model_name='estilovida',
            name='vino',
        ),
        migrations.AddField(
            model_name='estilovida',
            name='acutenos',
            field=models.BooleanField(default=True, verbose_name='ACUTENOS:'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='algodones',
            field=models.CharField(blank=True, max_length=1, verbose_name='ALGODONES:', choices=[(b'A', 'A VECES'), (b'B', 'SIEMPRE'), (b'C', 'NUNCA')]),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='anos_trabajo',
            field=models.CharField(max_length=200, verbose_name='A\xd1OS DE TRABAJO:', blank=True),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='antecedentes',
            field=models.CharField(max_length=200, verbose_name='ANTECEDENTES:', blank=True),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='apresiacion_ruido',
            field=models.CharField(blank=True, max_length=1, verbose_name='APRECIACION DEL RUIDO:', choices=[(b'I', 'MUY INTENSO'), (b'M', 'MODERADO'), (b'O', 'NO MOLESTO')]),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='armas_fuego',
            field=models.BooleanField(default=True, verbose_name='USO DE ARMAS DE FUEGO:'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='audifonos',
            field=models.BooleanField(default=True, verbose_name='AUDIFONOS:'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='audiometria_ante',
            field=models.CharField(max_length=200, verbose_name='AUDIOMETRIA ANTERIOR:', blank=True),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='buceo',
            field=models.BooleanField(default=True, verbose_name='BUCEO:'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='concluciones',
            field=models.CharField(max_length=200, verbose_name='CONCLUCIONES', blank=True),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='diapaz_od_1000hz',
            field=models.BooleanField(default=False, verbose_name='DIAPAZONES OIDO DERECHO 1000 Hz'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='diapaz_od_250hz',
            field=models.BooleanField(default=False, verbose_name='DIAPAZONES OIDO DERECHO 250 Hz:'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='diapaz_od_500hz',
            field=models.BooleanField(default=False, verbose_name='DIAPAZONES OIDO DERECHO 500 Hz'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='diapaz_oi_1000hz',
            field=models.BooleanField(default=False, verbose_name='DIAPAZONES OIDO IZQUIERDO 1000 Hz'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='diapaz_oi_250hz',
            field=models.BooleanField(default=False, verbose_name='DIAPAZONES OIDO IZQUIERDO 250 Hz'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='diapaz_oi_500hz',
            field=models.BooleanField(default=False, verbose_name='DIAPAZONES OIDO IZQUIERDO 500 Hz'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='discotecas',
            field=models.BooleanField(default=True, verbose_name='DISCOTECAS:'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='empr',
            field=models.CharField(max_length=200, verbose_name='EMPRESA:', blank=True),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='enf_tra_respiratorio',
            field=models.BooleanField(default=True, verbose_name='ENF. DEL TRACTO RESPIRATORIO ACTUAL:'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='exp_quimico',
            field=models.BooleanField(default=True, verbose_name='EXP. QUIMICO:'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='exp_recien_ruid18',
            field=models.BooleanField(default=True, verbose_name='EXPOSICION RECIENTE A RUIDOS (18 HORAS)'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='expos_laboral_ruido',
            field=models.BooleanField(default=True, verbose_name='EXPOS. LABORAL AL RUIDO:'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='fecha_examen',
            field=models.DateField(default=datetime.date.today, verbose_name='FECHA DE EXAMEN:'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='garganta_anormal',
            field=models.BooleanField(default=False, verbose_name='GARGANTA ANORMAL'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='garganta_normal',
            field=models.BooleanField(default=False, verbose_name='GARGANTA NORMAL'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='hipoacusia',
            field=models.BooleanField(default=True, verbose_name='HIPOACUSIA:'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='logoaudi_der_discrim',
            field=models.BooleanField(default=False, verbose_name='LOGOAUDIOMETRIA XX'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='logoaudi_der_ucmlc',
            field=models.BooleanField(default=False, verbose_name='LOGOAUDIOMETRIA XX'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='logoaudi_der_uducl',
            field=models.BooleanField(default=False, verbose_name='LOGOAUDIOMETRIA'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='logoaudi_der_umbral',
            field=models.BooleanField(default=False, verbose_name='LOGOAUDIOMETRIA DERECHO'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='logoaudi_izq_discrim',
            field=models.BooleanField(default=False, verbose_name='LOGOAUDIOMETRIA'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='logoaudi_izq_ucmlc',
            field=models.BooleanField(default=False, verbose_name='LOGOAUDIOMETRIA'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='logoaudi_izq_uducl',
            field=models.BooleanField(default=False, verbose_name='LOGOAUDIOMETRIA'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='logoaudi_izq_umbral',
            field=models.BooleanField(default=False, verbose_name='LOGOAUDIOMETRIA'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='med_ototoxicos',
            field=models.BooleanField(default=True, verbose_name='MEDICINA OTOTOXICOS:'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='medico',
            field=models.CharField(max_length=200, verbose_name='MEDICO', blank=True),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='meningitis',
            field=models.BooleanField(default=True, verbose_name='MENINGITIS:'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='ocupacion',
            field=models.CharField(max_length=200, verbose_name='OCUPACION:', blank=True),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='oido_anormal',
            field=models.BooleanField(default=False, verbose_name='OIDO ANORMAL'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='oido_normal',
            field=models.BooleanField(default=False, verbose_name='OIDO NORMAL'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='orejeras',
            field=models.CharField(blank=True, max_length=1, verbose_name='OREJERAS:', choices=[(b'A', 'A VECES'), (b'B', 'SIEMPRE'), (b'C', 'NUNCA')]),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='otalgia',
            field=models.BooleanField(default=True, verbose_name='OTALGIA:'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='otoscopia_od',
            field=models.BooleanField(default=False, verbose_name='OTOSCOPIA O.D.:'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='otoscopia_oi',
            field=models.BooleanField(default=False, verbose_name='OTOSCOPIA O.I.:'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='parotiditis',
            field=models.BooleanField(default=True, verbose_name='PAROTIDITIS:'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='resul_audiomet',
            field=models.CharField(max_length=200, verbose_name='RESULTADOS DE AUDIOMETRIA:', blank=True),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='sarampion',
            field=models.BooleanField(default=True, verbose_name='SARAMPION'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='secresion_otica',
            field=models.BooleanField(default=True, verbose_name='SECRECION OTICA'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='sistomatologia',
            field=models.CharField(max_length=200, verbose_name='SISTOMATOLOGIA', blank=True),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='tapones',
            field=models.CharField(blank=True, max_length=1, verbose_name='TAPONES:', choices=[(b'A', 'A VECES'), (b'B', 'SIEMPRE'), (b'C', 'NUNCA')]),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='tec',
            field=models.BooleanField(default=True, verbose_name='TEC:'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='tiempo_exposicion',
            field=models.CharField(max_length=200, verbose_name='TIEMPO DE EXPOSICION A RUIDO (8 HR):', blank=True),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='trauma_acustico',
            field=models.BooleanField(default=True, verbose_name='TRAUMA ACUSTICO:'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='vertigo',
            field=models.BooleanField(default=True, verbose_name='VERTIGO:'),
        ),
        migrations.AddField(
            model_name='estilovida',
            name='viaje_reciente',
            field=models.BooleanField(default=True, verbose_name='VIAJE RECIENTE < 6 HORAS:'),
        ),
        migrations.DeleteModel(
            name='EvaluacionAudiometrica',
        ),
    ]
