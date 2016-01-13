# -*- coding: utf-8 -*-
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

"""
Modelos básicos necesarios para recabar la información personal de una
:class:`Persona` en la aplicación, permitiendo centralizar las funciones que
se utilizarán a lo largo de todo el sistema
"""
import re
from datetime import date

from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django_extensions.db.models import TimeStampedModel

from persona.fields import OrderedCountryField


class Persona(models.Model):
    """Representación de una :class:`Persona` en la aplicación"""

    class Meta:
        permissions = (
            ('persona', 'Permite al usuario gestionar persona'),
        )

    GENEROS = (
        ('M', u'Masculino'),
        ('F', u'Femenino'),
    )

    ESTADOS_CIVILES = (
        ('S', u'Soltero/a'),
        ('D', u'Divorciado/a'),
        ('C', u'Casado/a'),
        ('U', u'Union Libre')
    )
    TIPOS_IDENTIDAD = (
        ("R", u"Documento de Identidad"),
        ("L", u"Licencia"),
        ("P", u"Pasaporte"),
        ("T", u"Tarjeta de Identidad"),
        ("N", u"Ninguno"),
    )

    EXAMEN_MEDICO = (
        ("O", u'PRE OCUPACIONAL'),
        ("I", u'PERIDICO'),
        ("E", u'RETIRO'),
        ("U", u'POR CAMBIO DE PUESTO'),
        ("A", u'POR REINCORPORACION'),
    )

    TRABAJOSREALIZAR = (
        ("0", u'CHOFER'),
        ("1", u'TRABAJOS DE ALTURA'),
        ("2", u'ADMINISTRATIVO'),
        ("3", u'LABORATORIO'),
        ("4", u'TRABAJO ESPACIO CONFINADO'),
        ("5", u'MANTENIMIENTO LIMPIEZA'),
    )
    __expresion__ = re.compile(r'\d{4}-\d{4}-\d{5}')

    tipo_identificacion = models.CharField(max_length=1,
                                           choices=TIPOS_IDENTIDAD, blank=True)
    identificacion = models.CharField(max_length=8, blank=True, verbose_name=u'D.N.I:')
    establecimiento = models.CharField(max_length=200, blank=True, verbose_name=u'ESTABLECIMIENTO:')
    proyecto = models.CharField(max_length=200, blank=True, verbose_name=u'PROYECTO:')
    fecha_examen = models.DateField(default=date.today, verbose_name=u'FECHA DE EXAMEN:')
    nombre = models.CharField(max_length=50, blank=True, verbose_name=u'NOMBRES:')
    apellido = models.CharField(max_length=50, blank=True, verbose_name=u'APELLIDOS:')
    sexo = models.CharField(max_length=1, choices=GENEROS, blank=True, verbose_name=u'SEXO:')
    nacimiento = models.DateField(default=date.today, verbose_name=u'FECHA NACIMIENTO:')
    lugar_nac = models.CharField(max_length=200, blank=True, null=True, verbose_name=u'LUGAR NACIMIENTO:' )
    estado_civil = models.CharField(max_length=1, choices=ESTADOS_CIVILES,
                                    blank=True, verbose_name=u'ESTADO CIVIL:')
    profesion = models.CharField(max_length=200, blank=True, verbose_name=u'PROFESION:')
    telefono = models.CharField(max_length=200, blank=True, verbose_name=u'TELEFONO:')
    celular = models.CharField(max_length=200, blank=True, verbose_name=u'CELULAR:')
    domicilio = models.CharField(max_length=200, blank=True, verbose_name=u'DOMICILIO:')
    email = models.CharField(max_length=200, blank=True, verbose_name=u'E-MAIL:')
    fotografia = models.ImageField(upload_to='persona/foto//%Y/%m/%d',
                                   blank=True, null=True,
                                   help_text="El archivo debe estar en "
                                             "formato jpg o png y no pesar "
                                             "mas de 120kb")
    nacionalidad = OrderedCountryField(blank=True, ordered=('HN',))
    duplicado = models.BooleanField(default=False)
    rtn = models.CharField(max_length=200, blank=True, null=True, verbose_name=u'Interfase', help_text=u'Deje en Blanco NO registre...!')
    examen_medico = models.CharField(max_length=1, choices=EXAMEN_MEDICO, blank=True)
    trabajo_realizar = models.CharField(max_length=1, choices=TRABAJOSREALIZAR, blank=True)
    mostrar_en_cardex = models.BooleanField(default=False, verbose_name=u'Realizar Seguimiento')

    @staticmethod
    def validar_identidad(identidad):

        """Permite validar la identidad ingresada antes de asignarla a una
        :class:`Persona`
        
        :param identidad: Número de identidad a validar
        """

        return Persona.__expresion__.match(identidad)

    def __unicode__(self):

        """Muestra el nombre completo de la persona"""

        return self.nombre_completo()

    def get_absolute_url(self):

        """Obtiene la URL absoluta"""

        return reverse('persona-view-id', args=[self.id])

    def nombre_completo(self):

        """Obtiene el nombre completo de la :class:`Persona`"""

        return u'{0} {1}'.format(self.nombre, self.apellido).upper()

    def obtener_edad(self):

        """Obtiene la edad de la :class:`Persona`"""

        if self.nacimiento is None:
            return None

        today = date.today()
        born = date(self.nacimiento.year,
                    self.nacimiento.month,
                    self.nacimiento.day)
        try:
            # raised when birth date is February 29 and the current year is
            # not a leap year
            birthday = born.replace(year=today.year)
        except ValueError:
            birthday = born.replace(year=today.year, day=born.day - 1)

        if birthday > today:
            return today.year - born.year - 1
        else:
            return today.year - born.year


