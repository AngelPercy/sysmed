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
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DetailView, UpdateView,
                                  ListView, View, TemplateView)
from django.views.generic.edit import FormMixin
from django.shortcuts import get_object_or_404, redirect
from django.db.models.query_utils import Q
from django.http import HttpResponse, Http404
from lab.forms import ResultadoEditForm

from lab.models import Resultado

from persona.forms import (PersonaForm, FisicoForm, EstiloVidaForm,
                           AntecedenteForm, AntecedenteFamiliarForm,
                           AntecedenteObstetricoForm,
                           AntecedenteQuirurgicoForm, PersonaSearchForm,
                           EmpleadorForm, EmpleoForm, PersonaDuplicateForm)
from persona.models import (Persona, Fisico, EstiloVida, Antecedente,
                            AntecedenteFamiliar, AntecedenteObstetrico,
                            AntecedenteQuirurgico, Empleo, Empleador, RegistroConsulta)
from users.mixins import LoginRequiredMixin
from django.core.servers.basehttp import FileWrapper
import mimetypes
from django.conf import settings
import os


class PersonaDownloadView(TemplateView):


    def get(self, request, *args, **kwargs):
        filename = request.GET['image']
        filepath = os.path.join(settings.MEDIA_ROOT, filename)  
        wrapper = FileWrapper(open(filepath, 'rb'))
        response = HttpResponse(wrapper, content_type="image/png")
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        return response

class PersonaDeleteView(TemplateView):

    def get(self, request, *args, **kwargs):
        resultado = Resultado.objects.filter(pk = request.GET['exam_id']).exists()
        if resultado:
            Resultado.objects.get(pk = request.GET['exam_id']).delete()
            return redirect(request.META['HTTP_REFERER'])
        else:
            raise Http404

class PersonaEditView(UpdateView):

    model = Resultado
    form_class = ResultadoEditForm
        

class PersonaPermissionMixin(LoginRequiredMixin):
    @method_decorator(permission_required('persona.persona'))
    def dispatch(self, *args, **kwargs):
        return super(PersonaPermissionMixin, self).dispatch(*args, **kwargs)


class PersonaMixin(View):
    """Agrega una :class:`Persona` en la vista"""

    def dispatch(self, *args, **kwargs):
        self.persona = get_object_or_404(Persona, pk=kwargs['persona'])
        return super(PersonaMixin, self).dispatch(*args, **kwargs)


class PersonaFormMixin(FormMixin, PersonaMixin):
    """Agrega la :class:`Persona` a los argumentos iniciales de un formulario"""

    def get_initial(self):
        initial = super(PersonaFormMixin, self).get_initial()
        initial = initial.copy()
        initial['persona'] = self.persona.id
        return initial


class PersonaIndexView(ListView, PersonaPermissionMixin):
    context_object_name = 'personas'
    model = Persona
    template_name = 'persona/index.html'
    paginate_by = 10


class PersonaDetailView(LoginRequiredMixin, DetailView):
    """Permite mostrar los datos de una :class:`Persona`"""

    context_object_name = 'persona'
    model = Persona

    def get_context_data(self, **kwargs):

        context = super(PersonaDetailView, self).get_context_data(**kwargs)

        registroConsulta = RegistroConsulta.objects.filter(person=self.object).last()
        context['registroConsulta'] = registroConsulta
        if self.object.sexo == 'F':
            antecedente_obstetrico = AntecedenteObstetrico(persona=self.object)
            antecedente_obstetrico.save()

        self.object.save()

        return context


class PersonaCreateView(CreateView, LoginRequiredMixin):
    """Permite ingresar :class:`Persona`s a la aplicación"""

    model = Persona
    form_class = PersonaForm

    def form_valid(self, form):
        user = form.save()
        personExist = Persona.objects.filter(identificacion = form.cleaned_data['identificacion']).exists()
        if personExist:
            person = Persona.objects.get(identificacion = form.cleaned_data['identificacion'])
            RegistroConsulta.objects.create(person = person)
            return redirect('/persona/%s' % person.pk)
        else:
            RegistroConsulta.objects.create(person = user)
        return super(PersonaCreateView, self).form_valid(form)


class PersonaUpdateView(UpdateView, LoginRequiredMixin):
    """Permite actualizar los datos de una :class:`Persona`"""

    model = Persona
    form_class = PersonaForm


class FisicoUpdateView(UpdateView, LoginRequiredMixin):
    """
    Permite actualizar los datos del :class:`Fisico` de una :class:`Persona`
    """

    model = Fisico
    form_class = FisicoForm


class EstiloVidaUpdateView(UpdateView, LoginRequiredMixin):
    """Permite actualizar los datos del :class:`EstiloVida` de una
    :class:`Persona`"""

    model = EstiloVida
    form_class = EstiloVidaForm


class AntecedenteUpdateView(UpdateView, LoginRequiredMixin):
    """Permite actualizar los datos del :class:`Antecedente` de una
    :class:`Persona`"""

    model = Antecedente
    form_class = AntecedenteForm


class AntecedenteFamiliarUpdateView(UpdateView, LoginRequiredMixin):
    """Permite actualizar los datos del :class:`AntecedenteFamiliar` de una
    :class:`Persona`"""

    model = AntecedenteFamiliar
    form_class = AntecedenteFamiliarForm


class AntecedenteObstetricoUpdateView(UpdateView, LoginRequiredMixin):
    """Permite actualizar los datos del :class:`AntecedenteObstetrico` de una
    :class:`Persona`"""

    model = AntecedenteObstetrico
    form_class = AntecedenteObstetricoForm


class AntecedenteQuirurgicoCreateView(PersonaFormMixin, LoginRequiredMixin,
                                      CreateView):
    """Permite actualizar los datos del :class:`AntecedenteQuirurgico` de una
    :class:`Persona`"""

    model = AntecedenteQuirurgico
    form_class = AntecedenteQuirurgicoForm


class AntecedenteQuirurgicoUpdateView(UpdateView, LoginRequiredMixin):
    """Permite actualizar los datos del :class:`AntecedenteQuirurgico` de una
    :class:`Persona`"""

    model = AntecedenteQuirurgico
    form_class = AntecedenteQuirurgicoForm


class PersonaSearchView(ListView, LoginRequiredMixin):
    context_object_name = 'personas'
    model = Persona
    template_name = 'persona/index.html'
    paginate_by = 10

    def get_queryset(self):
        form = PersonaSearchForm(self.request.GET)

        if form.is_valid():

            query = form.cleaned_data['query']

            queryset = Persona.objects.filter(
                Q(nombre__icontains=query) |
                Q(apellido__icontains=query) |
                Q(identificacion__icontains=query)
            )

            return queryset.all()

        return Persona.objects.none()


class EmpleadorCreateView(CreateView, LoginRequiredMixin):
    model = Empleador
    form_class = EmpleadorForm


class EmpleadorDetailView(DetailView, LoginRequiredMixin):
    model = Empleador
    context_object_name = 'empleador'


class EmpleoCreateView(PersonaFormMixin, CreateView):
    model = Empleo
    form_class = EmpleoForm


class PersonaDuplicateView(UpdateView, LoginRequiredMixin):
    model = Persona
    form_class = PersonaDuplicateForm


class AntecedenteObstetricoCreateView(PersonaFormMixin, CreateView,
                                      LoginRequiredMixin):
    model = AntecedenteObstetrico
    form_class = AntecedenteObstetricoForm
