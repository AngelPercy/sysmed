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
import calendar
from collections import defaultdict
from datetime import time, timedelta

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models import Q, Count
from django.forms.models import inlineformset_factory
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.utils.datetime_safe import date, datetime
from django.utils.decorators import method_decorator
from django.views.generic import (DetailView, CreateView, View,
                                  ListView, UpdateView, TemplateView,
                                  RedirectView)
from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.edit import FormMixin, DeleteView
from guardian.decorators import permission_required

from clinique.forms import (PacienteForm, CitaForm, EvaluacionForm,
                            ConsultaForm, SeguimientoForm, LecturaSignosForm,
                            DiagnosticoClinicoForm, ConsultorioForm,
                            CitaPersonaForm, CargoForm, OrdenMedicaForm,
                            NotaEnfermeriaForm, ExamenForm, EsperaForm,
                            PacienteSearchForm, PrescripcionForm,
                            IncapacidadForm, ReporteForm, RemisionForm)
from clinique.models import (Paciente, Cita, Consulta, Evaluacion,
                             Seguimiento, LecturaSignos, Consultorio,
                             DiagnosticoClinico, Cargo, OrdenMedica,
                             NotaEnfermeria, Examen, Espera, Prescripcion,
                             Incapacidad, Reporte, Remision)
from inventory.models import ItemTemplate, Inventario
from invoice.forms import PeriodoForm
from persona.forms import FisicoForm, AntecedenteForm, PersonaForm, \
    AntecedenteFamiliarForm, AntecedenteObstetricoForm, EstiloVidaForm, \
    AntecedenteQuirurgicoForm
from persona.models import Fisico, Antecedente, AntecedenteFamiliar, \
    AntecedenteObstetrico, AntecedenteQuirurgico, EstiloVida, Persona
from persona.views import PersonaFormMixin, AntecedenteObstetricoCreateView
from users.mixins import LoginRequiredMixin, CurrentUserFormMixin


class ConsultorioPermissionMixin(LoginRequiredMixin):
    #@method_decorator(permission_required('clinique.consultorio'))
    def dispatch(self, *args, **kwargs):
        return super(ConsultorioPermissionMixin, self).dispatch(*args, **kwargs)


class ConsultorioIndexView(ListView, ConsultorioPermissionMixin):
    template_name = 'clinique/index.html'
    paginate_by = 20
    context_object_name = 'pacientes'

    def dispatch(self, request, *args, **kwargs):
        tz = timezone.get_current_timezone()
        now = timezone.now()
        day = timedelta(days=1)
        self.yesterday = now - day
        self.today = tz.localize(datetime.combine(now, time.min))
        self.fin = date(now.year, now.month,
                        calendar.monthrange(now.year, now.month)[1])
        self.inicio = date(now.year, now.month, 1)
        self.inicio = tz.localize(datetime.combine(self.inicio, time.min))
        self.fin = tz.localize(datetime.combine(self.fin, time.max))

        return super(ConsultorioIndexView, self).dispatch(request, *args,
                                                          **kwargs)

    def get_queryset(self):
        return Paciente.objects.filter(
            consultorio__usuario=self.request.user).order_by('nombre').all()

    def get_context_data(self, **kwargs):
        context = super(ConsultorioIndexView, self).get_context_data(**kwargs)
        context['citaperiodoform'] = PeriodoForm(prefix='cita-periodo')
        context['citaperiodoform'].helper.form_action = 'cita-periodo'
        context['citaperiodoform'].set_legend(u'Citas por Periodo')

        context['diagnosticoperiodoform'] = PeriodoForm(
            prefix='diagnostico-periodo')
        context[
            'diagnosticoperiodoform'].helper.form_action = 'diagnostico-periodo'
        context['diagnosticoperiodoform'].set_legend(
            u'Diagnosticos por Periodo')

        context['cargosperiodoform'] = PeriodoForm(prefix='cargo-periodo')
        context['cargosperiodoform'].helper.form_action = 'cargo-periodo'
        context['cargosperiodoform'].set_legend(u'Cargos por Periodo')

        context['consultasperiodoform'] = PeriodoForm(prefix='consulta')
        context['consultasperiodoform'].helper.form_action = 'consulta-periodo'
        context['consultasperiodoform'].set_legend(u'Consultas por Periodo')

        context['evaluacionperiodoform'] = PeriodoForm(
            prefix='evaluacion-periodo')
        context[
            'evaluacionperiodoform'].helper.form_action = 'evaluacion-periodo'
        context['evaluacionperiodoform'].set_legend(u'Evaluaciones por Periodo')

        context['seguimientoperiodoform'] = PeriodoForm(
            prefix='seguimiento-periodo')
        context[
            'seguimientoperiodoform'].helper.form_action = 'seguimiento-periodo'
        context['seguimientoperiodoform'].set_legend(
            u'Seguimientos por Periodo')

        context['pacientesearch'] = PacienteSearchForm()
        context[
            'pacientesearch'].helper.form_action = \
            'clinique-paciente-search-add'

        context['esperas'] = Espera.objects.filter(fecha__gte=self.yesterday,
                                                   consulta=False,
                                                   terminada=False,
                                                   atendido=False,
                                                   ausente=False).all()

        return context


