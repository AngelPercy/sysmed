# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0025_persona_rtn'),
    ]

    operations = [
        migrations.AddField(
            model_name='antecedente',
            name='Enfermedad_ocular_descrip',
            field=models.CharField(max_length=200, verbose_name='ENFERMEDAD OCULAR DESCRIPCION:', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='abec',
            field=models.BooleanField(default=False, verbose_name='ABEC:'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='abeh',
            field=models.BooleanField(default=False, verbose_name='ABEH:'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='aben',
            field=models.BooleanField(default=False, verbose_name='ABEN:'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='anorma_a',
            field=models.BooleanField(default=False, verbose_name=b'ANORMALIDADES'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='anormalidades',
            field=models.CharField(max_length=200, verbose_name='ANORMALIDADES:', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='boca_amigdalas',
            field=models.BooleanField(default=False, help_text='labios sin lesiones mucosa oral rosada brillante congestiva', verbose_name='BOCA AMIGDALAS, FARINGE, LARINGE'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='cuello_anormal',
            field=models.BooleanField(default=False, verbose_name='ANORMALIDADES'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='cuello_normal',
            field=models.BooleanField(default=False, verbose_name='NORMAL'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='desc_b',
            field=models.CharField(max_length=200, verbose_name='DESCRIPCION', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='desc_d',
            field=models.CharField(max_length=200, verbose_name='DESCRIPCION', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='desc_e',
            field=models.CharField(max_length=200, verbose_name='DESCRIPCION', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='desc_f',
            field=models.CharField(max_length=200, verbose_name='DESCRIPCION', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='descr_c',
            field=models.CharField(max_length=200, verbose_name='DESCRIPCION', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='ectoscopia',
            field=models.BooleanField(default=False, verbose_name='ECTOSCOPIA:'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='edentulo_parcial',
            field=models.CharField(blank=True, max_length=1, choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='edentulo_total',
            field=models.CharField(blank=True, max_length=1, choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='genitales_anormal',
            field=models.BooleanField(default=False, verbose_name=b'ANORMALIDADES'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='genitales_normal',
            field=models.BooleanField(default=False, verbose_name=b'NORMAL'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='gingivitis',
            field=models.CharField(blank=True, max_length=1, choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='lotep',
            field=models.BooleanField(default=False, verbose_name='LOTEP:'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='nariz_anormal',
            field=models.BooleanField(default=False, verbose_name='ANORMALIDADES'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='nariz_normal',
            field=models.BooleanField(default=False, verbose_name='NORMAL'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='piezas_faltan',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='piezas_mal_estado',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='ppf',
            field=models.CharField(blank=True, max_length=1, choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='ppr',
            field=models.CharField(blank=True, max_length=1, choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='sin_alteraciones',
            field=models.CharField(max_length=200, verbose_name='SIN ALTERACIONES', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='v_c_o_d_corregida',
            field=models.CharField(max_length=20, verbose_name='Ojo derecho Corregida Visi\xf3n de Cerca:', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='v_c_o_d_sin_corregir',
            field=models.CharField(max_length=20, verbose_name='Ojo Derecho S/C Visi\xf3n de Cerca:', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='v_c_o_i_corregida',
            field=models.CharField(max_length=20, verbose_name='Ojo Izquierdo Corregida Visi\xf3n de Cerca:', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='v_c_o_i_sin_corregir',
            field=models.CharField(max_length=20, verbose_name='Ojo Izquierdo S/C Visi\xf3n de Cerca:', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='v_l_o_d_corregida',
            field=models.CharField(max_length=20, verbose_name='Ojo derecho Corregida Visi\xf3n de Cerca:', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='v_l_o_d_sin_corregir',
            field=models.CharField(max_length=20, verbose_name='Ojo Derecho S/C Visi\xf3n de Lejos:', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='v_l_o_i_corregida',
            field=models.CharField(max_length=20, verbose_name='Ojo Izquierdo Corregida Visi\xf3n de Cerca:', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='v_l_o_i_sin_corregir',
            field=models.CharField(max_length=20, verbose_name='Ojo Izquierdo S/C Visi\xf3n de Lejos:', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='vision_colores_nistagnos',
            field=models.CharField(blank=True, max_length=1, choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='vision_colores_normal',
            field=models.CharField(blank=True, max_length=1, choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
    ]
