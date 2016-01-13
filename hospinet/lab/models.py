# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 Carlos Flores <cafg10@gmail.com>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library. If not, see <http://www.gnu.org/licenses/>.
from django.db import models
from django_extensions.db.models import TimeStampedModel
from persona.models import Persona, transfer_object_to_persona, \
    persona_consolidation_functions


class Resultado(TimeStampedModel):
    """Permite registrar los :class:`Resultado`s de un examen de laboratorio"""

    class Meta:
        permissions = (
            ('lab', 'Permite al usuario administrar laboratorios'),
        )
    
    TIPOS_SANGRE = (
        ('A', u'A'),
        ('B', u'B'),
        ('AB', u'AB'),
        ('O', u'O'),
    )

    FACTOR_RH = (
        ('+', u'+'),
        ('-', u'-'),
    )


    persona = models.ForeignKey(Persona, related_name='resultados')
    descripcion = models.TextField()
    archivo = models.FileField(upload_to='lab/results/%Y/%m/%d')
    grupo_sanguineo = models.CharField(max_length=100, choices=TIPOS_SANGRE, blank=True, verbose_name=u'GRUPO SANGUINEO:')
    factor = models.CharField(max_length=100, choices=FACTOR_RH, blank=True, verbose_name=u'FACTOR:')
    hemoglobina = models.DecimalField(decimal_places=2, max_digits=8,
                                      null=True, verbose_name=u'HEMOGLOBINA:')
    hematocrito = models.DecimalField(decimal_places=2, max_digits=8,
                                      null=True, verbose_name=u'HEMATOCRITO:')
    reaccion_serologicas = models.CharField(max_length=100, blank=True, verbose_name=u'REACCION SEROLOGICAS:')
    orina = models.CharField(max_length=100, blank=True, verbose_name=u'ORINA:')
    serie_blanca = models.CharField(max_length=100, blank=True, verbose_name=u'SERIE BLANCA:')
    serie_roja = models.CharField(max_length=100, blank=True, verbose_name=u'SERIE ROJA:')
    col_total = models.CharField(max_length=100, blank=True, verbose_name=u'COL TOTAL:')
    hdl = models.DecimalField(decimal_places=2, max_digits=8,
                                      null=True, verbose_name=u'HDL:', help_text=u'VAL. NORMALES (35 - 55 MG %)')
    ldl = models.DecimalField(decimal_places=2, max_digits=8,
                                      null=True, verbose_name=u'LDL:', help_text=u'VAL. NORMALES (< 130 MG %)')
    vldl = models.DecimalField(decimal_places=2, max_digits=8,
                                      null=True, verbose_name=u'VLDL')
    trigliceridos = models.CharField(max_length=100, blank=True, verbose_name=u'TRIGLICERIDOS:', help_text=u'VAL. NORMALES (MENOR DE 200 MG %)')
    glucosa = models.CharField(max_length=100, blank=True, verbose_name=u'GLUCOSA:',help_text=u'VAL. NORMALES (70 - 110 MG % METOD)')
    tgp = models.CharField(max_length=100, blank=True, verbose_name=u'TGP:', help_text=u'VAL. NORMALES HOMBRES < 41 U/LT')
    tgo = models.CharField(max_length=100, blank=True, verbose_name=u'TGO:', help_text=u'VAL. NORMALES HOMBRES < 38 U/LT')
    creatinina = models.CharField(max_length=100, blank=True, verbose_name=u'CREATININA:', help_text=u'VAL. NORMALES HOMBRES 0.7 - 1')

    def get_absolute_url(self):
        """Obtiene la direccion que se utilizará para redireccionar luego de
        o editar un :class:`Resultado`"""

        return self.persona.get_absolute_url()


def consolidate_contracts(persona, clone):
    [transfer_object_to_persona(resultado, persona) for resultado in
     clone.resultados.all()]


persona_consolidation_functions.append(consolidate_contracts)
