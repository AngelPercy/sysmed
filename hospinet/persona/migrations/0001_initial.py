# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import persona.fields
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AntecedenteQuirurgico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('procedimiento', models.CharField(max_length=200, blank=True)),
                ('fecha', models.CharField(max_length=200, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empleador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('nombre', models.CharField(max_length=200, blank=True)),
                ('direccion', models.TextField()),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Empleo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('numero_empleado', models.CharField(max_length=200, null=True, blank=True)),
                ('empleador', models.ForeignKey(related_name='empleos', blank=True, to='persona.Empleador', null=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_identificacion', models.CharField(blank=True, max_length=1, choices=[(b'R', 'Documento de Identidad'), (b'L', 'Licencia'), (b'P', 'Pasaporte'), (b'T', 'Tarjeta de Identidad'), (b'N', 'Ninguno')])),
                ('identificacion', models.CharField(max_length=8, verbose_name='D.N.I:', blank=True)),
                ('establecimiento', models.CharField(max_length=200, verbose_name='ESTABLECIMIENTO:', blank=True)),
                ('proyecto', models.CharField(max_length=200, verbose_name='PROYECTO:', blank=True)),
                ('fecha_examen', models.DateField(default=datetime.date.today, verbose_name='FECHA DE EXAMEN:')),
                ('nombre', models.CharField(max_length=50, verbose_name='NOMBRES:', blank=True)),
                ('apellido', models.CharField(max_length=50, verbose_name='APELLIDOS:', blank=True)),
                ('sexo', models.CharField(blank=True, max_length=1, verbose_name='SEXO:', choices=[(b'M', 'Masculino'), (b'F', 'Femenino')])),
                ('nacimiento', models.DateField(default=datetime.date.today, verbose_name='FECHA NACIMIENTO:')),
                ('lugar_nac', models.CharField(max_length=200, null=True, verbose_name='LUGAR NACIMIENTO:', blank=True)),
                ('estado_civil', models.CharField(blank=True, max_length=1, verbose_name='ESTADO CIVIL:', choices=[(b'S', 'Soltero/a'), (b'D', 'Divorciado/a'), (b'C', 'Casado/a'), (b'U', 'Union Libre')])),
                ('profesion', models.CharField(max_length=200, verbose_name='PROFESION:', blank=True)),
                ('telefono', models.CharField(max_length=200, verbose_name='TELEFONO:', blank=True)),
                ('celular', models.CharField(max_length=200, verbose_name='CELULAR:', blank=True)),
                ('domicilio', models.CharField(max_length=200, verbose_name='DOMICILIO:', blank=True)),
                ('email', models.CharField(max_length=200, verbose_name='E-MAIL:', blank=True)),
                ('fotografia', models.ImageField(help_text=b'El archivo debe estar en formato jpg o png y no pesar mas de 120kb', null=True, upload_to=b'persona/foto//%Y/%m/%d', blank=True)),
                ('nacionalidad', persona.fields.OrderedCountryField(blank=True, max_length=2)),
                ('duplicado', models.BooleanField(default=False)),
                ('rtn', models.CharField(help_text='Deje en Blanco NO registre...!', max_length=200, null=True, verbose_name='Interfase', blank=True)),
                ('examen_medico', models.CharField(blank=True, max_length=1, choices=[(b'O', 'PRE OCUPACIONAL'), (b'I', 'PERIDICO'), (b'E', 'RETIRO'), (b'U', 'POR CAMBIO DE PUESTO'), (b'A', 'POR REINCORPORACION')])),
                ('trabajo_realizar', models.CharField(blank=True, max_length=1, choices=[(b'0', 'CHOFER'), (b'1', 'TRABAJOS DE ALTURA'), (b'2', 'ADMINISTRATIVO'), (b'3', 'LABORATORIO'), (b'4', 'TRABAJO ESPACIO CONFINADO'), (b'5', 'MANTENIMIENTO LIMPIEZA')])),
                ('mostrar_en_cardex', models.BooleanField(default=False, verbose_name='Realizar Seguimiento')),
            ],
            options={
                'permissions': (('persona', 'Permite al usuario gestionar persona'),),
            },
        ),
        migrations.CreateModel(
            name='PuestoTrabajo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('puesto', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('lugar', models.CharField(max_length=200, blank=True)),
                ('direccion', models.TextField()),
                ('empleador', models.ForeignKey(related_name='sedes', blank=True, to='persona.Empleador', null=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Antecedente',
            fields=[
                ('persona', models.OneToOneField(primary_key=True, serialize=False, to='persona.Persona')),
                ('ruido', models.BooleanField(default=False, verbose_name='RUIDO')),
                ('polvo', models.BooleanField(default=False, verbose_name='POLVO')),
                ('vibracion', models.BooleanField(default=False, verbose_name='VIBRACION')),
                ('segmentaria', models.BooleanField(default=False, verbose_name='SEGMENTARIA')),
                ('vibracion_total', models.BooleanField(default=False, verbose_name='VIBRACION TOTAL')),
                ('cancerigeno', models.BooleanField(default=False, verbose_name='CANCERIGENO')),
                ('mutagenico', models.BooleanField(default=False, verbose_name='MUTAGENICOS')),
                ('metales', models.BooleanField(default=False, verbose_name='MENTALES')),
                ('pesados', models.BooleanField(default=False, verbose_name='PESADOS')),
                ('solvente', models.BooleanField(default=False, verbose_name='SOLVENTE')),
                ('temperatura', models.BooleanField(default=False, verbose_name='TEMPERATURA')),
                ('biologico', models.BooleanField(default=False, verbose_name='BIOLOGICO')),
                ('postura', models.BooleanField(default=False, verbose_name='POSTURA')),
                ('turno_noche', models.BooleanField(default=False, verbose_name='TURNOS NOCHE')),
                ('carga', models.BooleanField(default=False, verbose_name='CARGAS')),
                ('movimiento', models.BooleanField(default=False, verbose_name='MOVIMIENTO')),
                ('repetitivo', models.BooleanField(default=False, verbose_name='REPETITIVO')),
                ('otros_a', models.BooleanField(default=False, verbose_name='OTROS')),
                ('postula', models.CharField(max_length=200, verbose_name='PUESTO AL QUE POSTULA:', blank=True)),
                ('hta', models.BooleanField(default=False, verbose_name='HTA:')),
                ('dm', models.BooleanField(default=False, verbose_name='DM:')),
                ('asma', models.BooleanField(default=False, verbose_name='ASMA:')),
                ('ram', models.BooleanField(default=False, verbose_name='RAM:')),
                ('h_tg', models.BooleanField(default=False, verbose_name='H.Tg:')),
                ('h_col', models.BooleanField(default=False, verbose_name='H.Col:')),
                ('prob_cv', models.BooleanField(default=False, verbose_name='Prob.CV:')),
                ('alergias', models.CharField(max_length=200, null=True, blank=True)),
                ('artropatia', models.BooleanField(default=False, verbose_name='ARTROPATIA:')),
                ('pt_columna', models.BooleanField(default=False, verbose_name='PT.COLUMNA:')),
                ('hpb', models.BooleanField(default=False, verbose_name='HPB:')),
                ('migrana', models.BooleanField(default=False, verbose_name='MIGRA\xd1A:')),
                ('cirugia', models.BooleanField(default=False)),
                ('sd_metabolico', models.BooleanField(default=False, verbose_name='SD. METABOLICO:')),
                ('cancer', models.BooleanField(default=False, verbose_name='CANCER:')),
                ('problema_renal', models.BooleanField(default=False, verbose_name='PROBLEMA RENAL:')),
                ('medicacion_actual', models.CharField(max_length=200, null=True, verbose_name='MEDICACION ACTUAL:', blank=True)),
                ('tabaco', models.CharField(blank=True, max_length=1, verbose_name='HABITOS TABACO:', choices=[(b'N', 'NADA'), (b'P', 'POCO'), (b'H', 'HABITUAL'), (b'E', 'EXESIVO')])),
                ('coca', models.CharField(blank=True, max_length=1, verbose_name='HABITOS COCA:', choices=[(b'N', 'NADA'), (b'P', 'POCO'), (b'H', 'HABITUAL'), (b'E', 'EXESIVO')])),
                ('alcohol', models.CharField(blank=True, max_length=1, verbose_name='HABITOS ALCOHOL:', choices=[(b'N', 'NADA'), (b'P', 'POCO'), (b'H', 'HABITUAL'), (b'E', 'EXESIVO')])),
                ('otros_b', models.CharField(max_length=200, verbose_name='OBSERVACIONES:', blank=True)),
                ('ectoscopia', models.BooleanField(default=False, verbose_name='ECTOSCOPIA:')),
                ('abec', models.BooleanField(default=False, verbose_name='ABEC:')),
                ('abeh', models.BooleanField(default=False, verbose_name='ABEH:')),
                ('aben', models.BooleanField(default=False, verbose_name='ABEN:')),
                ('lotep', models.BooleanField(default=False, verbose_name='LOTEP:')),
                ('anormalidades', models.CharField(max_length=200, verbose_name='ANORMALIDADES:', blank=True)),
                ('desc_b', models.CharField(max_length=200, verbose_name='DESCRIPCION', blank=True)),
                ('boca_amigdalas', models.BooleanField(default=False, help_text='labios sin lesiones mucosa oral rosada brillante congestiva', verbose_name='BOCA AMIGDALAS, FARINGE, LARINGE')),
                ('anorma_a', models.BooleanField(default=False, verbose_name=b'ANORMALIDADES')),
                ('descr_c', models.CharField(max_length=200, verbose_name='DESCRIPCION', blank=True)),
                ('genitales_normal', models.BooleanField(default=False, verbose_name=b'GENITALES NORMALES')),
                ('genitales_anormal', models.BooleanField(default=False, verbose_name=b'GENITALES ANORMAL')),
                ('desc_d', models.CharField(max_length=200, verbose_name='DESCRIPCION', blank=True)),
                ('cuello_normal', models.BooleanField(default=False, verbose_name=' CUELLO NORMAL')),
                ('cuello_anormal', models.BooleanField(default=False, verbose_name='CUELLO ANORMAL')),
                ('desc_e', models.CharField(max_length=200, verbose_name='DESCRIPCION', blank=True)),
                ('nariz_normal', models.BooleanField(default=False, verbose_name='NARIZ NORMAL')),
                ('nariz_anormal', models.BooleanField(default=False, verbose_name='NARIZ ANORMAL')),
                ('desc_f', models.CharField(help_text='DENTADURA ODONTOGRAMA DE ACUERDO A MINSA', max_length=200, verbose_name='DESCRIPCION', blank=True)),
                ('edentulo_parcial', models.CharField(blank=True, max_length=1, verbose_name='EDENTULO PARCIAL', choices=[(b'0', 'SI'), (b'1', 'NO')])),
                ('edentulo_total', models.CharField(blank=True, max_length=1, verbose_name='EDENTULO TOTAL', choices=[(b'0', 'SI'), (b'1', 'NO')])),
                ('ppf', models.CharField(blank=True, max_length=1, verbose_name='PPF', choices=[(b'0', 'SI'), (b'1', 'NO')])),
                ('gingivitis', models.CharField(blank=True, max_length=1, verbose_name='GINGIVITIS', choices=[(b'0', 'SI'), (b'1', 'NO')])),
                ('ppr', models.CharField(blank=True, max_length=1, verbose_name='PPR', choices=[(b'0', 'SI'), (b'1', 'NO')])),
                ('piezas_mal_estado', models.CharField(max_length=200, verbose_name='PIEZAS EN MAL ESTADO', blank=True)),
                ('piezas_faltan', models.CharField(help_text='EXAMENES DE LOS OJOS', max_length=200, verbose_name='PIEZAS QUE FALTAN', blank=True)),
                ('v_c_o_d_sin_corregir', models.CharField(max_length=20, verbose_name='OJO DER. S/C Visi\xf3n de Cerca:', blank=True)),
                ('v_l_o_d_sin_corregir', models.CharField(max_length=20, verbose_name='OJO DER. S/C Visi\xf3n de Lejos:', blank=True)),
                ('v_c_o_i_sin_corregir', models.CharField(max_length=20, verbose_name='OJO IZQ. S/C Visi\xf3n de Cerca:', blank=True)),
                ('v_l_o_i_sin_corregir', models.CharField(max_length=20, verbose_name='OJO IZQ. S/C Visi\xf3n de Lejos:', blank=True)),
                ('v_c_o_d_corregida', models.CharField(max_length=20, verbose_name='OJO DER. CORREGIDA Visi\xf3n de Cerca:', blank=True)),
                ('v_l_o_d_corregida', models.CharField(max_length=20, verbose_name='OJO DER. CORREGIDA Visi\xf3n de Cerca:', blank=True)),
                ('v_c_o_i_corregida', models.CharField(max_length=20, verbose_name='OJO IZQ. CORREGIDA Visi\xf3n de Cerca:', blank=True)),
                ('v_l_o_i_corregida', models.CharField(max_length=20, verbose_name='OJO IZQ. CORREGIDA Visi\xf3n de Cerca:', blank=True)),
                ('vision_colores_normal', models.CharField(blank=True, max_length=1, verbose_name='VISION DE COLORES', choices=[(b'0', 'SI'), (b'1', 'NO')])),
                ('vision_colores_nistagnos', models.CharField(blank=True, max_length=1, verbose_name='VISION DE COLORES NISTAGNOS', choices=[(b'0', 'SI'), (b'1', 'NO')])),
                ('Enfermedad_ocular_descrip', models.CharField(max_length=200, verbose_name='ENF. OCULAR DESC.', blank=True)),
                ('sin_alteraciones', models.CharField(help_text='EXAMENES DE LOS OIDOS DERECHO E IZQUIERDO', max_length=200, verbose_name='SIN ALTERACIONES', blank=True)),
                ('t_d_triangulo_de_luz', models.CharField(blank=True, max_length=1, verbose_name='TIMPANO DER. TRIANGULO DE LUZ', choices=[(b'0', 'SI'), (b'1', 'NO')])),
                ('t_d_perforaciones', models.CharField(blank=True, max_length=1, verbose_name='TIMPANO DER. PERFORACIONES', choices=[(b'0', 'SI'), (b'1', 'NO')])),
                ('t_d_abombamiento', models.CharField(blank=True, max_length=1, verbose_name='TIMPANO DER. ABOMBAMIENTO', choices=[(b'0', 'SI'), (b'1', 'NO')])),
                ('t_d_tapon_cerumen', models.CharField(blank=True, max_length=1, verbose_name='TIMPANO DER. TAPON CERUMEN', choices=[(b'0', 'SI'), (b'1', 'NO')])),
                ('t_d_observaciones', models.CharField(max_length=100, verbose_name='TIMPANO DERECHO OBSERVACIONES', blank=True)),
                ('t_i_triangulo_de_luz', models.CharField(blank=True, max_length=1, verbose_name='TIMPANO IZQ. TRIANGULO DE LUZ', choices=[(b'0', 'SI'), (b'1', 'NO')])),
                ('t_i_perforaciones', models.CharField(blank=True, max_length=1, verbose_name='TIMPANO IZQ. PERFORACIONES', choices=[(b'0', 'SI'), (b'1', 'NO')])),
                ('t_i_abombamiento', models.CharField(blank=True, max_length=1, verbose_name='TIMPANO IZQ. ABOMBAMIENTO', choices=[(b'0', 'SI'), (b'1', 'NO')])),
                ('t_i_tapon_cerumen', models.CharField(blank=True, max_length=1, verbose_name='TIMPANO IZQ. TAPON CERUMEN', choices=[(b'0', 'SI'), (b'1', 'NO')])),
                ('t_i_observaciones', models.CharField(max_length=100, verbose_name='TIMPANO IZQUIERDO OBSERVACIONES', blank=True)),
                ('audicion_d_hz_500', models.CharField(max_length=20, verbose_name='AUD. DER. Hz 500', blank=True)),
                ('audicion_d_hz_1000', models.CharField(max_length=20, verbose_name='AUD. DER. Hz 1000', blank=True)),
                ('audicion_d_hz_2000', models.CharField(max_length=20, verbose_name='AUD. DER. Hz 2000', blank=True)),
                ('audicion_d_hz_3000', models.CharField(max_length=20, verbose_name='AUD. DER. Hz 3000', blank=True)),
                ('audicion_d_hz_4000', models.CharField(max_length=20, verbose_name='AUD. DER. Hz 4000', blank=True)),
                ('audicion_d_hz_6000', models.CharField(max_length=20, verbose_name='AUD. DER. Hz 6000', blank=True)),
                ('audicion_d_hz_8000', models.CharField(max_length=20, verbose_name='AUD. DER. Hz 8000', blank=True)),
                ('derecha_conservada', models.BooleanField(default=False, verbose_name='AUD. DER. CONSERVADA')),
                ('comentario', models.CharField(max_length=200, verbose_name='COMENTARIO', blank=True)),
                ('audicion_i_hz_500', models.CharField(max_length=20, verbose_name='AUD. IZQ. Hz 500', blank=True)),
                ('audicion_i_hz_1000', models.CharField(max_length=20, verbose_name='AUD. IZQ. Hz 1000', blank=True)),
                ('audicion_i_hz_2000', models.CharField(max_length=20, verbose_name='AUD. IZQ. Hz 2000', blank=True)),
                ('audicion_i_hz_3000', models.CharField(max_length=20, verbose_name='AUD. IZQ. Hz 3000', blank=True)),
                ('audicion_i_hz_4000', models.CharField(max_length=20, verbose_name='AUD. IZQ. Hz 4000', blank=True)),
                ('audicion_i_hz_6000', models.CharField(max_length=20, verbose_name='AUD. IZQ. Hz 6000', blank=True)),
                ('audicion_i_hz_8000', models.CharField(max_length=20, verbose_name='AUD. IZQ. Hz 8000', blank=True)),
                ('izquierdo_conservada', models.BooleanField(default=False, verbose_name='AUD. IZQ. CONSERVADA')),
                ('comentarios', models.CharField(help_text='EXAMENES DE TORAX ECTOSCOPIA', max_length=200, verbose_name='COMENTARIO', blank=True)),
                ('torax_ectoscopia_normal', models.BooleanField(default=False, verbose_name=b'ECTOSCOPIA NORMAL')),
                ('torax_ectoscopia_anormal', models.BooleanField(default=False, verbose_name=b'ANORMAL')),
                ('desc_g', models.CharField(max_length=200, verbose_name='DESCRIPCION', blank=True)),
                ('corazon_normal', models.BooleanField(default=False, verbose_name=b'CORAZON NORMAL')),
                ('corazon_anormal', models.BooleanField(default=False, verbose_name=b'ANORMAL')),
                ('desc_h', models.CharField(max_length=200, verbose_name='DESCRIPCION', blank=True)),
                ('pulmones_normal', models.BooleanField(default=False, verbose_name=b'PULMONES NORMAL')),
                ('pulmones_anormal', models.BooleanField(default=False, verbose_name=b'ANORMAL')),
                ('desc_i', models.CharField(max_length=200, verbose_name='DESCRIPCION', blank=True)),
                ('miembro_sup_der_normal', models.BooleanField(default=False, verbose_name='MIENBRO SUP. DERECHO NORMAL')),
                ('mienbro_sup_der_anormal', models.BooleanField(default=False, verbose_name='MIENBRO SUP. DERECHO ANORMAL')),
                ('desc_j', models.CharField(max_length=200, verbose_name='DESCRIPCION', blank=True)),
                ('miembro_sup_izq_normal', models.BooleanField(default=False, verbose_name='MIENBRO SUP. IZQUIERDO NORMAL')),
                ('miembro_sup_izq_anormal', models.BooleanField(default=False, verbose_name='MIENBRO SUP. IZQUIERDO ANORMAL')),
                ('desc_k', models.CharField(max_length=200, verbose_name='DESCRIPCION', blank=True)),
                ('miembro_infe_der_normal', models.BooleanField(default=False, verbose_name='MIENBRO INF. DERECHO NORMAL')),
                ('miembro_infe_der_anormal', models.BooleanField(default=False, verbose_name='MIENBRO INF. DERECHO ANORMAL')),
                ('miembro_infe_izq_normal', models.BooleanField(default=False, verbose_name='MIENBRO INF. IZQUIERDO NORMAL')),
                ('miembro_infe_izq_anormal', models.BooleanField(default=False, verbose_name='MIENBRO INF. IZQUIERDO ANORMAL')),
                ('desc_m', models.CharField(max_length=200, verbose_name='DESCRIPCION', blank=True)),
                ('presentes', models.BooleanField(default=False, verbose_name='PRESENTES')),
                ('normoreflexia', models.BooleanField(default=False, verbose_name='NORMOREFLEXIA')),
                ('hipereflexia', models.BooleanField(default=False, verbose_name='HIPEREFLEXIA')),
                ('marcha_conservada', models.CharField(max_length=200, verbose_name='MARCHA CONSERVADA', blank=True)),
                ('columna_vert_normal', models.BooleanField(default=False, verbose_name='COLUMNA VERTEBRAL NORMAL')),
                ('columna_vert_anormal', models.BooleanField(default=False, verbose_name='COLUMAN VERTEBRAL ANORMAL')),
                ('desc_n', models.CharField(max_length=200, verbose_name='DESCRIPCION', blank=True)),
                ('abdomen_normal', models.BooleanField(default=False, verbose_name='ABDOMEN NORMAL')),
                ('abdomen_anormal', models.BooleanField(default=False, verbose_name='ANORMALIDADES')),
                ('desc_l', models.CharField(max_length=200, verbose_name='DESCRIPCION', blank=True)),
                ('pru_sup_der', models.CharField(blank=True, max_length=1, verbose_name='PRU Sup Drch', choices=[(b'0', 'SI'), (b'1', 'NO')])),
                ('pru_sup_izq', models.CharField(blank=True, max_length=1, verbose_name='PRU Sup Izq.', choices=[(b'0', 'SI'), (b'1', 'NO')])),
                ('pru_med_der', models.CharField(blank=True, max_length=1, verbose_name='PRU Med Drch', choices=[(b'0', 'SI'), (b'1', 'NO')])),
                ('pru_med_izq', models.CharField(blank=True, max_length=1, verbose_name='PRU Med Izq', choices=[(b'0', 'SI'), (b'1', 'NO')])),
                ('prl_der', models.CharField(blank=True, max_length=1, verbose_name='PRL Drch', choices=[(b'0', 'SI'), (b'1', 'NO')])),
                ('prl_izq', models.CharField(blank=True, max_length=1, verbose_name='PRL Izq', choices=[(b'0', 'SI'), (b'1', 'NO')])),
                ('hernias', models.CharField(blank=True, max_length=1, verbose_name='HERNIAS', choices=[(b'0', 'SI'), (b'1', 'NO')])),
                ('varices', models.CharField(blank=True, max_length=1, verbose_name='VARICES', choices=[(b'0', 'SI'), (b'1', 'NO')])),
                ('funciones_superiores', models.BooleanField(default=False, verbose_name='FUNCIONES SUP. CONSERVADA')),
                ('psicologico', models.CharField(blank=True, max_length=1, verbose_name='PSICOLOGICO', choices=[(b'A', 'APTO'), (b'N', 'NO APTO')])),
            ],
        ),
        migrations.CreateModel(
            name='AntecedenteFamiliar',
            fields=[
                ('persona', models.OneToOneField(related_name='antecedente_familiar', primary_key=True, serialize=False, to='persona.Persona')),
                ('mama', models.CharField(max_length=200, verbose_name='MAMA:', blank=True)),
                ('papa', models.CharField(max_length=200, verbose_name='PAPA:', blank=True)),
                ('hermano', models.CharField(max_length=200, verbose_name='HERMANO:', blank=True)),
                ('sin_importancia', models.BooleanField(default=False, verbose_name='SIN IMPORTANCIA')),
                ('con_importancia', models.BooleanField(default=False, verbose_name='CON IMPORTANCIA')),
                ('vivos', models.BooleanField(default=False)),
                ('n_hijos', models.CharField(max_length=100, verbose_name='N\xb0 DE HIJOS:', blank=True)),
                ('otros', models.CharField(max_length=200, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AntecedenteObstetrico',
            fields=[
                ('persona', models.OneToOneField(related_name='antecedente_obstetrico', primary_key=True, serialize=False, to='persona.Persona')),
                ('menarca', models.DateField(default=datetime.date.today)),
                ('ultimo_periodo', models.DateField(null=True, blank=True)),
                ('gestas', models.IntegerField(default=0)),
                ('partos', models.IntegerField(default=0)),
                ('cesareas', models.IntegerField(default=0)),
                ('otros', models.CharField(max_length=200, blank=True)),
                ('displasia', models.BooleanField(default=False)),
                ('anticoncepcion', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='EstiloVida',
            fields=[
                ('persona', models.OneToOneField(related_name='estilo_vida', primary_key=True, serialize=False, to='persona.Persona')),
                ('fecha_examen', models.DateField(default=datetime.date.today, verbose_name='FECHA DE EXAMEN:')),
                ('empr', models.CharField(max_length=200, verbose_name='EMPRESA:', blank=True)),
                ('ocupacion', models.CharField(max_length=200, verbose_name='OCUPACION:', blank=True)),
                ('anos_trabajo', models.CharField(max_length=200, verbose_name='A\xd1OS DE TRABAJO:', blank=True)),
                ('tiempo_exposicion', models.CharField(max_length=200, verbose_name='TIEMPO DE EXPOSICION A RUIDO (8 HR):', blank=True)),
                ('apresiacion_ruido', models.CharField(blank=True, max_length=1, verbose_name='APRECIACION DEL RUIDO:', choices=[(b'I', 'MUY INTENSO'), (b'M', 'MODERADO'), (b'O', 'NO MOLESTO')])),
                ('audiometria_ante', models.CharField(max_length=200, verbose_name='AUDIOMETRIA ANTERIOR:', blank=True)),
                ('resul_audiomet', models.CharField(max_length=200, verbose_name='RESULTADOS DE AUDIOMETRIA:', blank=True)),
                ('antecedentes', models.CharField(max_length=200, verbose_name='ANTECEDENTES:', blank=True)),
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
                ('sistomatologia', models.CharField(max_length=200, verbose_name='SISTOMATOLOGIA', blank=True)),
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
                ('medico', models.CharField(max_length=200, verbose_name='MEDICO', blank=True)),
                ('concluciones', models.CharField(max_length=200, verbose_name='CONCLUCIONES', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fisico',
            fields=[
                ('persona', models.OneToOneField(primary_key=True, serialize=False, to='persona.Persona')),
                ('talla', models.DecimalField(null=True, verbose_name='TALLA:', max_digits=5, decimal_places=2)),
                ('peso', models.DecimalField(null=True, verbose_name='PESO:', max_digits=5, decimal_places=2)),
                ('imc', models.CharField(max_length=100, verbose_name='IMC:', blank=True)),
                ('fr', models.CharField(max_length=100, verbose_name='FR:', blank=True)),
                ('saturacion', models.CharField(max_length=30, verbose_name='So2:', blank=True)),
                ('max_inspiracion', models.CharField(max_length=200, verbose_name='MAX INSPIRACION:', blank=True)),
                ('expiracion_forzada', models.CharField(max_length=200, blank=True)),
                ('pas', models.CharField(max_length=100, verbose_name='PAS:', blank=True)),
                ('pad', models.CharField(max_length=100, verbose_name='PAD:', blank=True)),
                ('fc', models.CharField(max_length=100, verbose_name='FC:', blank=True)),
                ('temperatura', models.DecimalField(null=True, verbose_name='T\xb0 :', max_digits=8, decimal_places=2)),
                ('perime_torax', models.CharField(max_length=100, verbose_name='PER\xcdMETRO TOR\xc1XICO:', blank=True)),
                ('perime_cintura', models.CharField(max_length=100, verbose_name='PER\xcdMETRO CINTURA:', blank=True)),
                ('perime_cadera', models.CharField(max_length=100, verbose_name='PER\xcdMETRO CADERA:', blank=True)),
                ('icc', models.CharField(max_length=100, verbose_name='ICC:', blank=True)),
                ('otros', models.CharField(max_length=200, verbose_name='OTROS', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='empleo',
            name='persona',
            field=models.ForeignKey(related_name='empleos', to='persona.Persona'),
        ),
        migrations.AddField(
            model_name='empleo',
            name='sede',
            field=models.ForeignKey(related_name='empleos', blank=True, to='persona.Sede', null=True),
        ),
        migrations.AddField(
            model_name='antecedentequirurgico',
            name='persona',
            field=models.ForeignKey(related_name='antecedentes_quirurgicos', to='persona.Persona'),
        ),
    ]
