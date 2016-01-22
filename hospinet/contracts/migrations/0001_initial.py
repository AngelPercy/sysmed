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
            name='Aseguradora',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('nombre', models.CharField(max_length=255, blank=True)),
                ('representante', models.CharField(default=b'', max_length=255, blank=True)),
                ('cardex', models.ForeignKey(related_name='cardex', blank=True, to='persona.Persona', null=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Autorizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('imagen', models.FileField(upload_to=b'contracts/autorizaciones/%Y/%m/%d')),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('vigente', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Beneficiario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('inscripcion', models.DateTimeField(default=django.utils.timezone.now)),
                ('activo', models.BooleanField(default=True)),
                ('dependiente', models.IntegerField(default=0)),
                ('exclusion', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Beneficio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('nombre', models.CharField(max_length=255, null=True, blank=True)),
                ('descuento', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('observacion', models.CharField(max_length=255, null=True, blank=True)),
                ('activo', models.BooleanField(default=True)),
                ('limite', models.IntegerField(default=0, verbose_name='L\xedmite de Eventos')),
                ('descuento_post_limite', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('aplicar_a_suspendidos', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Cancelacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('motivo', models.TextField()),
                ('pago', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('numero', models.CharField(default=b'', max_length=255, blank=True)),
                ('inicio', models.DateField()),
                ('vencimiento', models.DateField()),
                ('ultimo_pago', models.DateTimeField(default=django.utils.timezone.now)),
                ('renovacion', models.DateField(null=True, blank=True)),
                ('cancelado', models.BooleanField(default=False)),
                ('poliza', models.CharField(default=b'', max_length=255, blank=True)),
                ('certificado', models.IntegerField(default=0)),
                ('titular', models.IntegerField(default=0)),
                ('suspendido', models.BooleanField(default=False)),
                ('exclusion', models.TextField(blank=True)),
                ('administradores', models.ManyToManyField(related_name='contratos', to=settings.AUTH_USER_MODEL, blank=True)),
                ('empresa', models.ForeignKey(related_name='contratos', blank=True, to='persona.Empleador', null=True)),
            ],
            options={
                'permissions': (('contrato', 'Permite al usuario gestionar contratos'),),
            },
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('adjunto', models.FileField(null=True, upload_to=b'evento/%Y/%m/%d', blank=True)),
                ('precio', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('contrato', models.ForeignKey(related_name='eventos', to='contracts.Contrato')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='ImportFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('archivo', models.FileField(upload_to=b'contracts/import/%Y/%m/%d')),
                ('processed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='LimiteEvento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('cantidad', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='MasterContract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('inicio', models.DateField(default=django.utils.timezone.now)),
                ('vencimiento', models.DateField(default=django.utils.timezone.now)),
                ('poliza', models.CharField(max_length=255, null=True, blank=True)),
                ('adicionales', models.IntegerField(default=0)),
                ('comision', models.IntegerField(default=0)),
                ('processed', models.BooleanField(default=False)),
                ('aseguradora', models.ForeignKey(related_name='master_contracts', to='contracts.Aseguradora')),
                ('contratante', models.ForeignKey(related_name='master_contracts', blank=True, to='persona.Empleador', null=True)),
                ('item', models.ForeignKey(blank=True, to='inventory.ItemTemplate', null=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Meta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('contratos', models.IntegerField()),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='MetodoPago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('precio', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('facturar', models.BooleanField(default=False)),
                ('ciclo', models.BooleanField(default=False)),
                ('contrato', models.ForeignKey(related_name='pagos', to='contracts.Contrato')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='PCD',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('numero', models.CharField(unique=True, max_length=255)),
                ('pc', models.IntegerField(default=0)),
                ('persona', models.ForeignKey(related_name='pcds', to='persona.Persona')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('nombre', models.CharField(max_length=255, null=True, blank=True)),
                ('precio', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('edad_maxima', models.IntegerField()),
                ('consulta', models.ForeignKey(related_name='plan', blank=True, to='inventory.ItemTemplate', null=True)),
                ('item', models.ForeignKey(related_name='planes_precio', blank=True, to='inventory.ItemTemplate', null=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Prebeneficiario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('persona', models.ForeignKey(related_name='prebeneficiarios', to='persona.Persona')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Precontrato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('completado', models.BooleanField(default=False)),
                ('de_acuerdo', models.BooleanField(default=True)),
                ('metodo_de_pago', models.ForeignKey(related_name='precontratos', blank=True, to='contracts.MetodoPago', null=True)),
                ('persona', models.ForeignKey(related_name='precontratos', to='persona.Persona')),
                ('plan', models.ForeignKey(related_name='precontratos', blank=True, to='contracts.Plan', null=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='TipoEvento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('nombre', models.CharField(max_length=255, null=True, blank=True)),
                ('tipo_items', models.ForeignKey(related_name='tipo_eventos', blank=True, to='inventory.ItemType', null=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='TipoPago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('item', models.ForeignKey(related_name='tipos_pago', to='inventory.ItemTemplate')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('habilitado', models.BooleanField(default=True)),
                ('usuario', models.ForeignKey(related_name='vendedores', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.AddField(
            model_name='prebeneficiario',
            name='precontrato',
            field=models.ForeignKey(related_name='prebeneficiarios', to='contracts.Precontrato'),
        ),
        migrations.AddField(
            model_name='pago',
            name='tipo_de_pago',
            field=models.ForeignKey(related_name='pagos', to='contracts.TipoPago', null=True),
        ),
        migrations.AddField(
            model_name='mastercontract',
            name='plan',
            field=models.ForeignKey(related_name='master_contracts', to='contracts.Plan'),
        ),
        migrations.AddField(
            model_name='mastercontract',
            name='vendedor',
            field=models.ForeignKey(related_name='master_contracts', to='contracts.Vendedor'),
        ),
        migrations.AddField(
            model_name='limiteevento',
            name='plan',
            field=models.ForeignKey(related_name='limites', to='contracts.Plan'),
        ),
        migrations.AddField(
            model_name='limiteevento',
            name='tipo_evento',
            field=models.ForeignKey(related_name='limites', to='contracts.TipoEvento'),
        ),
        migrations.AddField(
            model_name='evento',
            name='tipo',
            field=models.ForeignKey(related_name='eventos', to='contracts.TipoEvento'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='master',
            field=models.ForeignKey(related_name='contratos', verbose_name=b'Contrato', blank=True, to='contracts.MasterContract', null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='persona',
            field=models.ForeignKey(related_name='contratos', to='persona.Persona'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='plan',
            field=models.ForeignKey(related_name='contratos', to='contracts.Plan'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='vendedor',
            field=models.ForeignKey(related_name='contratos', to='contracts.Vendedor'),
        ),
        migrations.AddField(
            model_name='cancelacion',
            name='contrato',
            field=models.ForeignKey(related_name='cancelaciones', to='contracts.Contrato'),
        ),
        migrations.AddField(
            model_name='beneficio',
            name='plan',
            field=models.ForeignKey(related_name='beneficios', to='contracts.Plan'),
        ),
        migrations.AddField(
            model_name='beneficio',
            name='tipo_items',
            field=models.ForeignKey(related_name='beneficios', blank=True, to='inventory.ItemType', null=True),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='contrato',
            field=models.ForeignKey(related_name='beneficiarios', to='contracts.Contrato'),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='persona',
            field=models.ForeignKey(related_name='beneficiarios', to='persona.Persona'),
        ),
    ]