class ConsultorioDetailView(SingleObjectMixin, ListView, LoginRequiredMixin):
    paginate_by = 20
    template_name = 'clinique/consultorio_detail.html'

    def dispatch(self, request, *args, **kwargs):
        tz = timezone.get_current_timezone()
        now = timezone.now()
        day = timedelta(days=1)
        self.yesterday = now - day
        self.today = tz.localize(datetime.combine(now, time.min))
        self.fin = date(now.year, now.month,
                        calendar.monthrange(now.year, now.month)[1])
        self.inicio = date(now.year, now.month, 1)
        self.inicio = tz.localize(datetime.combine(self.inicio, time.min))
        self.fin = tz.localize(datetime.combine(self.fin, time.max))

        return super(ConsultorioDetailView, self).dispatch(request, *args,
                                                           **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ConsultorioDetailView, self).get_context_data(**kwargs)

        context['consultorio'] = self.object
        context['buscar'] = PacienteSearchForm(
            initial={'consultorio': self.object.id})

        context['total'] = sum(e.tiempo() for e in self.get_queryset().all())
        context['citas'] = Cita.objects.filter(consultorio=self.object,
                                               fecha__gte=self.yesterday,
                                               fecha__lte=self.fin,
                                               ausente=False, atendida=False)

        context['consultas'] = Espera.objects.filter(consultorio=self.object,
                                                     consulta=True,
                                                     terminada=False)

        return context

    def get_queryset(self):
        self.object = self.get_object(Consultorio.objects.all())
        queryset = self.object.espera.filter(fecha__gte=self.yesterday,
                                             consulta=False, terminada=False,
                                             atendido=False, ausente=False)
        return queryset


class PacienteSearchView(ListView, LoginRequiredMixin):
    context_object_name = 'pacientes'
    model = Paciente
    template_name = 'clinique/paciente_list.html'
    paginate_by = 10

    def get_queryset(self):
        form = PacienteSearchForm(self.request.GET)

        # if not form.is_valid():
        # redirect('admision-estadisticas')
        form.is_valid()

        query = form.cleaned_data['query']
        consultorio = form.cleaned_data['consultorio']

        queryset = Paciente.objects.filter(
            Q(persona__nombre__icontains=query) |
            Q(persona__apellido__icontains=query) |
            Q(persona__identificacion__icontains=query),
            consultorio=consultorio,
        )

        return queryset.all()


class ConsultorioCreateView(CurrentUserFormMixin, CreateView):
    model = Consultorio
    form_class = ConsultorioForm


class ConsultorioMixin(View):
    def dispatch(self, *args, **kwargs):
        self.consultorio = get_object_or_404(Consultorio,
                                             pk=kwargs['consultorio'])
        return super(ConsultorioMixin, self).dispatch(*args, **kwargs)


