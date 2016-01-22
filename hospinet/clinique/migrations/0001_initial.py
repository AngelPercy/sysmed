# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
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
            name='Afeccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('codigo', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50, null=True, blank=True)),
                ('habilitado', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('cantidad', models.IntegerField(default=1)),
                ('facturado', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now, null=True, blank=True)),
                ('ausente', models.BooleanField(default=False)),
                ('atendida', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('motivo_de_consulta', models.TextField(default=None, null=True)),
                ('HEA', models.TextField(default=None, null=True)),
                ('facturada', models.BooleanField(default=False)),
                ('activa', models.BooleanField(default=True)),
                ('final', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Consultorio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('nombre', models.CharField(max_length=50, null=True, blank=True)),
                ('activo', models.BooleanField(default=True)),
                ('administradores', models.ManyToManyField(related_name='consultorios_administrados', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'ordering': ['nombre'],
                'permissions': (('consultorio', 'Permite al usuario gestionar consultorios'),),
            },
        ),
        migrations.CreateModel(
            name='DiagnosticoClinico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('diagnostico', models.TextField(null=True, blank=True)),
                ('afeccion', models.ForeignKey(related_name='diagnosticos_clinicos', blank=True, to='clinique.Afeccion', null=True)),
                ('consulta', models.ForeignKey(related_name='diagnosticos_clinicos', blank=True, to='clinique.Consulta', null=True)),
                ('persona', models.ForeignKey(related_name='diagnosticos_clinicos', blank=True, to='persona.Persona', null=True)),
                ('usuario', models.ForeignKey(related_name='diagnosticos_clinicos', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('nombre', models.CharField(max_length=50)),
                ('habilitado', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Espera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('atendido', models.BooleanField(default=False)),
                ('ausente', models.BooleanField(default=False)),
                ('consulta', models.BooleanField(default=False)),
                ('inicio', models.DateTimeField(auto_now_add=True)),
                ('terminada', models.BooleanField(default=False)),
                ('fin', models.DateTimeField(auto_now_add=True)),
                ('consultorio', models.ForeignKey(related_name='espera', blank=True, to='clinique.Consultorio', null=True)),
                ('persona', models.ForeignKey(related_name='espera', to='persona.Persona')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('orl', models.TextField()),
                ('cardiopulmonar', models.TextField()),
                ('gastrointestinal', models.TextField()),
                ('extremidades', models.TextField()),
                ('otras', models.TextField()),
                ('consulta', models.ForeignKey(related_name='evaluaciones', blank=True, to='clinique.Consulta', null=True)),
                ('persona', models.ForeignKey(related_name='evaluaciones', blank=True, to='persona.Persona', null=True)),
                ('usuario', models.ForeignKey(related_name='evaluaciones', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('descripcion', models.TextField(blank=True)),
                ('adjunto', models.FileField(upload_to=b'clinique/examen/%Y/%m/%d')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Incapacidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('descripcion', models.TextField()),
                ('dias', models.IntegerField(default=0)),
                ('consulta', models.ForeignKey(related_name='incapacidades', blank=True, to='clinique.Consulta', null=True)),
                ('persona', models.ForeignKey(related_name='incapacidades', blank=True, to='persona.Persona', null=True)),
                ('usuario', models.ForeignKey(related_name='incapacidades', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='LecturaSignos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('pulso', models.IntegerField()),
                ('temperatura', models.DecimalField(null=True, max_digits=8, decimal_places=2)),
                ('presion_sistolica', models.IntegerField(null=True)),
                ('presion_diastolica', models.IntegerField(null=True)),
                ('respiracion', models.IntegerField(null=True)),
                ('presion_arterial_media', models.CharField(max_length=200, blank=True)),
                ('persona', models.ForeignKey(related_name='lecturas_signos', to='persona.Persona', null=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('nombre', models.CharField(max_length=50, null=True, blank=True)),
                ('habilitado', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='NotaEnfermeria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('nota', models.TextField(blank=True)),
                ('persona', models.ForeignKey(related_name='notas_enfermeria', blank=True, to='persona.Persona', null=True)),
                ('usuario', models.ForeignKey(related_name='consultorio_notas_enfermeria', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='OrdenMedica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('evolucion', models.TextField(blank=True)),
                ('orden', models.TextField(blank=True)),
                ('farmacia', models.BooleanField(default=False)),
                ('facturada', models.BooleanField(default=False)),
                ('consulta', models.ForeignKey(related_name='ordenes_medicas', blank=True, to='clinique.Consulta', null=True)),
                ('medicamento', models.ForeignKey(related_name='ordenes_medicas', blank=True, to='inventory.ItemTemplate', null=True)),
                ('persona', models.ForeignKey(related_name='ordenes_medicas', blank=True, to='persona.Persona', null=True)),
                ('usuario', models.ForeignKey(related_name='ordenes_clinicas', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('consultorio', models.ForeignKey(related_name='pacientes', blank=True, to='clinique.Consultorio', null=True)),
                ('persona', models.ForeignKey(related_name='pacientes', to='persona.Persona')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Prescripcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('nota', models.TextField(verbose_name='Otros MEdicamentos', blank=True)),
                ('consulta', models.ForeignKey(related_name='prescripciones', blank=True, to='clinique.Consulta', null=True)),
                ('medicamento', models.ForeignKey(related_name='prescripciones', blank=True, to='inventory.ItemTemplate', null=True)),
                ('persona', models.ForeignKey(related_name='prescripciones', blank=True, to='persona.Persona', null=True)),
                ('usuario', models.ForeignKey(related_name='prescripciones', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Remision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('motivo', models.TextField()),
                ('consultorio', models.ForeignKey(related_name='remisiones', to='clinique.Consultorio')),
                ('especialidad', models.ForeignKey(related_name='remisiones', blank=True, to='clinique.Especialidad', null=True)),
                ('persona', models.ForeignKey(related_name='remisiones', to='persona.Persona')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('archivo', models.FileField(upload_to=b'consultorio/reports/%Y/%m/%d')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now, null=True, blank=True)),
                ('consultorio', models.ForeignKey(related_name='reportes', blank=True, to='clinique.Consultorio', null=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Seguimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('observaciones', models.TextField()),
                ('consultorio', models.ForeignKey(related_name='seguimientos', blank=True, to='clinique.Consultorio', null=True)),
                ('persona', models.ForeignKey(related_name='seguimientos', blank=True, to='persona.Persona', null=True)),
                ('usuario', models.ForeignKey(related_name='seguimientos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='TipoCargo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('nombre', models.CharField(max_length=200, blank=True)),
                ('descontable', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='TipoConsulta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=50)),
                ('habilitado', models.BooleanField(default=True)),
                ('facturable', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoRemision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.AddField(
            model_name='remision',
            name='tipo',
            field=models.ForeignKey(related_name='remisiones', to='clinique.TipoRemision'),
        ),
        migrations.AddField(
            model_name='examen',
            name='paciente',
            field=models.ForeignKey(related_name='consultorio_examenes', to='clinique.Paciente'),
        ),
        migrations.AddField(
            model_name='consultorio',
            name='especialidad',
            field=models.ForeignKey(related_name='consultorios', blank=True, to='clinique.Especialidad', null=True),
        ),
        migrations.AddField(
            model_name='consultorio',
            name='inventario',
            field=models.ForeignKey(related_name='consultorios', blank=True, to='inventory.Inventario', null=True),
        ),
        migrations.AddField(
            model_name='consultorio',
            name='localidad',
            field=models.ForeignKey(related_name='consultorios', blank=True, to='clinique.Localidad', null=True),
        ),
        migrations.AddField(
            model_name='consultorio',
            name='secretaria',
            field=models.ForeignKey(related_name='secretarias', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='consultorio',
            name='usuario',
            field=models.ForeignKey(related_name='consultorios', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='consulta',
            name='consultorio',
            field=models.ForeignKey(related_name='consultas', blank=True, to='clinique.Consultorio', null=True),
        ),
        migrations.AddField(
            model_name='consulta',
            name='persona',
            field=models.ForeignKey(related_name='consultas', blank=True, to='persona.Persona', null=True),
        ),
        migrations.AddField(
            model_name='consulta',
            name='tipo',
            field=models.ForeignKey(related_name='consultas', to='clinique.TipoConsulta'),
        ),
        migrations.AddField(
            model_name='cita',
            name='consultorio',
            field=models.ForeignKey(related_name='citas', blank=True, to='clinique.Consultorio', null=True),
        ),
        migrations.AddField(
            model_name='cita',
            name='persona',
            field=models.ForeignKey(related_name='citas', blank=True, to='persona.Persona', null=True),
        ),
        migrations.AddField(
            model_name='cargo',
            name='consulta',
            field=models.ForeignKey(related_name='cargos', blank=True, to='clinique.Consulta', null=True),
        ),
        migrations.AddField(
            model_name='cargo',
            name='item',
            field=models.ForeignKey(related_name='consultorio_cargos', to='inventory.ItemTemplate'),
        ),
        migrations.AddField(
            model_name='cargo',
            name='tipo',
            field=models.ForeignKey(related_name='cargos', to='inventory.ItemType'),
        ),
        migrations.AddField(
            model_name='cargo',
            name='usuario',
            field=models.ForeignKey(related_name='cargos_clinicos', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