class Fisico(models.Model):
    """Describe el estado fisico de una :class:`Persona`"""

    persona = models.OneToOneField(Persona, primary_key=True)
    talla = models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name=u'TALLA:')
    peso = models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name=u'PESO:')
    imc = models.CharField(max_length=100, blank=True, verbose_name=u'IMC:')
    fr = models.CharField(max_length=100, blank=True, verbose_name=u'FR:')
    saturacion = models.CharField(max_length=30, blank= True, verbose_name=u'So2:')
    max_inspiracion = models.CharField(max_length=200, blank= True, verbose_name=u'MAX INSPIRACION:')
    expiracion_forzada = models.CharField(max_length=200, blank= True)
    pas = models.CharField(max_length=100, blank= True, verbose_name=u'PAS:')
    pad = models.CharField(max_length=100, blank= True, verbose_name=u'PAD:')
    fc = models.CharField(max_length=100, blank= True, verbose_name=u'FC:')
    temperatura = models.DecimalField(decimal_places=2, max_digits=8,
                                      null=True, verbose_name=u'T° :')
    perime_torax = models.CharField(max_length=100, blank= True, verbose_name=u'PERÍMETRO TORÁXICO:')
    perime_cintura = models.CharField(max_length=100, blank= True, verbose_name=u'PERÍMETRO CINTURA:')
    perime_cadera = models.CharField(max_length=100, blank= True, verbose_name=u'PERÍMETRO CADERA:')
    icc = models.CharField(max_length=100, blank= True, verbose_name=u'ICC:')
    otros = models.CharField(max_length=200, blank=True, verbose_name=u'OTROS')
    
    def get_absolute_url(self):
        """Obtiene la URL absoluta"""

        return reverse('persona-view-id', args=[self.persona.id])