class ConsultorioFormMixin(ConsultorioMixin):
    def get_initial(self):
        initial = super(ConsultorioFormMixin, self).get_initial()
        initial['consultorio'] = self.consultorio.id
        return initial


class PacienteCreateView(PersonaFormMixin, CreateView, LoginRequiredMixin):
    """Permite agregar una :class:`Persona` como un :class:`Paciente` de un
    doctor que tiene un :class:`User` en el sistema"""

    model = Paciente
    form_class = PacienteForm


class PacientePersonaCreateView(CreateView, LoginRequiredMixin,
                                ConsultorioFormMixin):
    model = Paciente
    template_name = 'clinique/paciente_create.html'

    def dispatch(self, request, *args, **kwargs):

        self.persona = Persona()

        self.PacienteFormset = inlineformset_factory(Persona, Paciente,
                                                     form=PacienteForm,
                                                     fk_name='persona', extra=1)
        return super(PacientePersonaCreateView, self).dispatch(request, *args,
                                                               **kwargs)

    def get_form(self, form_class):
        formset = self.PacienteFormset(instance=self.persona, prefix='paciente',
                                       initial=[
                                           {'consultorio': self.consultorio.id}]
                                       )
        return formset

    def get_context_data(self, **kwargs):

        self.persona_form = PersonaForm(instance=self.persona, prefix='persona')
        self.persona_form.helper.form_tag = False

        context = super(PacientePersonaCreateView, self).get_context_data(
            **kwargs)
        context['persona_form'] = self.persona_form
        return context

    def post(self, request, *args, **kwargs):
        self.persona_form = PersonaForm(request.POST, request.FILES,
                                        instance=self.persona,
                                        prefix='persona')
        self.formset = self.PacienteFormset(request.POST, request.FILES,
                                            instance=self.persona,
                                            prefix='paciente')

        if self.persona_form.is_valid() and self.formset.is_valid():
            self.persona_form.save()
            instances = self.formset.save()
            for instance in instances:
                self.paciente = instance
                self.paciente.save()

            return self.form_valid(self.formset)
        else:
            self.object = None
            return self.form_invalid(self.formset)

    def get_success_url(self):

        return self.paciente.get_absolute_url()


class PacienteDetailView(DetailView, LoginRequiredMixin):
    """Permite ver los datos del :class"`Paciente` en la interfaz gráfica"""

    model = Persona
    context_object_name = 'paciente'
    template_name = 'clinique/paciente_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PacienteDetailView, self).get_context_data()

        context['consultas'] = self.object.consultas.filter(facturada=False,
                                                            activa=True).all()

        return context


class PacienteDeleteView(DeleteView, LoginRequiredMixin):
    model = Paciente

    def get_success_url(self):
        return reverse('consultorio-index')


class PacienteMixin(View):
    """Permite obtener un :class:`Paciente` desde los argumentos en una url"""

    def dispatch(self, *args, **kwargs):
        self.paciente = get_object_or_404(Paciente, pk=kwargs['paciente'])
        return super(PacienteMixin, self).dispatch(*args, **kwargs)


class ConsultaMixin(View):
    """Permite obtener un :class:`Paciente` desde los argumentos en una url"""

    def dispatch(self, *args, **kwargs):
        self.consulta = get_object_or_404(Consulta, pk=kwargs['consulta'])
        return super(ConsultaMixin, self).dispatch(*args, **kwargs)


class PacienteFormMixin(FormMixin, PacienteMixin):
    """Permite inicializar el paciente que se utilizará en un formulario"""

    def get_initial(self):
        initial = super(PacienteFormMixin, self).get_initial()
        initial = initial.copy()
        initial['paciente'] = self.paciente
        return initial


class ConsultaFormMixin(FormMixin, ConsultaMixin):
    """Permite inicializar el paciente que se utilizará en un formulario"""

    def get_initial(self):
        initial = super(ConsultaFormMixin, self).get_initial()
        initial = initial.copy()
        initial['consulta'] = self.consulta
        return initial


