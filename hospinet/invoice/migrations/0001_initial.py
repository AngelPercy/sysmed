# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import persona.fields
import django.utils.timezone
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
        ('persona', '0001_initial'),
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CierreTurno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('monto', models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)),
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
                ('monto', models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)),
                ('comprobante', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('discount', models.DecimalField(default=0, max_digits=7, decimal_places=2)),
                ('correlativo', models.IntegerField(default=0)),
                ('credito', models.BooleanField(default=False)),
                ('cerrado', models.BooleanField(default=False)),
                ('nulo', models.BooleanField(default=False)),
                ('emision', models.DateTimeField(default=django.utils.timezone.now)),
                ('cajero', models.ForeignKey(related_name='recibos', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('ciudad', models.ForeignKey(related_name='recibos', blank=True, to='users.Ciudad', null=True)),
                ('cliente', models.ForeignKey(related_name='recibos', to='persona.Persona')),
                ('tipo_de_venta', models.ForeignKey(blank=True, to='inventory.TipoVenta', null=True)),
            ],
            options={
                'permissions': (('cajero', 'Permite al usuario gestionar caja'),),
            },
        ),
        migrations.CreateModel(
            name='StatusPago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('nombre', models.CharField(max_length=255, blank=True)),
                ('reportable', models.BooleanField(default=True)),
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
                ('nombre', models.CharField(max_length=255, null=True, blank=True)),
                ('color', persona.fields.ColorField(default=b'', max_length=10)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='TurnoCaja',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('inicio', models.DateTimeField(null=True, blank=True)),
                ('fin', models.DateTimeField(null=True, blank=True)),
                ('apertura', models.DecimalField(default=0, max_digits=7, decimal_places=2)),
                ('finalizado', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(related_name='turno_caja', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('cantidad', models.IntegerField()),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('precio', models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)),
                ('impuesto', models.DecimalField(default=0, max_digits=7, decimal_places=2, blank=True)),
                ('descuento', models.IntegerField(default=0)),
                ('placas', models.IntegerField(default=0)),
                ('descontable', models.BooleanField(default=True)),
                ('discount', models.DecimalField(default=0, max_digits=7, decimal_places=2, blank=True)),
                ('tax', models.DecimalField(default=0, max_digits=7, decimal_places=2, blank=True)),
                ('total', models.DecimalField(default=0, max_digits=11, decimal_places=2, blank=True)),
                ('monto', models.DecimalField(null=True, max_digits=11, decimal_places=2, blank=True)),
                ('item', models.ForeignKey(related_name='ventas', blank=True, to='inventory.ItemTemplate', null=True)),
                ('recibo', models.ForeignKey(related_name='ventas', to='invoice.Recibo')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.AddField(
            model_name='pago',
            name='recibo',
            field=models.ForeignKey(related_name='pagos', to='invoice.Recibo'),
        ),
        migrations.AddField(
            model_name='pago',
            name='status',
            field=models.ForeignKey(related_name='pagos', blank=True, to='invoice.StatusPago', null=True),
        ),
        migrations.AddField(
            model_name='pago',
            name='tipo',
            field=models.ForeignKey(related_name='pagos', to='invoice.TipoPago'),
        ),
        migrations.AddField(
            model_name='cierreturno',
            name='pago',
            field=models.ForeignKey(related_name='cierres', to='invoice.TipoPago'),
        ),
        migrations.AddField(
            model_name='cierreturno',
            name='turno',
            field=models.ForeignKey(related_name='cierres', to='invoice.TurnoCaja'),
        ),
    ]