class EstiloVida(models.Model):
    """Resumen del estilo de vida de una :class:`Persona`"""

    CONDICION = (
        ("0", u'SI'),
        ("1", u'NO'),
    )

    CONDICIONALES = (
        ("A", u'A VECES'),
        ("B", u'SIEMPRE'),
        ("C", u'NUNCA'),
    )

    RUIDOS = (
        ("I", u'MUY INTENSO'),
        ("M", u'MODERADO'),
        ("O", u'NO MOLESTO'),
    )

    persona = models.OneToOneField(Persona, primary_key=True,
                                   related_name='estilo_vida')
    fecha_examen = models.DateField(default=date.today, verbose_name=u'FECHA DE EXAMEN:')
    empr = models.CharField(max_length=200, blank=True, verbose_name=u'EMPRESA:')
    ocupacion = models.CharField(max_length=200, blank=True, verbose_name=u'OCUPACION:')
    anos_trabajo = models.CharField(max_length=200, blank=True, verbose_name=u'AÑOS DE TRABAJO:')
    tiempo_exposicion = models.CharField(max_length=200, blank=True,verbose_name=u'TIEMPO DE EXPOSICION A RUIDO (8 HR):')
    apresiacion_ruido = models.CharField(max_length=1, choices=RUIDOS, blank=True, verbose_name=u'APRECIACION DEL RUIDO:')
    audiometria_ante = models.CharField(max_length=200, blank=True, verbose_name=u'AUDIOMETRIA ANTERIOR:')
    resul_audiomet = models.CharField(max_length=200, blank=True, verbose_name=u'RESULTADOS DE AUDIOMETRIA:')
    antecedentes = models.CharField(max_length=200, blank=True, verbose_name=u'ANTECEDENTES:')
    med_ototoxicos = models.BooleanField(default=True, blank=True, verbose_name=u'MEDICINA OTOTOXICOS:')
    meningitis = models.BooleanField(default=True, blank=True, verbose_name=u'MENINGITIS:')
    sarampion = models.BooleanField(default=True, blank=True, verbose_name=u'SARAMPION')
    parotiditis = models.BooleanField(default=True, blank=True, verbose_name=u'PAROTIDITIS:')
    buceo = models.BooleanField(default=True, blank=True, verbose_name=u'BUCEO:')
    exp_quimico = models.BooleanField(default=True, blank=True, verbose_name=u'EXP. QUIMICO:')
    discotecas = models.BooleanField(default=True, blank=True, verbose_name=u'DISCOTECAS:')
    trauma_acustico = models.BooleanField(default=True, blank=True, verbose_name=u'TRAUMA ACUSTICO:')
    expos_laboral_ruido = models.BooleanField(default=True, blank=True, verbose_name=u'EXPOS. LABORAL AL RUIDO:')
    tec = models.BooleanField(default=True, blank=True, verbose_name=u'TEC:')
    armas_fuego = models.BooleanField(default=True, blank=True, verbose_name=u'USO DE ARMAS DE FUEGO:')
    audifonos = models.BooleanField(default=True, blank=True, verbose_name=u'AUDIFONOS:')
    tapones = models.CharField(max_length=1, choices=CONDICIONALES, blank=True, verbose_name=u'TAPONES:')
    orejeras = models.CharField(max_length=1, choices=CONDICIONALES, blank=True, verbose_name=u'OREJERAS:')
    algodones = models.CharField(max_length=1, choices=CONDICIONALES, blank=True, verbose_name=u'ALGODONES:')
    sistomatologia = models.CharField(max_length=200, blank=True, verbose_name=u'SISTOMATOLOGIA')
    viaje_reciente = models.BooleanField(default=True, blank=True, verbose_name=u'VIAJE RECIENTE < 6 HORAS:')
    exp_recien_ruid18 = models.BooleanField(default=True, blank=True, verbose_name=u'EXPOSICION RECIENTE A RUIDOS (18 HORAS)')
    acutenos = models.BooleanField(default=True, blank=True, verbose_name=u'ACUTENOS:')
    hipoacusia = models.BooleanField(default=True, blank=True, verbose_name=u'HIPOACUSIA:')
    otalgia = models.BooleanField(default=True, blank=True, verbose_name=u'OTALGIA:')
    enf_tra_respiratorio = models.BooleanField(default=True, blank=True, verbose_name=u'ENF. DEL TRACTO RESPIRATORIO ACTUAL:')
    secresion_otica = models.BooleanField(default=True, blank=True, verbose_name=u'SECRECION OTICA')
    vertigo = models.BooleanField(default=True, blank=True, verbose_name=u'VERTIGO:')
    garganta_normal = models.BooleanField(default=False, blank=True, verbose_name=u'GARGANTA NORMAL')
    garganta_anormal = models.BooleanField(default=False, blank=True, verbose_name=u'GARGANTA ANORMAL')
    oido_normal = models.BooleanField(default=False, blank=True, verbose_name=u'OIDO NORMAL')
    oido_anormal = models.BooleanField(default=False, blank=True, verbose_name=u'OIDO ANORMAL')
    otoscopia_od = models.BooleanField(default=False, blank=True, verbose_name=u'OTOSCOPIA O.D.:')
    otoscopia_oi = models.BooleanField(default=False, blank=True, verbose_name=u'OTOSCOPIA O.I.:')
    diapaz_od_250hz = models.BooleanField(default=False, blank=True, verbose_name=u'DIAPAZONES OIDO DERECHO 250 Hz:')
    diapaz_od_500hz = models.BooleanField(default=False, blank=True, verbose_name=u'DIAPAZONES OIDO DERECHO 500 Hz')
    diapaz_od_1000hz = models.BooleanField(default=False, blank=True, verbose_name=u'DIAPAZONES OIDO DERECHO 1000 Hz')
    diapaz_oi_250hz = models.BooleanField(default=False, blank=True, verbose_name=u'DIAPAZONES OIDO IZQUIERDO 250 Hz')
    diapaz_oi_500hz = models.BooleanField(default=False, blank=True, verbose_name=u'DIAPAZONES OIDO IZQUIERDO 500 Hz')
    diapaz_oi_1000hz = models.BooleanField(default=False, blank=True, verbose_name=u'DIAPAZONES OIDO IZQUIERDO 1000 Hz')
    medico = models.CharField(max_length=200, blank=True, verbose_name=u'MEDICO')
    concluciones = models.CharField(max_length=200, blank=True, verbose_name=u'CONCLUCIONES')

    def get_absolute_url(self):
        """Obtiene la URL absoluta"""

        return reverse('persona-view-id', args=[self.persona.id])