class ConsultorioPacienteListView(ConsultorioMixin, ListView,
                                  LoginRequiredMixin):
    model = Paciente
    context_object_name = 'pacientes'

    def get_queryset(self):
        return Paciente.objects.filter(consultorio=self.consultorio).order_by(
            'created').all()


class CitaCreateView(CreateView, LoginRequiredMixin):
    model = Cita
    form_class = CitaForm


class CitaPersonaCreateView(CreateView, PersonaFormMixin, LoginRequiredMixin):
    model = Cita
    form_class = CitaPersonaForm


class CitaPeriodoView(TemplateView, LoginRequiredMixin):
    """Muestra los contratos de un periodo"""
    template_name = 'clinique/cita_periodo.html'

    def dispatch(self, request, *args, **kwargs):
        self.form = PeriodoForm(request.GET, prefix='cita-periodo')

        if self.form.is_valid():
            self.inicio = self.form.cleaned_data['inicio']
            self.fin = datetime.combine(self.form.cleaned_data['fin'], time.max)
            self.citas = Cita.objects.filter(
                fecha__gte=self.inicio,
                fecha__lte=self.fin
            )
        return super(CitaPeriodoView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CitaPeriodoView, self).get_context_data(**kwargs)

        context['citas'] = self.citas
        context['inicio'] = self.inicio
        context['fin'] = self.fin

        return context


class DiagnosticoPeriodoView(TemplateView, LoginRequiredMixin):
    """Muestra los :class:`DiagnosticoClinico` de un periodo"""
    template_name = 'clinique/diagnostico_periodo.html'

    def dispatch(self, request, *args, **kwargs):
        self.form = PeriodoForm(request.GET, prefix='diagnostico-periodo')

        if self.form.is_valid():
            self.inicio = self.form.cleaned_data['inicio']
            self.fin = datetime.combine(self.form.cleaned_data['fin'], time.max)
            self.diagnosticos = DiagnosticoClinico.objects.filter(
                created__gte=self.inicio,
                created__lte=self.fin
            ).order_by('paciente__consultorio')
        return super(DiagnosticoPeriodoView, self).dispatch(request, *args,
                                                            **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DiagnosticoPeriodoView, self).get_context_data(**kwargs)

        context['diagnosticos'] = self.diagnosticos
        context['inicio'] = self.inicio
        context['fin'] = self.fin
        context['total'] = self.diagnosticos.count()

        DiagnosticoClinico.objects.values('paciente__consultorio').annotate(
            consultorio_count=Count('paciente__consultorio')
        ).filter(created__gte=self.inicio, created__lte=self.fin)

        cons = defaultdict(int)
        consultorios = Consultorio.objects.all()
        for consultorio in consultorios:
            cons[consultorio] = DiagnosticoClinico.objects.filter(
                created__gte=self.inicio, created__lte=self.fin,
                paciente__consultorio=consultorio).count()

        cons = dict((k, v) for k, v in cons.items() if v > 0)

        context['consultorios'] = reversed(
            sorted(cons.iteritems(), key=lambda x: x[1]))
        context['consultorio_graph'] = reversed(
            sorted(cons.iteritems(), key=lambda x: x[1]))
        context['consultorio_graph2'] = reversed(
            sorted(cons.iteritems(), key=lambda x: x[1]))

        return context


