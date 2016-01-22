# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
        ('inventory', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Adjunto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('archivo', models.FileField(upload_to=b'examen/adjunto/%Y/%m/%d')),
                ('descripcion', models.CharField(max_length=255, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dicom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('archivo', models.FileField(upload_to=b'examen/dicom/%Y/%m/%d')),
                ('descripcion', models.CharField(max_length=255, blank=True)),
                ('convertido', models.BooleanField(default=False)),
                ('imagen', models.ImageField(upload_to=b'examen/dicom/imagen/%Y/%m/%d', blank=True)),
                ('uuid', django_extensions.db.fields.UUIDField(editable=False, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estudio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='EstudioProgramado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('remitio', models.CharField(max_length=200)),
                ('efectuado', models.NullBooleanField(default=False)),
                ('n_rx', models.CharField(max_length=100, verbose_name='N\xb0 RX:', blank=True)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('calidad', models.CharField(max_length=100, verbose_name='CALIDAD:', blank=True)),
                ('simbolo', models.CharField(max_length=100, verbose_name='SIMBOLOS:', blank=True)),
                ('campo_pulmonar', models.CharField(max_length=200, verbose_name='CAMPO PULMONAR', blank=True)),
                ('hilios', models.CharField(max_length=100, verbose_name='HILIOS:', blank=True)),
                ('mediastino', models.CharField(max_length=100, verbose_name='MEDIASTINO:', blank=True)),
                ('senos', models.CharField(max_length=100, verbose_name='SENOS:', blank=True)),
                ('silueta_cardiovascular', models.CharField(max_length=100, verbose_name='SILUETA CARDIOVASCULAR', blank=True)),
                ('conclu_radiograficas', models.CharField(max_length=100, verbose_name='CONCLUCIONES RADIOGRAFICAS', blank=True)),
                ('normal', models.CharField(blank=True, max_length=1, choices=[(b'1', 'NORMAL 0/0'), (b'2', 'NORMAL CERO'), (b'3', 'SIN NEUMOCONIOSIS')])),
                ('sospecha', models.CharField(blank=True, max_length=1, choices=[(b'4', 'SOSPECHA 1/O'), (b'5', 'SOSPECHA 1/0'), (b'6', 'IMG. RAD. EXPLOSION A POLVO')])),
                ('con_neumoconiosis', models.CharField(blank=True, max_length=1, choices=[(b'A', 'UNO 1/1'), (b'B', 'UNO 1/2'), (b'C', 'DOS 2/1'), (b'D', 'DOS 2/2'), (b'E', 'DOS 2/3'), (b'F', 'TRES 3/2'), (b'G', 'TRES 3/3'), (b'H', 'CUATRO A'), (b'I', 'CUATRO B'), (b'J', 'CUATRO C')])),
                ('persona', models.ForeignKey(related_name='estudios_progamados', to='persona.Persona')),
            ],
        ),
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(default=datetime.datetime.now)),
                ('uuid', django_extensions.db.fields.UUIDField(editable=False, blank=True)),
                ('remitio', models.CharField(max_length=200, null=True)),
                ('facturado', models.NullBooleanField(default=False)),
                ('persona', models.ForeignKey(related_name='examenes', to='persona.Persona')),
            ],
            options={
                'permissions': (('examen', 'Permite al usuario gestionar examenes'),),
            },
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.ImageField(upload_to=b'examen/imagen/%Y/%m/%d')),
                ('descripcion', models.CharField(max_length=255, blank=True)),
                ('examen', models.ForeignKey(related_name='imagenes', to='imaging.Examen')),
            ],
        ),
        migrations.CreateModel(
            name='Radiologo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('nombre', models.CharField(max_length=255, blank=True)),
                ('porcentaje', models.IntegerField(default=30)),
                ('item', models.ForeignKey(blank=True, to='inventory.ItemTemplate', null=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('nombre', models.CharField(max_length=255, blank=True)),
                ('porcentaje', models.IntegerField(default=10)),
                ('item', models.ForeignKey(blank=True, to='inventory.ItemTemplate', null=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='TipoExamen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('item', models.ForeignKey(blank=True, to='inventory.ItemTemplate', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='examen',
            name='radiologo',
            field=models.ForeignKey(related_name='examenes', to='imaging.Radiologo'),
        ),
        migrations.AddField(
            model_name='examen',
            name='tecnico',
            field=models.ForeignKey(related_name='examenes', blank=True, to='imaging.Tecnico', null=True),
        ),
        migrations.AddField(
            model_name='examen',
            name='tipo_de_examen',
            field=models.ForeignKey(related_name='examenes', to='imaging.TipoExamen'),
        ),
        migrations.AddField(
            model_name='examen',
            name='tipo_de_venta',
            field=models.ForeignKey(related_name='examenes', to='inventory.TipoVenta'),
        ),
        migrations.AddField(
            model_name='examen',
            name='usuario',
            field=models.ForeignKey(related_name='estudios_realizados', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='estudioprogramado',
            name='radiologo',
            field=models.ForeignKey(related_name='estudios', to='imaging.Radiologo'),
        ),
        migrations.AddField(
            model_name='estudioprogramado',
            name='tecnico',
            field=models.ForeignKey(related_name='estudios', blank=True, to='imaging.Tecnico', null=True),
        ),
        migrations.AddField(
            model_name='estudioprogramado',
            name='tipo_de_examen',
            field=models.ForeignKey(related_name='estudios_progamados', to='imaging.TipoExamen'),
        ),
        migrations.AddField(
            model_name='estudioprogramado',
            name='tipo_de_venta',
            field=models.ForeignKey(related_name='estudios', to='inventory.TipoVenta'),
        ),
        migrations.AddField(
            model_name='estudioprogramado',
            name='usuario',
            field=models.ForeignKey(related_name='estudios_programados', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='estudio',
            name='examen',
            field=models.ForeignKey(related_name='estudios', to='imaging.Examen'),
        ),
        migrations.AddField(
            model_name='estudio',
            name='tipo_de_examen',
            field=models.ForeignKey(related_name='estudios', to='imaging.TipoExamen'),
        ),
        migrations.AddField(
            model_name='dicom',
            name='examen',
            field=models.ForeignKey(related_name='dicoms', to='imaging.Examen'),
        ),
        migrations.AddField(
            model_name='adjunto',
            name='examen',
            field=models.ForeignKey(related_name='adjuntos', to='imaging.Examen'),
        ),
    ]