class Antecedente(models.Model):
    """Describe el historial clínico de una :class:`Persona` al llegar a
    consulta por primera vez
    """
    HABITOS = (
        ("N", u'NADA'),
        ("P", u'POCO'),
        ("H", u'HABITUAL'),
        ("E", u'EXESIVO'),
    )

    CONDICION = (
        ("0", u'SI'),
        ("1", u'NO'),
    )

    CONDICIONALES = (
        ("A", u'A VECES'),
        ("B", u'SIEMPRE'),
        ("C", u'NUNCA'),
    )

    RUIDOS = (
        ("I", u'MUY INTENSO'),
        ("M", u'MODERADO'),
        ("O", u'NO MOLESTO'),
    )

    APTITUD = (
        ("A", u'APTO'),
        ("N", u'NO APTO'),
    )

    persona = models.OneToOneField(Persona, primary_key=True)

    # complete = models.BooleanField(default=False, blank=True)
    # reaction = models.BooleanField(default=False, blank=True)
    ruido = models.BooleanField(default=False, blank=True, verbose_name=u'RUIDO')
    polvo = models.BooleanField(default=False, blank=True, verbose_name=u'POLVO')
    vibracion = models.BooleanField(default=False, blank=True, verbose_name=u'VIBRACION')
    segmentaria = models.BooleanField(default=False, blank=True, verbose_name=u'SEGMENTARIA')
    vibracion_total = models.BooleanField(default=False, blank=True, verbose_name=u'VIBRACION TOTAL')
    cancerigeno = models.BooleanField(default=False, blank=True, verbose_name=u'CANCERIGENO')
    mutagenico = models.BooleanField(default=False, blank=True, verbose_name=u'MUTAGENICOS')
    metales = models.BooleanField(default=False, blank=True, verbose_name=u'MENTALES')
    pesados = models.BooleanField(default=False, blank=True, verbose_name=u'PESADOS')
    solvente = models.BooleanField(default=False, blank=True, verbose_name=u'SOLVENTE')
    temperatura = models.BooleanField(default=False, blank=True, verbose_name=u'TEMPERATURA')
    biologico = models.BooleanField(default=False, blank=True, verbose_name=u'BIOLOGICO')
    postura = models.BooleanField(default=False, blank=True, verbose_name=u'POSTURA')
    turno_noche = models.BooleanField(default=False, blank=True, verbose_name=u'TURNOS NOCHE')
    carga = models.BooleanField(default=False, blank=True, verbose_name=u'CARGAS')
    movimiento = models.BooleanField(default=False, blank=True, verbose_name=u'MOVIMIENTO')
    repetitivo = models.BooleanField(default=False, blank=True, verbose_name=u'REPETITIVO')
    otros_a = models.BooleanField(default=False, blank=True, verbose_name=u'OTROS')
    postula = models.CharField(max_length=200, blank=True, verbose_name=u'PUESTO AL QUE POSTULA:')
    hta = models.BooleanField(default=False, blank=True, verbose_name=u'HTA:')
    dm = models.BooleanField(default=False, blank=True, verbose_name=u'DM:')
    asma = models.BooleanField(default=False, blank=True, verbose_name=u'ASMA:')
    ram = models.BooleanField(default=False, blank=True, verbose_name=u'RAM:')
    h_tg = models.BooleanField(default=False, blank=True, verbose_name=u'H.Tg:')
    h_col = models.BooleanField(default=False, blank=True, verbose_name=u'H.Col:')
    prob_cv = models.BooleanField(default=False, blank=True, verbose_name=u'Prob.CV:')
    alergias = models.CharField(max_length=200, blank=True, null=True)
    artropatia = models.BooleanField(default=False, blank=True, verbose_name=u'ARTROPATIA:')
    pt_columna = models.BooleanField(default=False, blank=True, verbose_name=u'PT.COLUMNA:')
    hpb = models.BooleanField(default=False, blank=True, verbose_name=u'HPB:')
    migrana = models.BooleanField(default=False, blank=True, verbose_name=u'MIGRAÑA:')
    cirugia = models.BooleanField(default=False, blank=True)
    sd_metabolico = models.BooleanField(default=False, blank=True, verbose_name=u'SD. METABOLICO:')
    cancer = models.BooleanField(default=False, blank=True, verbose_name=u'CANCER:')
    problema_renal = models.BooleanField(default=False, blank=True, verbose_name=u'PROBLEMA RENAL:')
    medicacion_actual = models.CharField(max_length=200, blank=True, null=True, verbose_name=u'MEDICACION ACTUAL:')
    tabaco = models.CharField(max_length=1, choices=HABITOS, blank=True, verbose_name=u'HABITOS TABACO:')
    coca = models.CharField(max_length=1, choices=HABITOS, blank=True, verbose_name=u'HABITOS COCA:')
    alcohol = models.CharField(max_length=1, choices=HABITOS, blank=True, verbose_name=u'HABITOS ALCOHOL:')
    otros_b = models.CharField(max_length=200, blank=True, verbose_name=u'OBSERVACIONES:')

    ectoscopia = models.BooleanField(default=False, blank=True, verbose_name=u'ECTOSCOPIA:')
    abec = models.BooleanField(default=False, blank=True, verbose_name=u'ABEC:')
    abeh = models.BooleanField(default=False, blank=True, verbose_name=u'ABEH:')
    aben = models.BooleanField(default=False, blank=True,verbose_name=u'ABEN:')
    lotep = models.BooleanField(default=False, blank=True, verbose_name=u'LOTEP:')
    anormalidades = models.CharField(max_length=200, blank=True, verbose_name=u'ANORMALIDADES:')
    desc_b = models.CharField(max_length=200, blank=True, verbose_name=u'DESCRIPCION')
    boca_amigdalas = models.BooleanField(default=False, blank=True, 
                                        help_text=u'labios sin lesiones mucosa oral rosada brillante congestiva',
                                        verbose_name=u'BOCA AMIGDALAS, FARINGE, LARINGE')
    anorma_a = models.BooleanField(default=False, blank=True, verbose_name='ANORMALIDADES')
    descr_c = models.CharField(max_length=200, blank=True, verbose_name=u'DESCRIPCION')
    genitales_normal = models.BooleanField(default=False, blank=True, verbose_name='GENITALES NORMALES')
    genitales_anormal = models.BooleanField(default=False, blank=True, verbose_name='GENITALES ANORMAL')
    desc_d = models.CharField(max_length=200, blank=True, verbose_name=u'DESCRIPCION')
    cuello_normal = models.BooleanField(default=False, blank=True, verbose_name=u' CUELLO NORMAL')
    cuello_anormal = models.BooleanField(default=False, blank=True, verbose_name=u'CUELLO ANORMAL')
    desc_e = models.CharField(max_length=200, blank=True, verbose_name=u'DESCRIPCION')
    nariz_normal = models.BooleanField(default=False, blank=True, verbose_name=u'NARIZ NORMAL')
    nariz_anormal = models.BooleanField(default=False, blank=True, verbose_name=u'NARIZ ANORMAL') 
    desc_f = models.CharField(max_length=200, blank=True, verbose_name=u'DESCRIPCION', help_text=u'DENTADURA ODONTOGRAMA DE ACUERDO A MINSA')
    '''dentadura Odontograma de acuerdo a minsa'''
    edentulo_parcial = models.CharField(max_length=1, choices=CONDICION, blank=True, verbose_name=u'EDENTULO PARCIAL')
    edentulo_total = models.CharField(max_length=1, choices=CONDICION, blank=True, verbose_name=u'EDENTULO TOTAL')
    ppf = models.CharField(max_length=1, choices=CONDICION, blank=True, verbose_name=u'PPF')
    gingivitis = models.CharField(max_length=1, choices=CONDICION, blank=True, verbose_name=u'GINGIVITIS')
    ppr = models.CharField(max_length=1, choices=CONDICION, blank=True, verbose_name=u'PPR')
    piezas_mal_estado = models.CharField(max_length=200, blank=True, verbose_name=u'PIEZAS EN MAL ESTADO' )
    piezas_faltan = models.CharField(max_length=200, blank=True, verbose_name=u'PIEZAS QUE FALTAN', help_text=u'EXAMENES DE LOS OJOS')
    '''ojos'''
    v_c_o_d_sin_corregir = models.CharField(max_length=20, blank=True, verbose_name=u'OJO DER. S/C Visión de Cerca:')
    v_l_o_d_sin_corregir = models.CharField(max_length=20, blank=True, verbose_name=u'OJO DER. S/C Visión de Lejos:')
    v_c_o_i_sin_corregir = models.CharField(max_length=20, blank=True, verbose_name=u'OJO IZQ. S/C Visión de Cerca:')
    v_l_o_i_sin_corregir = models.CharField(max_length=20, blank=True, verbose_name=u'OJO IZQ. S/C Visión de Lejos:')
    v_c_o_d_corregida = models.CharField(max_length=20, blank=True, verbose_name=u'OJO DER. CORREGIDA Visión de Cerca:')
    v_l_o_d_corregida = models.CharField(max_length=20, blank=True, verbose_name=u'OJO DER. CORREGIDA Visión de Cerca:')
    v_c_o_i_corregida = models.CharField(max_length=20, blank=True, verbose_name=u'OJO IZQ. CORREGIDA Visión de Cerca:')
    v_l_o_i_corregida = models.CharField(max_length=20, blank=True, verbose_name=u'OJO IZQ. CORREGIDA Visión de Cerca:')
    vision_colores_normal =  models.CharField(max_length=1, choices=CONDICION, blank=True, verbose_name=u'VISION DE COLORES')
    vision_colores_nistagnos = models.CharField(max_length=1, choices=CONDICION, blank=True, verbose_name=u'VISION DE COLORES NISTAGNOS')
    Enfermedad_ocular_descrip = models.CharField(max_length=200, blank=True, verbose_name=u'ENF. OCULAR DESC.')
    sin_alteraciones = models.CharField(max_length=200, blank=True, verbose_name=u'SIN ALTERACIONES', help_text=u'EXAMENES DE LOS OIDOS DERECHO E IZQUIERDO')

    t_d_triangulo_de_luz= models.CharField(max_length=1, choices=CONDICION, blank=True, verbose_name=u'TIMPANO DER. TRIANGULO DE LUZ')
    t_d_perforaciones = models.CharField(max_length=1, choices=CONDICION, blank=True, verbose_name=u'TIMPANO DER. PERFORACIONES')
    t_d_abombamiento = models.CharField(max_length=1, choices=CONDICION, blank=True, verbose_name=u'TIMPANO DER. ABOMBAMIENTO')
    t_d_tapon_cerumen = models.CharField(max_length=1, choices=CONDICION, blank=True, verbose_name=u'TIMPANO DER. TAPON CERUMEN')
    t_d_observaciones = models.CharField(max_length=100, blank=True, verbose_name=u'TIMPANO DERECHO OBSERVACIONES')
    t_i_triangulo_de_luz= models.CharField(max_length=1, choices=CONDICION, blank=True, verbose_name=u'TIMPANO IZQ. TRIANGULO DE LUZ')
    t_i_perforaciones = models.CharField(max_length=1, choices=CONDICION, blank=True,verbose_name=u'TIMPANO IZQ. PERFORACIONES')
    t_i_abombamiento = models.CharField(max_length=1, choices=CONDICION, blank=True, verbose_name=u'TIMPANO IZQ. ABOMBAMIENTO')
    t_i_tapon_cerumen = models.CharField(max_length=1, choices=CONDICION, blank=True, verbose_name=u'TIMPANO IZQ. TAPON CERUMEN')
    t_i_observaciones = models.CharField(max_length=100, blank=True, verbose_name=u'TIMPANO IZQUIERDO OBSERVACIONES')
    audicion_d_hz_500 = models.CharField(max_length=20, blank=True, verbose_name=u'AUD. DER. Hz 500')
    audicion_d_hz_1000 = models.CharField(max_length=20, blank=True, verbose_name=u'AUD. DER. Hz 1000')
    audicion_d_hz_2000 = models.CharField(max_length=20, blank=True, verbose_name=u'AUD. DER. Hz 2000')
    audicion_d_hz_3000 = models.CharField(max_length=20, blank=True, verbose_name=u'AUD. DER. Hz 3000')
    audicion_d_hz_4000 = models.CharField(max_length=20, blank=True, verbose_name=u'AUD. DER. Hz 4000')
    audicion_d_hz_6000 = models.CharField(max_length=20, blank=True, verbose_name=u'AUD. DER. Hz 6000')
    audicion_d_hz_8000 = models.CharField(max_length=20, blank=True, verbose_name=u'AUD. DER. Hz 8000')
    derecha_conservada = models.BooleanField(default=False, blank=True, verbose_name=u'AUD. DER. CONSERVADA')
    comentario = models.CharField(max_length=200, blank=True, verbose_name=u'COMENTARIO')
    audicion_i_hz_500 = models.CharField(max_length=20, blank=True, verbose_name=u'AUD. IZQ. Hz 500')
    audicion_i_hz_1000 = models.CharField(max_length=20, blank=True, verbose_name=u'AUD. IZQ. Hz 1000')
    audicion_i_hz_2000 = models.CharField(max_length=20, blank=True, verbose_name=u'AUD. IZQ. Hz 2000')
    audicion_i_hz_3000 = models.CharField(max_length=20, blank=True, verbose_name=u'AUD. IZQ. Hz 3000')
    audicion_i_hz_4000 = models.CharField(max_length=20, blank=True, verbose_name=u'AUD. IZQ. Hz 4000')
    audicion_i_hz_6000 = models.CharField(max_length=20, blank=True, verbose_name=u'AUD. IZQ. Hz 6000')
    audicion_i_hz_8000 = models.CharField(max_length=20, blank=True, verbose_name=u'AUD. IZQ. Hz 8000')
    izquierdo_conservada = models.BooleanField(default=False, blank=True, verbose_name=u'AUD. IZQ. CONSERVADA')
    comentarios = models.CharField(max_length=200, blank= True, verbose_name=u'COMENTARIO', help_text=u'EXAMENES DE TORAX ECTOSCOPIA')

    '''torax corazon'''
    torax_ectoscopia_normal = models.BooleanField(default=False, blank=True, verbose_name='ECTOSCOPIA NORMAL')
    torax_ectoscopia_anormal = models.BooleanField(default=False, blank=True, verbose_name='ANORMAL')
    desc_g = models.CharField(max_length=200, blank=True, verbose_name=u'DESCRIPCION')
    corazon_normal = models.BooleanField(default=False, blank=True, verbose_name='CORAZON NORMAL')
    corazon_anormal = models.BooleanField(default=False, blank=True, verbose_name='ANORMAL')
    desc_h = models.CharField(max_length=200, blank=True, verbose_name=u'DESCRIPCION')
    pulmones_normal = models.BooleanField(default=False, blank=True, verbose_name='PULMONES NORMAL')
    pulmones_anormal = models.BooleanField(default=False, blank=True, verbose_name='ANORMAL')
    desc_i = models.CharField(max_length=200, blank=True, verbose_name=u'DESCRIPCION')
    '''sistema oseo mio articular'''

    miembro_sup_der_normal = models.BooleanField(default=False, blank=True, verbose_name=u'MIENBRO SUP. DERECHO NORMAL' )
    mienbro_sup_der_anormal = models.BooleanField(default=False, blank=True, verbose_name=u'MIENBRO SUP. DERECHO ANORMAL')
    desc_j = models.CharField(max_length=200, blank=True, verbose_name=u'DESCRIPCION')
    miembro_sup_izq_normal = models.BooleanField(default=False, blank=True, verbose_name=u'MIENBRO SUP. IZQUIERDO NORMAL')
    miembro_sup_izq_anormal = models.BooleanField(default=False, blank=True, verbose_name=u'MIENBRO SUP. IZQUIERDO ANORMAL')
    desc_k = models.CharField(max_length=200, blank=True, verbose_name=u'DESCRIPCION')
    miembro_infe_der_normal = models.BooleanField(default=False, blank=True, verbose_name=u'MIENBRO INF. DERECHO NORMAL')
    miembro_infe_der_anormal = models.BooleanField(default=False, blank=True,verbose_name=u'MIENBRO INF. DERECHO ANORMAL')
    desc_l = models.CharField(max_length=200, blank=True, verbose_name=u'DESCRIPCION')
    miembro_infe_izq_normal = models.BooleanField(default=False, blank=True, verbose_name=u'MIENBRO INF. IZQUIERDO NORMAL')
    miembro_infe_izq_anormal = models.BooleanField(default=False, blank=True, verbose_name=u'MIENBRO INF. IZQUIERDO ANORMAL')
    desc_m = models.CharField(max_length=200, blank=True, verbose_name=u'DESCRIPCION')
    presentes = models.BooleanField(default=False, blank=True, verbose_name=u'PRESENTES' )
    normoreflexia = models.BooleanField(default=False, blank=True, verbose_name=u'NORMOREFLEXIA')
    hipereflexia = models.BooleanField(default=False, blank=True, verbose_name=u'HIPEREFLEXIA')
    marcha_conservada = models.CharField(max_length=200, blank=True, verbose_name=u'MARCHA CONSERVADA')
    columna_vert_normal = models.BooleanField(default=False, blank=True, verbose_name=u'COLUMNA VERTEBRAL NORMAL')
    columna_vert_anormal = models.BooleanField(default=False, blank=True, verbose_name=u'COLUMAN VERTEBRAL ANORMAL')
    desc_n = models.CharField(max_length=200, blank=True, verbose_name=u'DESCRIPCION')
    '''abdomen'''
    abdomen_normal = models.BooleanField(default=False, blank=True, verbose_name=u'ABDOMEN NORMAL')
    abdomen_anormal = models.BooleanField(default=False, blank=True, verbose_name=u'ANORMALIDADES')
    desc_l = models.CharField(max_length=200, blank= True, verbose_name=u'DESCRIPCION')
    pru_sup_der = models.CharField(max_length=1, choices=CONDICION, blank=True, verbose_name=u'PRU Sup Drch')
    pru_sup_izq = models.CharField(max_length=1, choices=CONDICION, blank=True, verbose_name=u'PRU Sup Izq.')
    pru_med_der = models.CharField(max_length=1, choices=CONDICION, blank=True, verbose_name=u'PRU Med Drch')
    pru_med_izq = models.CharField(max_length=1, choices=CONDICION, blank=True, verbose_name=u'PRU Med Izq')
    prl_der = models.CharField(max_length=1, choices=CONDICION, blank=True, verbose_name=u'PRL Drch')
    prl_izq = models.CharField(max_length=1, choices=CONDICION, blank=True, verbose_name=u'PRL Izq')
    hernias = models.CharField(max_length=1, choices=CONDICION, blank=True, verbose_name=u'HERNIAS')
    varices = models.CharField(max_length=1, choices=CONDICION, blank=True, verbose_name=u'VARICES')
    funciones_superiores = models.BooleanField(default=False, blank=True, verbose_name=u'FUNCIONES SUP. CONSERVADA')
    psicologico = models.CharField(max_length=1, choices=APTITUD, blank=True, verbose_name=u'PSICOLOGICO')


    def get_absolute_url(self):
        """Obtiene la URL absoluta"""

        return reverse('persona-view-id', args=[self.persona.id])