class CargoPeriodoView(TemplateView, LoginRequiredMixin):
    """Muestra los :class:`Cargo` de un periodo"""
    template_name = 'clinique/cargo_periodo.html'

    def dispatch(self, request, *args, **kwargs):
        self.form = PeriodoForm(request.GET, prefix='cargo-periodo')

        if self.form.is_valid():
            self.inicio = self.form.cleaned_data['inicio']
            self.fin = datetime.combine(self.form.cleaned_data['fin'], time.max)
            self.cargos = Cargo.objects.filter(
                created__gte=self.inicio,
                created__lte=self.fin
            )
        return super(CargoPeriodoView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CargoPeriodoView, self).get_context_data(**kwargs)

        context['cargos'] = self.cargos
        context['inicio'] = self.inicio
        context['fin'] = self.fin

        context['cuenta'] = ItemTemplate.objects.values('descripcion').annotate(
            cargo_count=Count('consultorio_cargos')).filter(
            consultorio_cargos__created__gte=self.inicio,
            consultorio_cargos__created__lte=self.fin)

        return context


class CitaListView(ConsultorioMixin, ListView, LoginRequiredMixin):
    model = Cita
    context_object_name = 'citas'

    def get_queryset(self):
        self.citas = Cita.objects.filter(consultorio=self.consultorio,
                                         fecha__gte=timezone.now().date(),
                                         ausente=False)

        return self.citas.all()

    def get_context_data(self, **kwargs):
        context = super(CitaListView, self).get_context_data(**kwargs)
        context['consultorio'] = self.consultorio

        fechas = defaultdict(list)

        for cita in self.citas.all():
            fechas[cita.fecha.date()].append(cita)

        context['fechas'] = fechas.iteritems()
        return context


class CitaAusenteView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self, **kwargs):
        cita = get_object_or_404(Cita, pk=kwargs['pk'])
        cita.ausente = True
        cita.save()
        messages.info(self.request,
                      u'¡Se marco la espera como ausente!')
        return cita.get_absolute_url()


class EvaluacionCreateView(PersonaFormMixin, ConsultaFormMixin,
                           CurrentUserFormMixin, CreateView):
    model = Evaluacion
    form_class = EvaluacionForm


class EvaluacionUpdateView(UpdateView, LoginRequiredMixin):
    model = Evaluacion
    form_class = EvaluacionForm


class EvaluacionPeriodoView(TemplateView, LoginRequiredMixin):
    """Muestra los :class:`Evaluacion` de un periodo"""
    template_name = 'clinique/evaluacion_periodo.html'

    def dispatch(self, request, *args, **kwargs):
        self.form = PeriodoForm(request.GET, prefix='evaluacion-periodo')

        if self.form.is_valid():
            self.inicio = self.form.cleaned_data['inicio']
            self.fin = datetime.combine(self.form.cleaned_data['fin'], time.max)
            self.evaluaciones = Evaluacion.objects.filter(
                created__gte=self.inicio,
                created__lte=self.fin
            ).order_by('paciente__consultorio')
        return super(EvaluacionPeriodoView, self).dispatch(request, *args,
                                                           **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EvaluacionPeriodoView, self).get_context_data(**kwargs)

        context['evaluaciones'] = self.evaluaciones
        context['inicio'] = self.inicio
        context['fin'] = self.fin

        return context


class ConsultaCreateView(PersonaFormMixin, CurrentUserFormMixin,
                         ConsultorioFormMixin, CreateView,
                         LoginRequiredMixin):
    model = Consulta
    form_class = ConsultaForm


class ConsultaDetailView(LoginRequiredMixin, DetailView):
    model = Consulta
    context_object_name = 'consulta'


class SeguimientoCreateView(PersonaFormMixin, CurrentUserFormMixin, CreateView,
                            LoginRequiredMixin):
    model = Seguimiento
    form_class = SeguimientoForm


class SeguimientoPeriodoView(TemplateView, LoginRequiredMixin):
    """Muestra los :class:`Seguimiento`s de un periodo"""
    template_name = 'clinique/seguimiento_periodo.html'

    def dispatch(self, request, *args, **kwargs):
        self.form = PeriodoForm(request.GET, prefix='seguimiento-periodo')

        if self.form.is_valid():
            self.inicio = self.form.cleaned_data['inicio']
            self.fin = datetime.combine(self.form.cleaned_data['fin'], time.max)
            self.seguimiento = Seguimiento.objects.filter(
                created__gte=self.inicio,
                created__lte=self.fin
            )
        return super(SeguimientoPeriodoView, self).dispatch(request, *args,
                                                            **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SeguimientoPeriodoView, self).get_context_data(**kwargs)

        context['seguimientos'] = self.seguimiento
        context['inicio'] = self.inicio
        context['fin'] = self.fin

        context['cuenta'] = Seguimiento.objects.values(
            'paciente').annotate(
            seguimiento_count=Count('id'))

        return context


