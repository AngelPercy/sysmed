# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0022_auto_20151116_1125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estilovida',
            name='logoaudi_der_discrim',
        ),
        migrations.RemoveField(
            model_name='estilovida',
            name='logoaudi_der_ucmlc',
        ),
        migrations.RemoveField(
            model_name='estilovida',
            name='logoaudi_der_uducl',
        ),
        migrations.RemoveField(
            model_name='estilovida',
            name='logoaudi_der_umbral',
        ),
        migrations.RemoveField(
            model_name='estilovida',
            name='logoaudi_izq_discrim',
        ),
        migrations.RemoveField(
            model_name='estilovida',
            name='logoaudi_izq_ucmlc',
        ),
        migrations.RemoveField(
            model_name='estilovida',
            name='logoaudi_izq_uducl',
        ),
        migrations.RemoveField(
            model_name='estilovida',
            name='logoaudi_izq_umbral',
        ),
        migrations.RemoveField(
            model_name='fisico',
            name='altura',
        ),
        migrations.RemoveField(
            model_name='fisico',
            name='color_de_cabello',
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
            name='duplicado',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='fax',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='mostrar_en_cardex',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='rtn',
        ),
        migrations.AddField(
            model_name='estilovida',
            name='archivo',
            field=models.ImageField(help_text=b'El archivo debe estar en formato jpg o png y no pesar mas de 120kb', null=True, upload_to=b'persona/foto//%Y/%m/%d', blank=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='lugar_nac',
            field=models.CharField(max_length=200, null=True, verbose_name='LUGAR NACIMIENTO:', blank=True),
        ),
        migrations.AlterField(
            model_name='fisico',
            name='max_inspiracion',
            field=models.CharField(max_length=200, verbose_name='MAX INSPIRACION:', blank=True),
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
            name='establecimiento',
            field=models.CharField(max_length=200, verbose_name='ESTABLECIMIENTO:', blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='estado_civil',
            field=models.CharField(blank=True, max_length=1, verbose_name='ESTADO CIVIL:', choices=[(b'S', 'Soltero/a'), (b'D', 'Divorciado/a'), (b'C', 'Casado/a'), (b'U', 'Union Libre')]),
        ),
        migrations.AlterField(
            model_name='persona',
            name='examen_medico',
            field=models.CharField(blank=True, max_length=1, choices=[(b'O', 'PRE OCUPACIONAL'), (b'I', 'PERIDICO'), (b'E', 'RETIRO'), (b'U', 'POR CAMBIO DE PUESTO'), (b'A', 'POR REINCORPORACION')]),
        ),
        migrations.AlterField(
            model_name='persona',
            name='fecha_examen',
            field=models.DateField(default=datetime.date.today, verbose_name='FECHA DE EXAMEN:'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='identificacion',
            field=models.CharField(max_length=8, verbose_name='D.N.I:', blank=True),
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
            name='proyecto',
            field=models.CharField(max_length=200, verbose_name='PROYECTO:', blank=True),
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
    ]