class AntecedenteFamiliar(models.Model):
    """Registra los antecedentes familiares de una :class:`Persona`"""

    persona = models.OneToOneField(Persona, primary_key=True,
                                   related_name='antecedente_familiar')
    mama = models.CharField(max_length=200, blank=True, verbose_name=u'MAMA:')
    papa = models.CharField(max_length=200, blank=True, verbose_name=u'PAPA:')
    hermano = models.CharField(max_length=200, blank=True, verbose_name=u'HERMANO:')
    sin_importancia = models.BooleanField(default=False, blank=True,
                                                   verbose_name=u'SIN IMPORTANCIA')
    con_importancia = models.BooleanField(default=False, blank=True,
                                                   verbose_name=u'CON IMPORTANCIA')
    vivos = models.BooleanField(default=False, blank=True)
    n_hijos = models.CharField(max_length=100, blank=True, verbose_name=u'N° DE HIJOS:')
    otros = models.CharField(max_length=200, blank=True)

    def get_absolute_url(self):
        """Obtiene la URL absoluta"""

        return reverse('persona-view-id', args=[self.persona.id])


class AntecedenteObstetrico(models.Model):
    """Registra los antecedentes obstetricos de una :class:`Persona`"""

    persona = models.OneToOneField(Persona, primary_key=True,
                                   related_name='antecedente_obstetrico')

    menarca = models.DateField(default=date.today)
    ultimo_periodo = models.DateField(null=True, blank=True)
    gestas = models.IntegerField(default=0)
    partos = models.IntegerField(default=0)
    cesareas = models.IntegerField(default=0)
    otros = models.CharField(max_length=200, blank=True)
    displasia = models.BooleanField(default=False, blank=True)
    anticoncepcion = models.BooleanField(default=False, blank=True)

    def get_absolute_url(self):
        """Obtiene la URL absoluta"""

        return reverse('persona-view-id', args=[self.persona.id])