class LecturaSignosCreateView(PersonaFormMixin, LoginRequiredMixin, CreateView):
    model = LecturaSignos
    form_class = LecturaSignosForm

    def form_valid(self, form):
        self.object = form.save(commit=True)

        esperas = Espera.objects.filter(persona=self.object.persona,
                                        terminada=False)

        for espera in esperas.all():
            espera.fecha = timezone.now()

        return HttpResponseRedirect(self.get_success_url())


class LecturaSignosUpdateView(UpdateView, LoginRequiredMixin):
    model = LecturaSignos
    form_class = LecturaSignosForm


class DiagnosticoCreateView(PersonaFormMixin, ConsultaFormMixin,
                            CurrentUserFormMixin, CreateView):
    model = DiagnosticoClinico
    form_class = DiagnosticoClinicoForm


class DiagnosticoUpdateView(UpdateView, LoginRequiredMixin):
    model = DiagnosticoClinico
    form_class = DiagnosticoClinicoForm


class CliniquePersonaUpdateView(UpdateView, LoginRequiredMixin):
    model = Persona
    form_class = PersonaForm
    template_name = 'clinique/persona_update.html'

    def get_success_url(self):
        return reverse('clinique-fisico-editar', args=[self.object.id])


class CliniqueFisicoUpdateView(UpdateView, LoginRequiredMixin):
    """
    Permite actualizar los datos del :class:`Fisico` de una :class:`Persona`
    """

    model = Fisico
    form_class = FisicoForm
    template_name = 'clinique/fisico_update.html'

    def get_success_url(self):
        return reverse('clinique-antecedente-editar',
                       args=[self.object.persona.id])


class CliniqueAntecedenteUpdateView(UpdateView, LoginRequiredMixin):
    """Permite actualizar los datos del :class:`Antecedente` de una
    :class:`Persona`"""

    model = Antecedente
    form_class = AntecedenteForm
    template_name = 'clinique/antecedente_update.html'

    def get_success_url(self):
        return reverse('clinique-antecedente-familiar-editar',
                       args=[self.object.persona.id])


class CliniqueAntecedenteObstetricoCreateView(AntecedenteObstetricoCreateView):
    def get_success_url(self):
        return reverse('clinique-antecedente-editar',
                       args=[self.object.persona.id])


class CliniqueAntecedenteFamiliarUpdateView(UpdateView, LoginRequiredMixin):
    """Permite actualizar los datos del :class:`AntecedenteFamiliar` de una
    :class:`Persona`"""

    model = AntecedenteFamiliar
    form_class = AntecedenteFamiliarForm
    template_name = 'clinique/antecedente_familiar_update.html'

    def get_success_url(self):
        return reverse('clinique-estilovida-editar',
                       args=[self.object.persona.id])


class CliniqueAntecedenteObstetricoUpdateView(UpdateView, LoginRequiredMixin):
    """Permite actualizar los datos del :class:`AntecedenteObstetrico` de una
    :class:`Persona`"""

    model = AntecedenteObstetrico
    form_class = AntecedenteObstetricoForm
    template_name = 'clinique/antecedente_obstetrico_update.html'


class CliniqueAntecedenteQuirurgicoUpdateView(UpdateView, LoginRequiredMixin):
    """Permite actualizar los datos del :class:`AntecedenteQuirurgico` de una
    :class:`Persona`"""

    model = AntecedenteQuirurgico
    form_class = AntecedenteQuirurgicoForm
    template_name = 'clinique/antecedente_quirurgico_update.html'

    def get_success_url(self):
        return reverse('clinique-antecedente-editar',
                       args=[self.object.persona.id])


