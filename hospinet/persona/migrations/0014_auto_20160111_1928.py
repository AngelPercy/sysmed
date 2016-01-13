# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0013_persona_mostrar_en_cardex'),
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
        migrations.RenameField(
            model_name='antecedente',
            old_name='alcoholismo',
            new_name='cirugia',
        ),
        migrations.RenameField(
            model_name='antecedentefamiliar',
            old_name='alcoholismo',
            new_name='vivos',
        ),
        migrations.RenameField(
            model_name='fisico',
            old_name='color_de_cabello',
            new_name='expiracion_forzada',
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
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='alergias',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='asma',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='cancer',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='colelitiasis',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='colitis',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='congenital',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='diabetes',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='dislipidemias',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='epoc',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='general',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='hipertension',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='migrana',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='nutricional',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='obesidad',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='sindrome_coronario_agudo',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='sinusitis',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='tabaquismo',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='tiroides',
        ),
        migrations.RemoveField(
            model_name='antecedentefamiliar',
            name='tuberculosis',
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
        migrations.RemoveField(
            model_name='fisico',
            name='altura',
        ),
        migrations.RemoveField(
            model_name='fisico',
            name='color_de_ojos',
        ),
        migrations.RemoveField(
            model_name='fisico',
            name='factor_rh',
        ),
        migrations.RemoveField(
            model_name='fisico',
            name='lateralidad',
        ),
        migrations.RemoveField(
            model_name='fisico',
            name='tipo_de_sangre',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='fax',
        ),
        migrations.AddField(
            model_name='antecedente',
            name='Enfermedad_ocular_descrip',
            field=models.CharField(max_length=200, verbose_name='ENF. OCULAR DESC.', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='abdomen_anormal',
            field=models.BooleanField(default=False, verbose_name='ANORMALIDADES'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='abdomen_normal',
            field=models.BooleanField(default=False, verbose_name='ABDOMEN NORMAL'),
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
            name='alcohol',
            field=models.CharField(blank=True, max_length=1, verbose_name='HABITOS ALCOHOL:', choices=[(b'N', 'NADA'), (b'P', 'POCO'), (b'H', 'HABITUAL'), (b'E', 'EXESIVO')]),
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
            name='artropatia',
            field=models.BooleanField(default=False, verbose_name='ARTROPATIA:'),
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
            name='biologico',
            field=models.BooleanField(default=False, verbose_name='BIOLOGICO'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='boca_amigdalas',
            field=models.BooleanField(default=False, help_text='labios sin lesiones mucosa oral rosada brillante congestiva', verbose_name='BOCA AMIGDALAS, FARINGE, LARINGE'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='cancerigeno',
            field=models.BooleanField(default=False, verbose_name='CANCERIGENO'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='carga',
            field=models.BooleanField(default=False, verbose_name='CARGAS'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='coca',
            field=models.CharField(blank=True, max_length=1, verbose_name='HABITOS COCA:', choices=[(b'N', 'NADA'), (b'P', 'POCO'), (b'H', 'HABITUAL'), (b'E', 'EXESIVO')]),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='columna_vert_anormal',
            field=models.BooleanField(default=False, verbose_name='COLUMAN VERTEBRAL ANORMAL'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='columna_vert_normal',
            field=models.BooleanField(default=False, verbose_name='COLUMNA VERTEBRAL NORMAL'),
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
            name='cuello_anormal',
            field=models.BooleanField(default=False, verbose_name='CUELLO ANORMAL'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='cuello_normal',
            field=models.BooleanField(default=False, verbose_name=' CUELLO NORMAL'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='derecha_conservada',
            field=models.BooleanField(default=False, verbose_name='AUD. DER. CONSERVADA'),
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
            field=models.CharField(help_text='DENTADURA ODONTOGRAMA DE ACUERDO A MINSA', max_length=200, verbose_name='DESCRIPCION', blank=True),
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
            field=models.CharField(max_length=200, verbose_name='DESCRIPCION', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='desc_n',
            field=models.CharField(max_length=200, verbose_name='DESCRIPCION', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='descr_c',
            field=models.CharField(max_length=200, verbose_name='DESCRIPCION', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='dm',
            field=models.BooleanField(default=False, verbose_name='DM:'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='ectoscopia',
            field=models.BooleanField(default=False, verbose_name='ECTOSCOPIA:'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='edentulo_parcial',
            field=models.CharField(blank=True, max_length=1, verbose_name='EDENTULO PARCIAL', choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='edentulo_total',
            field=models.CharField(blank=True, max_length=1, verbose_name='EDENTULO TOTAL', choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='funciones_superiores',
            field=models.BooleanField(default=False, verbose_name='FUNCIONES SUP. CONSERVADA'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='genitales_anormal',
            field=models.BooleanField(default=False, verbose_name=b'GENITALES ANORMAL'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='genitales_normal',
            field=models.BooleanField(default=False, verbose_name=b'GENITALES NORMALES'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='gingivitis',
            field=models.CharField(blank=True, max_length=1, verbose_name='GINGIVITIS', choices=[(b'0', 'SI'), (b'1', 'NO')]),
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
            name='izquierdo_conservada',
            field=models.BooleanField(default=False, verbose_name='AUD. IZQ. CONSERVADA'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='lotep',
            field=models.BooleanField(default=False, verbose_name='LOTEP:'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='marcha_conservada',
            field=models.CharField(max_length=200, verbose_name='MARCHA CONSERVADA', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='medicacion_actual',
            field=models.CharField(max_length=200, null=True, verbose_name='MEDICACION ACTUAL:', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='metales',
            field=models.BooleanField(default=False, verbose_name='MENTALES'),
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
            name='movimiento',
            field=models.BooleanField(default=False, verbose_name='MOVIMIENTO'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='mutagenico',
            field=models.BooleanField(default=False, verbose_name='MUTAGENICOS'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='nariz_anormal',
            field=models.BooleanField(default=False, verbose_name='NARIZ ANORMAL'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='nariz_normal',
            field=models.BooleanField(default=False, verbose_name='NARIZ NORMAL'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='normoreflexia',
            field=models.BooleanField(default=False, verbose_name='NORMOREFLEXIA'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='otros_a',
            field=models.BooleanField(default=False, verbose_name='OTROS'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='otros_b',
            field=models.CharField(max_length=200, verbose_name='OBSERVACIONES:', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='pesados',
            field=models.BooleanField(default=False, verbose_name='PESADOS'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='piezas_faltan',
            field=models.CharField(help_text='EXAMENES DE LOS OJOS', max_length=200, verbose_name='PIEZAS QUE FALTAN', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='piezas_mal_estado',
            field=models.CharField(max_length=200, verbose_name='PIEZAS EN MAL ESTADO', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='polvo',
            field=models.BooleanField(default=False, verbose_name='POLVO'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='postula',
            field=models.CharField(max_length=200, verbose_name='PUESTO AL QUE POSTULA:', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='postura',
            field=models.BooleanField(default=False, verbose_name='POSTURA'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='ppf',
            field=models.CharField(blank=True, max_length=1, verbose_name='PPF', choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='ppr',
            field=models.CharField(blank=True, max_length=1, verbose_name='PPR', choices=[(b'0', 'SI'), (b'1', 'NO')]),
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
            name='pt_columna',
            field=models.BooleanField(default=False, verbose_name='PT.COLUMNA:'),
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
            name='ram',
            field=models.BooleanField(default=False, verbose_name='RAM:'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='repetitivo',
            field=models.BooleanField(default=False, verbose_name='REPETITIVO'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='ruido',
            field=models.BooleanField(default=False, verbose_name='RUIDO'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='sd_metabolico',
            field=models.BooleanField(default=False, verbose_name='SD. METABOLICO:'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='segmentaria',
            field=models.BooleanField(default=False, verbose_name='SEGMENTARIA'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='sin_alteraciones',
            field=models.CharField(help_text='EXAMENES DE LOS OIDOS DERECHO E IZQUIERDO', max_length=200, verbose_name='SIN ALTERACIONES', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='solvente',
            field=models.BooleanField(default=False, verbose_name='SOLVENTE'),
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
            name='tabaco',
            field=models.CharField(blank=True, max_length=1, verbose_name='HABITOS TABACO:', choices=[(b'N', 'NADA'), (b'P', 'POCO'), (b'H', 'HABITUAL'), (b'E', 'EXESIVO')]),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='temperatura',
            field=models.BooleanField(default=False, verbose_name='TEMPERATURA'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='torax_ectoscopia_anormal',
            field=models.BooleanField(default=False, verbose_name=b'ANORMAL'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='torax_ectoscopia_normal',
            field=models.BooleanField(default=False, verbose_name=b'ECTOSCOPIA NORMAL'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='turno_noche',
            field=models.BooleanField(default=False, verbose_name='TURNOS NOCHE'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='v_c_o_d_corregida',
            field=models.CharField(max_length=20, verbose_name='OJO DER. CORREGIDA Visi\xf3n de Cerca:', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='v_c_o_d_sin_corregir',
            field=models.CharField(max_length=20, verbose_name='OJO DER. S/C Visi\xf3n de Cerca:', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='v_c_o_i_corregida',
            field=models.CharField(max_length=20, verbose_name='OJO IZQ. CORREGIDA Visi\xf3n de Cerca:', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='v_c_o_i_sin_corregir',
            field=models.CharField(max_length=20, verbose_name='OJO IZQ. S/C Visi\xf3n de Cerca:', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='v_l_o_d_corregida',
            field=models.CharField(max_length=20, verbose_name='OJO DER. CORREGIDA Visi\xf3n de Cerca:', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='v_l_o_d_sin_corregir',
            field=models.CharField(max_length=20, verbose_name='OJO DER. S/C Visi\xf3n de Lejos:', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='v_l_o_i_corregida',
            field=models.CharField(max_length=20, verbose_name='OJO IZQ. CORREGIDA Visi\xf3n de Cerca:', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='v_l_o_i_sin_corregir',
            field=models.CharField(max_length=20, verbose_name='OJO IZQ. S/C Visi\xf3n de Lejos:', blank=True),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='varices',
            field=models.CharField(blank=True, max_length=1, verbose_name='VARICES', choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='vibracion',
            field=models.BooleanField(default=False, verbose_name='VIBRACION'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='vibracion_total',
            field=models.BooleanField(default=False, verbose_name='VIBRACION TOTAL'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='vision_colores_nistagnos',
            field=models.CharField(blank=True, max_length=1, verbose_name='VISION DE COLORES NISTAGNOS', choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='vision_colores_normal',
            field=models.CharField(blank=True, max_length=1, verbose_name='VISION DE COLORES', choices=[(b'0', 'SI'), (b'1', 'NO')]),
        ),
        migrations.AddField(
            model_name='antecedentefamiliar',
            name='con_importancia',
            field=models.BooleanField(default=False, verbose_name='CON IMPORTANCIA'),
        ),
        migrations.AddField(
            model_name='antecedentefamiliar',
            name='hermano',
            field=models.CharField(max_length=200, verbose_name='HERMANO:', blank=True),
        ),
        migrations.AddField(
            model_name='antecedentefamiliar',
            name='mama',
            field=models.CharField(max_length=200, verbose_name='MAMA:', blank=True),
        ),
        migrations.AddField(
            model_name='antecedentefamiliar',
            name='n_hijos',
            field=models.CharField(max_length=100, verbose_name='N\xb0 DE HIJOS:', blank=True),
        ),
        migrations.AddField(
            model_name='antecedentefamiliar',
            name='papa',
            field=models.CharField(max_length=200, verbose_name='PAPA:', blank=True),
        ),
        migrations.AddField(
            model_name='antecedentefamiliar',
            name='sin_importancia',
            field=models.BooleanField(default=False, verbose_name='SIN IMPORTANCIA'),
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
            field=models.CharField(max_length=200, verbose_name='MAX INSPIRACION:', blank=True),
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
        migrations.AddField(
            model_name='persona',
            name='establecimiento',
            field=models.CharField(max_length=200, verbose_name='ESTABLECIMIENTO:', blank=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='examen_medico',
            field=models.CharField(blank=True, max_length=1, choices=[(b'O', 'PRE OCUPACIONAL'), (b'I', 'PERIDICO'), (b'E', 'RETIRO'), (b'U', 'POR CAMBIO DE PUESTO'), (b'A', 'POR REINCORPORACION')]),
        ),
        migrations.AddField(
            model_name='persona',
            name='fecha_examen',
            field=models.DateField(default=datetime.date.today, verbose_name='FECHA DE EXAMEN:'),
        ),
        migrations.AddField(
            model_name='persona',
            name='lugar_nac',
            field=models.CharField(max_length=200, null=True, verbose_name='LUGAR NACIMIENTO:', blank=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='proyecto',
            field=models.CharField(max_length=200, verbose_name='PROYECTO:', blank=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='trabajo_realizar',
            field=models.CharField(blank=True, max_length=1, choices=[(b'0', 'CHOFER'), (b'1', 'TRABAJOS DE ALTURA'), (b'2', 'ADMINISTRATIVO'), (b'3', 'LABORATORIO'), (b'4', 'TRABAJO ESPACIO CONFINADO'), (b'5', 'MANTENIMIENTO LIMPIEZA')]),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='asma',
            field=models.BooleanField(default=False, verbose_name='ASMA:'),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='cancer',
            field=models.BooleanField(default=False, verbose_name='CANCER:'),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='migrana',
            field=models.BooleanField(default=False, verbose_name='MIGRA\xd1A:'),
        ),
        migrations.AlterField(
            model_name='fisico',
            name='peso',
            field=models.DecimalField(null=True, verbose_name='PESO:', max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='persona',
            name='apellido',
            field=models.CharField(max_length=50, verbose_name='APELLIDOS:', blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='celular',
            field=models.CharField(max_length=200, verbose_name='CELULAR:', blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='domicilio',
            field=models.CharField(max_length=200, verbose_name='DOMICILIO:', blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='email',
            field=models.CharField(max_length=200, verbose_name='E-MAIL:', blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='estado_civil',
            field=models.CharField(blank=True, max_length=1, verbose_name='ESTADO CIVIL:', choices=[(b'S', 'Soltero/a'), (b'D', 'Divorciado/a'), (b'C', 'Casado/a'), (b'U', 'Union Libre')]),
        ),
        migrations.AlterField(
            model_name='persona',
            name='identificacion',
            field=models.CharField(max_length=8, verbose_name='D.N.I:', blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='mostrar_en_cardex',
            field=models.BooleanField(default=False, verbose_name='Realizar Seguimiento'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nacimiento',
            field=models.DateField(default=datetime.date.today, verbose_name='FECHA NACIMIENTO:'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='NOMBRES:', blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='profesion',
            field=models.CharField(max_length=200, verbose_name='PROFESION:', blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='rtn',
            field=models.CharField(help_text='Deje en Blanco NO registre...!', max_length=200, null=True, verbose_name='Interfase', blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='sexo',
            field=models.CharField(blank=True, max_length=1, verbose_name='SEXO:', choices=[(b'M', 'Masculino'), (b'F', 'Femenino')]),
        ),
        migrations.AlterField(
            model_name='persona',
            name='telefono',
            field=models.CharField(max_length=200, verbose_name='TELEFONO:', blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='tipo_identificacion',
            field=models.CharField(blank=True, max_length=1, choices=[(b'R', 'Documento de Identidad'), (b'L', 'Licencia'), (b'P', 'Pasaporte'), (b'T', 'Tarjeta de Identidad'), (b'N', 'Ninguno')]),
        ),
    ]