class Empleador(TimeStampedModel):
    nombre = models.CharField(max_length=200, blank=True)
    direccion = models.TextField()

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('empresa', args=[self.id])


class Sede(TimeStampedModel):
    empleador = models.ForeignKey(Empleador, null=True, blank=True,
                                  related_name='sedes')
    lugar = models.CharField(max_length=200, blank=True)
    direccion = models.TextField()

    def __unicode__(self):
        return u'{0} de {1}'.format(self.lugar, self.empleador.nombre)


class Empleo(TimeStampedModel):
    empleador = models.ForeignKey(Empleador, null=True, blank=True,
                                  related_name='empleos')
    sede = models.ForeignKey(Sede, related_name='empleos', null=True,
                             blank=True)
    persona = models.ForeignKey(Persona, related_name='empleos')
    numero_empleado = models.CharField(max_length=200, blank=True, null=True)

    def get_absolute_url(self):
        return self.persona.get_absolute_url()


class PuestoTrabajo(TimeStampedModel):
    puesto = models.CharField(max_length=200, blank=True, null=True)

    def get_absolute_url(self):
        return self.persona.get_absolute_url()

class AntecedenteQuirurgico(models.Model):
    """Registra los antecendentes quirurgicos de una :class:`Persona`"""

    persona = models.ForeignKey(Persona,
                                related_name="antecedentes_quirurgicos")
    procedimiento = models.CharField(max_length=200, blank=True)
    fecha = models.CharField(max_length=200, blank=True)

    def get_absolute_url(self):
        """Obtiene la URL absoluta"""

        return self.persona.get_absolute_url()