class CliniqueAntecedenteQuirurgicoCreateView(CreateView, PersonaFormMixin,
                                              PacienteMixin,
                                              LoginRequiredMixin):
    model = AntecedenteQuirurgico
    form_class = AntecedenteQuirurgicoForm
    template_name = 'clinique/antecedente_quirurgico_create.html'

    def get_success_url(self):
        return reverse('clinique-paciente', args=[self.paciente.id])


class CliniqueEstiloVidaUpdateView(UpdateView, LoginRequiredMixin):
    """Permite actualizar los datos del :class:`EstiloVida` de una
    :class:`Persona`"""

    model = EstiloVida
    form_class = EstiloVidaForm
    template_name = 'clinique/estilo_vida_update.html'


class CargoCreateView(ConsultaFormMixin, CurrentUserFormMixin, CreateView):
    """Permite crear :class:`Cargo`s durante una :class:`Consulta`"""
    model = Cargo
    form_class = CargoForm

    def form_valid(self, form):
        self.object = form.save(commit=False)

        consultorio = self.object.consulta.consultorio
        if consultorio.inventario is None:
            inventario = Inventario(lugar=consultorio.nombre)
            inventario.save()
            consultorio.inventario = inventario
            consultorio.save()

        item = consultorio.inventario.buscar_item(self.object.item)
        item.disminuir(self.object.cantidad)
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class OrdenMedicaCreateView(PersonaFormMixin, ConsultaFormMixin,
                            CurrentUserFormMixin, CreateView):
    model = OrdenMedica
    form_class = OrdenMedicaForm


class OrdenMedicaUpdateView(LoginRequiredMixin, UpdateView):
    model = OrdenMedica
    form_class = OrdenMedicaForm


class NotaEnfermeriaCreateView(PersonaFormMixin, CurrentUserFormMixin,
                               CreateView):
    model = NotaEnfermeria
    form_class = NotaEnfermeriaForm


class ExamenCreateView(PacienteFormMixin, LoginRequiredMixin, CreateView):
    model = Examen
    form_class = ExamenForm


class ExamenUpdateView(UpdateView, LoginRequiredMixin):
    model = Examen
    form_class = ExamenForm


class EsperaCreateView(PersonaFormMixin, ConsultorioFormMixin,
                       LoginRequiredMixin, CreateView):
    model = Espera
    form_class = EsperaForm


class EsperaConsultorioCreateView(PersonaFormMixin, LoginRequiredMixin,
                                  CreateView):
    model = Espera
    form_class = EsperaForm


class EsperaListView(ConsultorioMixin, LoginRequiredMixin, ListView):
    model = Espera


class EsperaAusenteView(RedirectView, LoginRequiredMixin):
    permanent = False

    def get_redirect_url(self, **kwargs):
        espera = get_object_or_404(Espera, pk=kwargs['pk'])
        espera.ausente = True
        espera.save()
        messages.info(self.request,
                      u'¡Se marco la espera como ausente!')
        return espera.get_absolute_url()


class PrescripcionCreateView(PersonaFormMixin, ConsultaFormMixin,
                             CurrentUserFormMixin, CreateView):
    model = Prescripcion
    form_class = PrescripcionForm


class PrescripcionUpdateView(UpdateView, LoginRequiredMixin):
    model = Prescripcion
    form_class = PrescripcionForm


class IncapacidadCreateView(PersonaFormMixin, ConsultaFormMixin,
                            CurrentUserFormMixin, CreateView):
    model = Incapacidad
    form_class = IncapacidadForm


class IncapacidadUpdateView(LoginRequiredMixin, UpdateView):
    model = Incapacidad
    form_class = IncapacidadForm


class ReporteCreateView(ConsultorioFormMixin, LoginRequiredMixin, CreateView):
    model = Reporte
    form_class = ReporteForm


