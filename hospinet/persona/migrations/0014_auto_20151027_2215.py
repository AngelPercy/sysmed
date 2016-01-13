# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0013_persona_mostrar_en_cardex'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='examen_medico',
            field=models.CharField(blank=True, max_length=1, choices=[(b'O', 'Pre Ocupacional'), (b'I', 'Periodico'), (b'E', 'Retiro'), (b'U', 'Por cambio de puesto'), (b'A', 'Por reincorporacion')]),
        ),
        migrations.AddField(
            model_name='persona',
            name='trabajo_realizar',
            field=models.CharField(blank=True, max_length=1, choices=[(b'0', 'CHOFER'), (b'1', 'TRABAJOS DE ALTURA'), (b'2', 'ADMINISTRATIVO'), (b'3', 'LABORATORIO'), (b'4', 'TRABAJO ESPACIO CONFINADO'), (b'5', 'MANTENIMIENTO LIMPIEZA')]),
        ),
    ]
