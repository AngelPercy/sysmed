# -*- coding: utf-8 -*-
#
# Copyright (C) 2011-2013 Carlos Flores <cafg10@gmail.com>
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

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Fieldset
from django.utils import timezone

from persona.models import (Persona, Fisico, EstiloVida, Antecedente,
                            AntecedenteFamiliar, AntecedenteObstetrico,
                            AntecedenteQuirurgico, Empleador, Empleo)


class FieldSetFormMixin(forms.Form):
    def __init__(self, *args, **kwargs):
        super(FieldSetFormMixin, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.html5_required = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-4'
        self.helper.field_class = 'col-md-7'
        self.field_names = self.fields.keys()


class FieldSetModelFormMixinNoButton(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FieldSetModelFormMixinNoButton, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.html5_required = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-4'
        self.helper.field_class = 'col-md-7'
        self.field_names = self.fields.keys()


class FieldSetModelFormMixin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FieldSetModelFormMixin, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.html5_required = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-4'
        self.helper.field_class = 'col-md-7'
        self.field_names = self.fields.keys()
        self.helper.add_input(Submit('submit', u'Guardar'))


class DateWidget(forms.DateInput):
    """Permite mostrar un input preparado para fecha y hora utilizando
    JQuery UI DatePicker"""

    def __init__(self, attrs=None):
        super(DateWidget, self).__init__(attrs)
        if attrs is not None:
            self.attrs = attrs.copy()
        else:
            self.attrs = {'class': 'datepicker'}

        if not 'format' in self.attrs:
            self.attrs['format'] = '%d/%m/%Y'


class FutureDateWidget(forms.DateInput):
    """Permite mostrar un input preparado para fecha y hora utilizando
    JQuery UI DatePicker"""

    def __init__(self, attrs=None):
        super(FutureDateWidget, self).__init__(attrs)
        if attrs is not None:
            self.attrs = attrs.copy()
        else:
            self.attrs = {'class': 'future-datepicker'}

        if not 'format' in self.attrs:
            self.attrs['format'] = '%d/%m/%Y'


class DateTimeWidget(forms.DateTimeInput):
    """Permite mostrar un input preparado para fecha y hora utilizando
    JQuery UI DateTimePicker"""

    class Media:
        js = ('js/jquery-ui-timepicker.js',)

    def __init__(self, attrs=None):
        super(DateTimeWidget, self).__init__(attrs)
        if attrs is not None:
            self.attrs = attrs.copy()
        else:
            self.attrs = {'class': 'datetimepicker'}

        if 'format' not in self.attrs:
            self.attrs['format'] = '%d/%m/%Y %H:%M'


class PersonaForm(FieldSetModelFormMixin):
    """Permite mostrar una interfaz para capturar los datos de una
    :class:`Persona`"""

    class Meta:
        model = Persona
        exclude = ('duplicado',)

    class Media:
        js = ('js/jquery.validate.min.js', 'js/persona.validator.js',)

    nacimiento = forms.DateField(widget=DateWidget(), required=False,
                                 initial=timezone.now)
    domicilio = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        self.helper.layout = Fieldset(u'Agregar Persona', *self.field_names)
        self.helper.form_id = "persona_form"


class BasePersonaForm(FieldSetModelFormMixin):
    """Permite editar la información que depende de una :class:`Persona`"""

    persona = forms.ModelChoiceField(label="",
                                     queryset=Persona.objects.all(),
                                     widget=forms.HiddenInput())


class FisicoForm(BasePersonaForm):
    """Permite editar :class:`Fisico`"""

    class Meta:
        model = Fisico
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FisicoForm, self).__init__(*args, **kwargs)
        self.helper.layout = Fieldset(u'Editar Fisico', *self.field_names)


class EstiloVidaForm(BasePersonaForm):
    """Permite editar :class:`EstiloVida`"""

    class Meta:
        model = EstiloVida
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EstiloVidaForm, self).__init__(*args, **kwargs)
        self.helper.layout = Fieldset(u'Editar Audiometria',
                                      *self.field_names)


class AntecedenteForm(BasePersonaForm):
    """Permite editar :class:`Antecedente`"""

    class Meta:
        model = Antecedente
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AntecedenteForm, self).__init__(*args, **kwargs)
        self.helper.layout = Fieldset(u'Editar Antecedentes Personales',
                                      *self.field_names)


class AntecedenteFamiliarForm(BasePersonaForm):
    """Permite editar :class:`AntecedenteFamiliar`"""

    class Meta:
        model = AntecedenteFamiliar
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AntecedenteFamiliarForm, self).__init__(*args, **kwargs)
        self.helper.layout = Fieldset(
            u'Editar Antecedentes Familiares',
            *self.field_names)


class AntecedenteObstetricoForm(BasePersonaForm):
    """Permite editar :class:`AntecedenteObstetrico`"""

    class Meta:
        model = AntecedenteObstetrico
        fields = '__all__'

    menarca = forms.DateField(widget=DateWidget(), required=False,
                              initial=timezone.now)
    ultimo_periodo = forms.DateField(widget=DateWidget(), required=False,
                                     initial=timezone.now)

    def __init__(self, *args, **kwargs):
        super(AntecedenteObstetricoForm, self).__init__(*args, **kwargs)
        self.helper.layout = Fieldset(u'Editar Antecedentes Obstétricos',
                                      *self.field_names)


class AntecedenteQuirurgicoForm(BasePersonaForm):
    """Permite editar :class:`AntecedenteQuirurgico`"""

    class Meta:
        model = AntecedenteQuirurgico
        fields = '__all__'

    fecha = forms.DateTimeField(widget=DateTimeWidget(), required=False,
                                initial=timezone.now)

    def __init__(self, *args, **kwargs):
        super(AntecedenteQuirurgicoForm, self).__init__(*args, **kwargs)
        self.helper.layout = Fieldset(u'Antecedente Quirúrgico',
                                      *self.field_names)


class PersonaSearchForm(FieldSetFormMixin):
    query = forms.CharField(label=u"Nombre o Identidad")

    def __init__(self, *args, **kwargs):
        super(PersonaSearchForm, self).__init__(*args, **kwargs)
        self.helper.add_input(Submit('submit', u'Buscar'))
        self.helper.layout = Fieldset(u'Buscar Persona', *self.field_names)
        self.helper.form_method = 'GET'
        self.helper.form_action = 'persona-search'


class EmpleadorForm(FieldSetModelFormMixin):
    class Meta:
        model = Empleador
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EmpleadorForm, self).__init__(*args, **kwargs)
        self.helper.layout = Fieldset(u'Datos del Empleador', *self.field_names)


class EmpleoForm(BasePersonaForm):
    class Meta:
        model = Empleo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EmpleoForm, self).__init__(*args, **kwargs)
        self.helper.layout = Fieldset(u'Datos de Empleo', *self.field_names)


class PersonaDuplicateForm(FieldSetModelFormMixin):
    class Meta:
        model = Persona
        fields = ('duplicado',)

    def __init__(self, *args, **kwargs):
        super(PersonaDuplicateForm, self).__init__(*args, **kwargs)
        self.helper.layout = Fieldset(u'Reportar Persona Duplicada',
                                      *self.field_names)


class PersonaRTNForm(FieldSetModelFormMixin):
    class Meta:
        model = Persona
        fields = ('rtn',)

    def __init__(self, *args, **kwargs):
        super(PersonaRTNForm, self).__init__(*args, **kwargs)
        self.helper.layout = Fieldset(u'Actualizar RTN de la Persona',
                                      *self.field_names)
