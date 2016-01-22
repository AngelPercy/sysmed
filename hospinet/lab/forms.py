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

from crispy_forms.layout import Fieldset
from lab.models import Resultado
from persona.forms import BasePersonaForm
from django import forms


class ResultadoForm(BasePersonaForm):
    class Meta:
        model = Resultado
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ResultadoForm, self).__init__(*args, **kwargs)
        self.helper.layout = Fieldset(u'Agregar Resultado de Laboratorio',
                                      *self.field_names)


class ResultadoEditForm(BasePersonaForm):

    archivo = forms.ImageField(required = False)

    class Meta:
        model = Resultado
        exclude = ('archivo',)
   #      widgets = {
			# 'archivo' : forms.ImageField(attrs={
			# 		'require' : False
			# 	})
			# }


    # def __init__(self, *args, **kwargs):
    #     super(ResultadoEditForm, self).__init__(*args, **kwargs)
    #     self.helper.layout = Fieldset(u'Agregar Resultado de Laboratorio',
    #                                   *self.field_names)

    # def clean(self):
    # 	print "asdasd"
    # 	print self.form.cleaned_data
