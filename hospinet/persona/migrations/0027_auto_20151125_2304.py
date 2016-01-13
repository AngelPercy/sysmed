# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0026_auto_20151123_0059'),
    ]

    operations = [
        migrations.AddField(
            model_name='antecedente',
            name='abdomen_simetrico',
            field=models.BooleanField(default=False, verbose_name='ABDOMEN NORMAL'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='anormalida',
            field=models.CharField(max_length=200, verbose_name='ANORMALIDADES', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='audicion_d_hz_1000',
            field=models.CharField(max_length=20, verbose_name='AUD. DER. Hz 1000', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='audicion_d_hz_2000',
            field=models.CharField(max_length=20, verbose_name='AUD. DER. Hz 2000', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='audicion_d_hz_3000',
            field=models.CharField(max_length=20, verbose_name='AUD. DER. Hz 3000', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='audicion_d_hz_4000',
            field=models.CharField(max_length=20, verbose_name='AUD. DER. Hz 4000', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='audicion_d_hz_500',
            field=models.CharField(max_length=20, verbose_name='AUD. DER. Hz 500', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='audicion_d_hz_6000',
            field=models.CharField(max_length=20, verbose_name='AUD. DER. Hz 6000', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='audicion_d_hz_8000',
            field=models.CharField(max_length=20, verbose_name='AUD. DER. Hz 8000', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='audicion_i_hz_1000',
            field=models.CharField(max_length=20, verbose_name='AUD. IZQ. Hz 1000', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='audicion_i_hz_2000',
            field=models.CharField(max_length=20, verbose_name='AUD. IZQ. Hz 2000', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='audicion_i_hz_3000',
            field=models.CharField(max_length=20, verbose_name='AUD. IZQ. Hz 3000', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='audicion_i_hz_4000',
            field=models.CharField(max_length=20, verbose_name='AUD. IZQ. Hz 4000', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='audicion_i_hz_500',
            field=models.CharField(max_length=20, verbose_name='AUD. IZQ. Hz 500', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='audicion_i_hz_6000',
            field=models.CharField(max_length=20, verbose_name='AUD. IZQ. Hz 6000', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='audicion_i_hz_8000',
            field=models.CharField(max_length=20, verbose_name='AUD. IZQ. Hz 8000', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='columna_vert_anormal',
            field=models.BooleanField(default=False, verbose_name='COLUMAN VERTEBRAL ANORMAL'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='columna_vert_normal',
            field=models.CharField(max_length=200, verbose_name='COLUMNA VERTEBRAL NORMAL', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='comentario',
            field=models.CharField(max_length=200, verbose_name='COMENTARIO', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='comentarios',
            field=models.CharField(help_text='EXAMENES DE TORAX ECTOSCOPIA', max_length=200, verbose_name='COMENTARIO', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='corazon_anormal',
            field=models.BooleanField(default=False, verbose_name=b'ANORMAL'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='corazon_normal',
            field=models.BooleanField(default=False, verbose_name=b'CORAZON NORMAL'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='derecha_conservada',
            field=models.BooleanField(default=False, verbose_name='AUD. DER. CONSERVADA'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='desc_g',
            field=models.CharField(max_length=200, verbose_name='DESCRIPCION', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='desc_h',
            field=models.CharField(max_length=200, verbose_name='DESCRIPCION', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='desc_i',
            field=models.CharField(max_length=200, verbose_name='DESCRIPCION', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='desc_j',
            field=models.CharField(max_length=200, verbose_name='DESCRIPCION', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='desc_k',
            field=models.CharField(max_length=200, verbose_name='DESCRIPCION', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='desc_l',
            field=models.CharField(max_length=200, verbose_name='DESCRIPCION', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='desc_m',
            field=models.CharField(help_text='REFLEJOS OSTEOTENDINOS', max_length=200, verbose_name='DESCRIPCION', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='desc_n',
            field=models.BooleanField(default=False, verbose_name='DESCRIPCION'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='funciones_superiores',
            field=models.BooleanField(default=False, verbose_name='FUNCIONES SUP. CONSERVADA'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='hernias',
            field=models.CharField(blank=True, max_length=1, verbose_name='HERNIAS', choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='hipereflexia',
            field=models.BooleanField(default=False, verbose_name='HIPEREFLEXIA'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='izquierdo_conservada',
            field=models.BooleanField(default=False, verbose_name='AUD. IZQ. CONSERVADA'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='marcha_conservada',
            field=models.CharField(max_length=200, verbose_name='MARCHA CONSERVADA', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='miembro_infe_der_anormal',
            field=models.BooleanField(default=False, verbose_name='MIENBRO INF. DERECHO ANORMAL'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='miembro_infe_der_normal',
            field=models.BooleanField(default=False, verbose_name='MIENBRO INF. DERECHO NORMAL'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='miembro_infe_izq_anormal',
            field=models.BooleanField(default=False, verbose_name='MIENBRO INF. IZQUIERDO ANORMAL'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='miembro_infe_izq_normal',
            field=models.BooleanField(default=False, verbose_name='MIENBRO INF. IZQUIERDO NORMAL'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='miembro_sup_der_normal',
            field=models.BooleanField(default=False, verbose_name='MIENBRO SUP. DERECHO NORMAL'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='miembro_sup_izq_anormal',
            field=models.BooleanField(default=False, verbose_name='MIENBRO SUP. IZQUIERDO ANORMAL'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='miembro_sup_izq_normal',
            field=models.BooleanField(default=False, verbose_name='MIENBRO SUP. IZQUIERDO NORMAL'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='mienbro_sup_der_anormal',
            field=models.BooleanField(default=False, verbose_name='MIENBRO SUP. DERECHO ANORMAL'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='normoreflexia',
            field=models.BooleanField(default=False, verbose_name='NORMOREFLEXIA'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='presentes',
            field=models.BooleanField(default=False, verbose_name='PRESENTES'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='prl_der',
            field=models.CharField(blank=True, max_length=1, verbose_name='PRL Drch', choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='prl_izq',
            field=models.CharField(blank=True, max_length=1, verbose_name='PRL Izq', choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='pru_med_der',
            field=models.CharField(blank=True, max_length=1, verbose_name='PRU Med Drch', choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='pru_med_izq',
            field=models.CharField(blank=True, max_length=1, verbose_name='PRU Med Izq', choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='pru_sup_der',
            field=models.CharField(blank=True, max_length=1, verbose_name='PRU Sup Drch', choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='pru_sup_izq',
            field=models.CharField(blank=True, max_length=1, verbose_name='PRU Sup Izq.', choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='psicologico',
            field=models.CharField(blank=True, max_length=1, verbose_name='PSICOLOGICO', choices=[(b'A', 'APTO'), (b'N', 'NO APTO')]),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='pulmones_anormal',
            field=models.BooleanField(default=False, verbose_name=b'ANORMAL'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='pulmones_normal',
            field=models.BooleanField(default=False, verbose_name=b'PULMONES NORMAL'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='t_d_abombamiento',
            field=models.CharField(blank=True, max_length=1, verbose_name='TIMPANO DER. ABOMBAMIENTO', choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='t_d_observaciones',
            field=models.CharField(max_length=100, verbose_name='TIMPANO DERECHO OBSERVACIONES', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='t_d_perforaciones',
            field=models.CharField(blank=True, max_length=1, verbose_name='TIMPANO DER. PERFORACIONES', choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='t_d_tapon_cerumen',
            field=models.CharField(blank=True, max_length=1, verbose_name='TIMPANO DER. TAPON CERUMEN', choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='t_d_triangulo_de_luz',
            field=models.CharField(blank=True, max_length=1, verbose_name='TIMPANO DER. TRIANGULO DE LUZ', choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='t_i_abombamiento',
            field=models.CharField(blank=True, max_length=1, verbose_name='TIMPANO IZQ. ABOMBAMIENTO', choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='t_i_observaciones',
            field=models.CharField(max_length=100, verbose_name='TIMPANO IZQUIERDO OBSERVACIONES', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='t_i_perforaciones',
            field=models.CharField(blank=True, max_length=1, verbose_name='TIMPANO IZQ. PERFORACIONES', choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='t_i_tapon_cerumen',
            field=models.CharField(blank=True, max_length=1, verbose_name='TIMPANO IZQ. TAPON CERUMEN', choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='t_i_triangulo_de_luz',
            field=models.CharField(blank=True, max_length=1, verbose_name='TIMPANO IZQ. TRIANGULO DE LUZ', choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='torax_ectoscopia_anormal',
            field=models.BooleanField(default=False, verbose_name=b'ANORMAL'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='torax_ectoscopia_normal',
            field=models.BooleanField(default=False, verbose_name=b'EXTOSCOPIA NORMAL'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='varices',
            field=models.CharField(blank=True, max_length=1, verbose_name='VARICES', choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='Enfermedad_ocular_descrip',
            field=models.CharField(max_length=200, verbose_name='ENF. OCULAR DESC.', blank=True),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='alcohol',
            field=models.CharField(blank=True, max_length=1, verbose_name='HABITOS ALCOHOL:', choices=[(b'N', 'NADA'), (b'P', 'POCO'), (b'H', 'HABITUAL'), (b'E', 'EXESIVO')]),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='artropatia',
            field=models.BooleanField(default=False, verbose_name='ARTROPATIA:'),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='cancer',
            field=models.BooleanField(default=False, verbose_name='CANCER:'),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='coca',
            field=models.CharField(blank=True, max_length=1, verbose_name='HABITOS COCA:', choices=[(b'N', 'NADA'), (b'P', 'POCO'), (b'H', 'HABITUAL'), (b'E', 'EXESIVO')]),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='cuello_anormal',
            field=models.BooleanField(default=False, verbose_name='CUELLO ANORMAL'),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='cuello_normal',
            field=models.BooleanField(default=False, verbose_name=' CUELLO NORMAL'),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='desc_f',
            field=models.CharField(help_text='DENTADURA ODONTOGRAMA DE ACUERDO A MINSA', max_length=200, verbose_name='DESCRIPCION', blank=True),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='edentulo_parcial',
            field=models.CharField(blank=True, max_length=1, verbose_name='EDENTULO PARCIAL', choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='edentulo_total',
            field=models.CharField(blank=True, max_length=1, verbose_name='EDENTULO TOTAL', choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='genitales_anormal',
            field=models.BooleanField(default=False, verbose_name=b'GENITALES ANORMAL'),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='genitales_normal',
            field=models.BooleanField(default=False, verbose_name=b'GENITALES NORMALES'),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='gingivitis',
            field=models.CharField(blank=True, max_length=1, verbose_name='GINGIVITIS', choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='medicacion_actual',
            field=models.CharField(max_length=200, null=True, verbose_name='MEDICACION ACTUAL:', blank=True),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='migrana',
            field=models.BooleanField(default=False, verbose_name='MIGRA\xd1A:'),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='nariz_anormal',
            field=models.BooleanField(default=False, verbose_name='NARIZ ANORMAL'),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='nariz_normal',
            field=models.BooleanField(default=False, verbose_name='NARIZ NORMAL'),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='otros_b',
            field=models.CharField(max_length=200, verbose_name='OBSERVACIONES:', blank=True),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='piezas_faltan',
            field=models.CharField(help_text='EXAMENES DE LOS OJOS', max_length=200, verbose_name='PIEZAS QUE FALTAN', blank=True),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='piezas_mal_estado',
            field=models.CharField(max_length=200, verbose_name='PIEZAS EN MAL ESTADO', blank=True),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='ppf',
            field=models.CharField(blank=True, max_length=1, verbose_name='PPF', choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='ppr',
            field=models.CharField(blank=True, max_length=1, verbose_name='PPR', choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='pt_columna',
            field=models.BooleanField(default=False, verbose_name='PT.COLUMNA:'),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='sd_metabolico',
            field=models.BooleanField(default=False, verbose_name='SD. METABOLICO:'),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='sin_alteraciones',
            field=models.CharField(help_text='EXAMENES DE LOS OIDOS DERECHO E IZQUIERDO', max_length=200, verbose_name='SIN ALTERACIONES', blank=True),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='tabaco',
            field=models.CharField(blank=True, max_length=1, verbose_name='HABITOS TABACO:', choices=[(b'N', 'NADA'), (b'P', 'POCO'), (b'H', 'HABITUAL'), (b'E', 'EXESIVO')]),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='v_c_o_d_corregida',
            field=models.CharField(max_length=20, verbose_name='OJO DER. CORREGIDA Visi\xf3n de Cerca:', blank=True),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='v_c_o_d_sin_corregir',
            field=models.CharField(max_length=20, verbose_name='OJO DER. S/C Visi\xf3n de Cerca:', blank=True),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='v_c_o_i_corregida',
            field=models.CharField(max_length=20, verbose_name='OJO IZQ. CORREGIDA Visi\xf3n de Cerca:', blank=True),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='v_c_o_i_sin_corregir',
            field=models.CharField(max_length=20, verbose_name='OJO IZQ. S/C Visi\xf3n de Cerca:', blank=True),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='v_l_o_d_corregida',
            field=models.CharField(max_length=20, verbose_name='OJO DER. CORREGIDA Visi\xf3n de Cerca:', blank=True),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='v_l_o_d_sin_corregir',
            field=models.CharField(max_length=20, verbose_name='OJO DER. S/C Visi\xf3n de Lejos:', blank=True),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='v_l_o_i_corregida',
            field=models.CharField(max_length=20, verbose_name='OJO IZQ. CORREGIDA Visi\xf3n de Cerca:', blank=True),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='v_l_o_i_sin_corregir',
            field=models.CharField(max_length=20, verbose_name='OJO IZQ. S/C Visi\xf3n de Lejos:', blank=True),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='vision_colores_nistagnos',
            field=models.CharField(blank=True, max_length=1, verbose_name='VISION DE COLORES NISTAGNOS', choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='vision_colores_normal',
            field=models.CharField(blank=True, max_length=1, verbose_name='VISION DE COLORES', choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
    ]