def create_persona(sender, instance, created, **kwargs):
    if created:
        fisico = Fisico(persona=instance)
        fisico.save()
        estilo_vida = EstiloVida(persona=instance)
        estilo_vida.save()
        antecedente = Antecedente(persona=instance)
        antecedente.save()
        antecedente_familiar = AntecedenteFamiliar(persona=instance)
        antecedente_familiar.save()

        if instance.sexo == 'F':
            antecedente_obstetrico = AntecedenteObstetrico(persona=instance)
            antecedente_obstetrico.save()


post_save.connect(create_persona, sender=Persona)

persona_consolidation_functions = []


def remove_duplicates():
    count = Persona.objects.filter(duplicado=True).count()
    persona = Persona.objects.filter(duplicado=True).first()

    if count == 1:
        persona.duplicado = False
        persona.save()

    while persona and count > 1:
        print(persona)
        consolidate_into_persona(persona)
        persona = Persona.objects.filter(duplicado=True).first()
        count = Persona.objects.filter(duplicado=True).count()


def consolidate_into_persona(persona):
    clones = Persona.objects.filter(nombre__iexact=persona.nombre,
                                    duplicado=True,
                                    apellido__iexact=persona.apellido,
                                    identificacion=persona.identificacion).exclude(
        pk=persona.pk)
    print(clones.count())
    for clone in clones.all():
        print(clone)

    [move_persona(persona, clone) for clone in clones.all()]
    persona.duplicado = False
    persona.save()


def move_persona(persona, clone):
    [function(persona, clone) for function in persona_consolidation_functions]
    print(u"Removing persona")
    clone.delete()


def transfer_object_to_persona(entity, persona):
    entity.persona = persona
    entity.save()