class ReporteListView(ListView, LoginRequiredMixin):
    model = Reporte
    queryset = Reporte.objects.order_by('-created')
    context_object_name = 'reportes'
    paginate_by = 20


class CitaEsperaRedirectView(RedirectView, LoginRequiredMixin):
    """Crea una :class:´Espera´ a partir de una :class:´Cita´ y redirige al
    usuario al :class:´Consultorio´ asociado"""

    permanent = False

    def get_redirect_url(self, **kwargs):
        cita = get_object_or_404(Cita, pk=kwargs['pk'])
        espera = cita.to_espera()
        espera.save()
        messages.info(self.request,
                      u'¡Se envio el paciente a salada de espera!')
        return espera.get_absolute_url()


class EsperaConsultaRedirectView(RedirectView, LoginRequiredMixin):
    """Crea una :class:´Espera´ a partir de una :class:´Cita´ y redirige al
    usuario al :class:´Consultorio´ asociado"""

    permanent = False

    def get_redirect_url(self, **kwargs):
        espera = get_object_or_404(Espera, pk=kwargs['pk'])
        espera.consulta = True
        espera.inicio = timezone.now()
        espera.save()
        messages.info(self.request,
                      u'¡Se envio el paciente a salada de consulta!')
        return espera.get_absolute_url()


class EsperaTerminadaRedirectView(RedirectView, LoginRequiredMixin):
    """Crea una :class:´Espera´ a partir de una :class:´Cita´ y redirige al
    usuario al :class:´Consultorio´ asociado"""

    permanent = False

    def get_redirect_url(self, **kwargs):
        espera = get_object_or_404(Espera, pk=kwargs['pk'])
        espera.terminada = True
        espera.fin = timezone.now()
        consultas = Consulta.objects.filter(activa=True, persona=espera.persona)

        for consulta in consultas.all():
            consulta.activa = False
            consulta.save()

        espera.save()
        messages.info(self.request,
                      u'¡La consulta se marcó como terminada!')
        return espera.get_absolute_url()


class RemisionCreateView(LoginRequiredMixin, PersonaFormMixin, CreateView):
    """Permite crear una :class:`Remision` a una :class:`Persona`"""

    model = Remision
    form_class = RemisionForm


class ConsultaTerminadaRedirectView(RedirectView, LoginRequiredMixin):
    permanent = False

    def get_redirect_url(self, **kwargs):
        consulta = get_object_or_404(Consulta, pk=kwargs['pk'])
        consulta.activa = False
        consulta.final = timezone.now()
        consulta.save()

        esperas = Espera.objects.filter(terminada=False,
                                        persona=consulta.persona)
        for espera in esperas.all():
            espera.terminada = True
            espera.fin = timezone.now()
            espera.save()

        messages.info(self.request,
                      u'¡La consulta se marcó como terminada!')
        return consulta.get_absolute_url()


class ConsultaPeriodoView(TemplateView, LoginRequiredMixin):
    """Muestra las opciones disponibles para la aplicación"""

    template_name = 'clinique/consulta_list.html'

    def dispatch(self, request, *args, **kwargs):
        """Filtra las :class:`Emergencia` de acuerdo a los datos ingresados en
        el formulario"""

        self.form = PeriodoForm(request.GET, prefix='consulta')
        if self.form.is_valid():
            self.inicio = self.form.cleaned_data['inicio']
            self.fin = datetime.combine(self.form.cleaned_data['fin'], time.max)
            self.consultas = Consulta.objects.filter(
                created__range=(self.inicio, self.fin)
            )
        else:
            return redirect('invoice-index')

        return super(ConsultaPeriodoView, self).dispatch(request, *args,
                                                         **kwargs)

    def get_context_data(self, **kwargs):

        """Permite utilizar las :class:`Emergencia`s en la vista"""

        context = super(ConsultaPeriodoView, self).get_context_data(**kwargs)
        context['consultas'] = self.consultas
        context['inicio'] = self.inicio
        context['fin'] = self.fin
        return context
