# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal
import django.utils.timezone
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('ingresada', models.BooleanField(default=False)),
                ('proveedor', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Historial',
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
            name='Inventario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lugar', models.CharField(default=b'Bodega', max_length=255)),
                ('puede_comprar', models.NullBooleanField(default=False)),
            ],
            options={
                'permissions': (('inventario', 'Permite al usuario gestionar inventario'),),
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('vencimiento', models.DateTimeField(default=django.utils.timezone.now)),
                ('cantidad', models.IntegerField(default=0)),
                ('inventario', models.ForeignKey(related_name='items', to='inventory.Inventario')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='ItemAction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('action', models.TextField()),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='ItemComprado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('ingresado', models.BooleanField(default=False)),
                ('cantidad', models.IntegerField(default=0)),
                ('compra', models.ForeignKey(related_name='items', to='inventory.Compra')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='ItemHistorial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('cantidad', models.IntegerField(default=0)),
                ('historial', models.ForeignKey(related_name='items', to='inventory.Historial')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='ItemRequisicion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('cantidad', models.IntegerField()),
                ('entregada', models.BooleanField(default=False)),
                ('pendiente', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='ItemTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('descripcion', models.CharField(max_length=255)),
                ('marca', models.CharField(max_length=32, null=True, blank=True)),
                ('modelo', models.CharField(max_length=32, null=True, blank=True)),
                ('notas', models.TextField(null=True, blank=True)),
                ('precio_de_venta', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('costo', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('unidad_de_medida', models.CharField(max_length=32, null=True, blank=True)),
                ('impuestos', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('activo', models.BooleanField(default=True)),
                ('comision', models.DecimalField(default=Decimal('30.00'), max_digits=4, decimal_places=2)),
                ('comision2', models.DecimalField(default=Decimal('10.00'), max_digits=4, decimal_places=2)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='ItemType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('nombre', models.CharField(max_length=255)),
                ('consulta', models.BooleanField(default=True, verbose_name=b'Aparece en Cargos de Consulta')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='descripci\xf3n')),
            ],
        ),
        migrations.CreateModel(
            name='Requisicion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('aprobada', models.NullBooleanField(default=False)),
                ('entregada', models.NullBooleanField(default=False)),
                ('inventario', models.ForeignKey(related_name='requisiciones', blank=True, to='inventory.Inventario', null=True)),
                ('usuario', models.ForeignKey(related_name='requisiciones', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='TipoVenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('descripcion', models.CharField(max_length=255, null=True, blank=True)),
                ('incremento', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('disminucion', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Transferencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('aplicada', models.NullBooleanField(default=False)),
                ('destino', models.ForeignKey(related_name='entradas', blank=True, to='inventory.Inventario', null=True)),
                ('origen', models.ForeignKey(related_name='salidas', blank=True, to='inventory.Inventario', null=True)),
                ('requisicion', models.ForeignKey(related_name='transferencias', blank=True, to='inventory.Requisicion', null=True)),
                ('usuario', models.ForeignKey(related_name='transferencias', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Transferido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('cantidad', models.IntegerField()),
                ('aplicada', models.BooleanField(default=False)),
                ('item', models.ForeignKey(related_name='transferidos', to='inventory.ItemTemplate')),
                ('transferencia', models.ForeignKey(related_name='transferidos', to='inventory.Transferencia')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.AddField(
            model_name='itemtemplate',
            name='item_type',
            field=models.ManyToManyField(related_name='items', to='inventory.ItemType', blank=True),
        ),
        migrations.AddField(
            model_name='itemtemplate',
            name='suppliers',
            field=models.ManyToManyField(related_name='plantillas', to='inventory.Proveedor', blank=True),
        ),
        migrations.AddField(
            model_name='itemrequisicion',
            name='item',
            field=models.ForeignKey(related_name='requisiciones', to='inventory.ItemTemplate'),
        ),
        migrations.AddField(
            model_name='itemrequisicion',
            name='requisicion',
            field=models.ForeignKey(related_name='items', to='inventory.Requisicion'),
        ),
        migrations.AddField(
            model_name='itemhistorial',
            name='item',
            field=models.ForeignKey(related_name='historicos', to='inventory.ItemTemplate'),
        ),
        migrations.AddField(
            model_name='itemcomprado',
            name='item',
            field=models.ForeignKey(related_name='comprado', blank=True, to='inventory.ItemTemplate', null=True),
        ),
        migrations.AddField(
            model_name='itemaction',
            name='item',
            field=models.ForeignKey(related_name='acciones', to='inventory.ItemTemplate'),
        ),
        migrations.AddField(
            model_name='itemaction',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='item',
            name='plantilla',
            field=models.ForeignKey(related_name='items', verbose_name=b'Item', to='inventory.ItemTemplate'),
        ),
        migrations.AddField(
            model_name='historial',
            name='inventario',
            field=models.ForeignKey(related_name='historiales', to='inventory.Inventario'),
        ),
        migrations.AddField(
            model_name='compra',
            name='inventario',
            field=models.ForeignKey(related_name='compras', blank=True, to='inventory.Inventario', null=True),
        ),
    ]
