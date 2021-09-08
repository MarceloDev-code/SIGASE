from django.shortcuts import render

# Create your views here.
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny
from sello.models import *
from sello.forms import *
from sello.serializers import *


@login_required
def inicio(request):
    """
     Página inicial del sitio

    :param request: Django request
    :return: Html
    """
    ctx = {}

    return render(
        request,
        'directorio/inicio.html',
        ctx
    )


### CRUD ALUMNOS
@login_required
def estudiante(request):

   #listado de estudiante
   
    ctx = {}
    listado_estudiante = estudiante.objects.all()
    filtro = request.GET.get('filtro', None)
    if filtro:
        listado_estudiante = listado_estudiante.filter(
            Q(nombres__icontains=filtro) |
            Q(apellidoPaterno__icontains=filtro) |
            Q(ApellidoMaterno__icontains=filtro) |
            Q(apellidos__icontains=filtro) |
            Q(rut__icontains=filtro) |
            Q(rut_sin_formato__icontains=filtro)
        )

    paginator = Paginator(listado_estudiante, 10)

    page = request.GET.get('page')
    try:
        d_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        d_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        d_list = paginator.page(paginator.num_pages)

    ctx['estudiante'] = d_list

    return render(
        request,
        'directorio/estudiante/estudiante.html',
        ctx
    )


@login_required
def mostrar_estudiante(request, id_estudiante):
    """
     Mostrar detalle de estudiante

    :param request: Django request
    :param id_estudiante: ID de modelo Persona
    :return: Html
    """

    ctx = {}
    estudiante = estudiante.objects.get(id=id_estudiante)
    ctx['estudiante'] = estudiante

    return render(
        request,
        'directorio/estudiante/mostrar_estudiante.html',
        ctx

    )

@login_required
def crear_estudiante(request):
    """
     Crea un nuevo registro de estudiante asociado al modelo
     Persona

    :param request: Django request
    :return: Html
    """
    ctx = {}

    if request.method == "POST":
        form = estudianteForm(request.POST)
        if form.is_valid():
            obj = form.save()
            messages.success(
                request,
                u"Persona <strong>{}</strong> creada satisfactoriamente...".format(
                    obj.nombre_completo()
                )
            )
            return redirect(
                'reserva:estudiante'
            )

    else:
        form = estudianteForm()

    ctx['form'] = form

    return render(
        request,
        'directorio/estudiante/crear_estudiante.html',
        ctx
    )


@login_required
def editar_estudiante(request, rut_estudiante):
    """
     Función para actualizar una estudiante por su id

    :param request: Django request
    :param id_estudiante: ID modelo Persona
    :return: Html
    """
    ctx = {}
    estudiante = get_object_or_404(
        id=rut_estudiante,
        estudiante
    )

    if request.method == "POST":
        form = estudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            obj = form.save()
            messages.success(
                request,
                u"Persona <strong>{}</strong> actualizada satisfactoriamente...".format(
                    obj.nombre_completo()
                )
            )
            return redirect(
                'reserva:estudiante'
            )
    else:
        form = estudianteForm(instance=estudiante)

    ctx['estudiante'] = estudiante
    ctx['form'] = form

    return render(
        request,
        'directorio/estudiante/editar_estudiante.html',
        ctx
    )


@login_required
def eliminar_estudiante(request, id_estudiante):
    """
    Elimina un registro de estudiante de la base de datos

    :param request: Django request
    :param id_estudiante: ID Persona
    :return:
    """
    ctx = {}
    ninja = estudiante.objects
    estudiante = get_object_or_404(
        estudiante,
        pk=id_estudiante
    )
    if request.method == "POST":
        nombre = estudiante.nombre_completo()

        messages.error(
            request,
            u"el profesor <strong>{}</strong> ha sido eliminada satisfactoriamente...".format(
                nombre
            )
        )
        estudiante.delete()
        return redirect(
            'reserva:estudiante'
        )

    ctx['profesor'] = estudiante

    return render(
        request,
        'directorio/estudiante/eliminar_estudiante.html',
        ctx
    )



### CRUD asignatura ##

@login_required
def asignaturas(request):
    """
     Listado de estudiante


    :param request: Django request
    :return: Html
    """
    ctx = {}
    listado_estudiante = asignatura.objects.all()
    filtro = request.GET.get('filtro', None)
    if filtro:
        listado_estudiante = listado_estudiante.filter(
            Q(idAsignatura__icontains=filtro) |
            Q(nombreAsignatura__icontains=filtro) |
            Q(facultad__icontains=filtro)
        )

    paginator = Paginator(listado_estudiante, 10)

    page = request.GET.get('page')
    try:
        d_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        d_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        d_list = paginator.page(paginator.num_pages)

    ctx['asignatura'] = d_list

    return render(
        request,
        'directorio/estudiante/asignaturas.html',
        ctx
    )

@login_required
def crear_asignatura(request):
    """
     Crea un nuevo registro de directorio asociado al modelo
     directorio

    :param request: Django request
    :return: Html
    """
    ctx = {}

    if request.method == "POST":
        form = AsignaturaForm(request.POST)
        if form.is_valid():
            obj = form.save()
            messages.success(
                request,
                u"asignatura creada satisfactoriamente..."
                )


            return redirect(
                'reserva:inicio'
            )

    else:
        form = AsignaturaForm()

    ctx['form'] = form

    return render(
        request,
        'directorio/asignatura/crear_asignatura.html',
        ctx
    )



@login_required
def eliminar_asignatura(request, id_asignatura):
    """
    Elimina un registro de departamento de la base de datos

    :param request: Django request
    :param id_departamento: ID modelo Departamento
    :return:
    """
    ctx = {}

    directorio = get_object_or_404(
        asignatura,
        pk=id_asignatura
    )
    if request.method == "POST":
        id_asignatura = asignatura.idAsignatura
        asignatura.delete()
        messages.error(
            request,
            u"El directorio <strong>{}</strong> ha sido eliminado satisfactoriamente...".format(
                id_asignatura
            )
        )

        return redirect(
            'reserva:inicio'
        )

    ctx['asignatura'] = asignatura

    return render(
        request,
        'directorio/asignatura/eliminar_asignatura.html',
        ctx
    )


@login_required
def editar_asignatura(request, id_asignatura):
    """
     Función para actualizar una directorio por su id

    :param request: Django request
    :param id_directorio: ID modelo directorio
    :return: Html
    """
    ctx = {}
    directorio = get_object_or_404(
        asignatura,
        id=id_asignatura
    )

    if request.method == "POST":
        form = AsignaturaForm(request.POST, instance=asignatura)
        if form.is_valid():
            obj = form.save()

            return redirect(
                'reserva:inicio',
                obj.id
            )
    else:
        form = AsignaturaForm(instance=asignatura)

    ctx['asignatura'] = asignatura
    ctx['form'] = form

    return render(
        request,
        'directorio/asignatura/editar_asignatura.html',
        ctx
    )

### CRUD modulos ##
@login_required
def modulos(request):
    """
     Listado de estudiante


    :param request: Django request
    :return: Html
    """
    ctx = {}
    listado_estudiante = Modulos.objects.all()
    filtro = request.GET.get('filtro', None)
    if filtro:
        listado_estudiante = listado_estudiante.filter(
            Q(idmodulo__icontains=filtro) |
            Q(idSala__icontains=filtro) |
            Q(capacidad__icontains=filtro)
        )

    paginator = Paginator(listado_estudiante, 10)

    page = request.GET.get('page')
    try:
        d_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        d_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        d_list = paginator.page(paginator.num_pages)

    ctx['Modulos'] = d_list

    return render(
        request,
        'directorio/modulos/modulos.html',
        ctx
    )

@login_required
def crear_modulo(request):
    """
     Crea un nuevo registro de directorio asociado al modelo
     directorio

    :param request: Django request
    :return: Html
    """
    ctx = {}

    if request.method == "POST":
        form = ModulosForm(request.POST)
        if form.is_valid():
            obj = form.save()

            return redirect(
                'reserva:inicio'
            )

    else:
        form = ModulosForm()

    ctx['form'] = form

    return render(
        request,
        'directorio/modulos/crear_modulos.html',
        ctx
    )



@login_required
def eliminar_modulos(request, id_modulo):
    """
    Elimina un registro de departamento de la base de datos

    :param request: Django request
    :param id_departamento: ID modelo Departamento
    :return:
    """
    ctx = {}

    modulo = get_object_or_404(
        Modulos,
        pk=id_modulo
    )
    if request.method == "POST":
        id_modulo = Modulos.idmodulo

        messages.error(
            request,
            u"La reserva <strong>{}</strong> ha sido eliminado satisfactoriamente...".format(
                id_modulo
            )
        )
        modulo.delete()
        return redirect(
            'reserva:modulos'
        )

    ctx['Modulos'] = modulo

    return render(
        request,
        'directorio/modulos/eliminar_modulos.html',
        ctx
    )



@login_required
def editar_modulos(request, id_modulo):
    """
     Función para actualizar una directorio por su id

    :param request: Django request
    :param id_directorio: ID modelo directorio
    :return: Html
    """
    ctx = {}
    modulo = get_object_or_404(
        Modulos,
       id=id_modulo
    )

    if request.method == "POST":
        form = ModulosForm(request.POST, instance=modulo)
        if form.is_valid():
            obj = form.save()
            messages.success(
                request,
                u"modulo actualizada satisfactoriamente..."
                )

            return redirect(
                    'reserva:modulos'
            )
    else:
        form = ModulosForm(instance=modulo)

    ctx['Modulos'] = modulo
    ctx['form'] = form

    return render(
        request,
        'directorio/reserva/editar_reservas.html',
        ctx
    )

### CRUD salas ##




@login_required
def eliminar_asignatura(request, id_sala):
    """
    Elimina un registro de departamento de la base de datos

    :param request: Django request
    :param id_departamento: ID modelo Departamento
    :return:
    """
    ctx = {}

    directorio = get_object_or_404(
        Sala,
        pk=id_sala
    )
    if request.method == "POST":
        id_sala = Sala.idSala
        asignatura.delete()
        messages.error(
            request,
            u"El directorio <strong>{}</strong> ha sido eliminado satisfactoriamente...".format(
                id_sala
            )
        )

        return redirect(
            'reserva:inicio'
        )

    ctx['Sala'] = Sala

    return render(
        request,
        'directorio/asignatura/eliminar_sala.html',
        ctx
    )


@login_required
def editar_sala(request, id_sala):
    """
     Función para actualizar una directorio por su id

    :param request: Django request
    :param id_directorio: ID modelo directorio
    :return: Html
    """
    ctx = {}
    sala = get_object_or_404(
        Sala,
       id=id_sala
    )

    if request.method == "POST":
        form = SalaForm(request.POST, instance=sala)
        if form.is_valid():
            obj = form.save()
            messages.success(
                request,
                u"sala actualizada satisfactoriamente..."
                )

            return redirect(
                    'reserva:salas'
            )
    else:
        form = SalaForm(instance=sala)

    ctx['Sala'] = sala
    ctx['form'] = form

    return render(
        request,
        'directorio/Salas/editar_sala.html',
        ctx
    )

### CRUD salas ##

@login_required
def salas(request):
    """
     Listado de estudiante


    :param request: Django request
    :return: Html
    """
    ctx = {}
    listado_estudiante = Sala.objects.all()
    filtro = request.GET.get('filtro', None)
    if filtro:
        listado_estudiante = listado_estudiante.filter(
            Q(idAsignatura__icontains=filtro) |
            Q(nombreAsignatura__icontains=filtro) |
            Q(facultad__icontains=filtro)
        )

    paginator = Paginator(listado_estudiante, 10)

    page = request.GET.get('page')
    try:
        d_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        d_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        d_list = paginator.page(paginator.num_pages)

    ctx['Sala'] = d_list

    return render(
        request,
        'directorio/Salas/salas.html',
        ctx
    )


@login_required
def crear_sala(request):
    """
     Crea un nuevo registro de directorio asociado al modelo
     directorio

    :param request: Django request
    :return: Html
    """
    ctx = {}

    if request.method == "POST":
        form = SalaForm(request.POST)
        if form.is_valid():
            obj = form.save()

            return redirect(
                'reserva:inicio'
            )

    else:
        form = SalaForm()

    ctx['form'] = form

    return render(
        request,
        'directorio/Salas/crear_sala.html',
        ctx
    )



@login_required
def eliminar_sala(request, id_sala):
    """
    Elimina un registro de departamento de la base de datos

    :param request: Django request
    :param id_departamento: ID modelo Departamento
    :return:
    """
    ctx = {}

    sala = get_object_or_404(
        Sala,
        pk=id_sala
    )
    if request.method == "POST":
        sala1 = Sala.idSala

        messages.error(
            request,
            u"El directorio <strong>{}</strong> ha sido eliminado satisfactoriamente...".format(
                sala1
            )
        )
        sala.delete()
        return redirect(
            'reserva:inicio'
        )

    ctx['Sala'] = sala

    return render(
        request,
        'directorio/Salas/eliminar_sala.html',
        ctx
    )


### CRUD reserva ##

@login_required
def reservas(request):
    """
     Listado de estudiante


    :param request: Django request
    :return: Html
    """
    ctx = {}
    listado_estudiante = Reserva.objects.all()
    filtro = request.GET.get('filtro', None)
    if filtro:
        listado_estudiante = listado_estudiante.filter(
            Q(id_Clase__icontains=filtro) |
            Q(id_Modulo__icontains=filtro) |
            Q(id_reserva__iconstains=filtro) |
            Q(start_date__icontains=filtro)
        )

    paginator = Paginator(listado_estudiante, 10)

    page = request.GET.get('page')
    try:
        d_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        d_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        d_list = paginator.page(paginator.num_pages)

    ctx['Reserva'] = d_list

    return render(
        request,
        'directorio/reserva/reservas.html',
        ctx
    )

@login_required
def crear_reserva(request):
    """
     Crea un nuevo registro de directorio asociado al modelo
     directorio

    :param request: Django request
    :return: Html
    """
    ctx = {}

    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            obj = form.save()

            return redirect(
                'reserva:inicio'
            )

    else:
        form = ReservaForm()

    ctx['form'] = form

    return render(
        request,
        'directorio/reserva/crear_reserva.html',
        ctx
    )




@login_required
def eliminar_reserva(request, id_reserva):
    """
    Elimina un registro de departamento de la base de datos

    :param request: Django request
    :param id_departamento: ID modelo Departamento
    :return:
    """
    ctx = {}

    reserva = get_object_or_404(
        Reserva,
        pk=id_reserva
    )
    if request.method == "POST":
        id_reserva = Reserva.id_reserva

        messages.error(
            request,
            u"La reserva <strong>{}</strong> ha sido eliminado satisfactoriamente...".format(
                id_reserva
            )
        )
        reserva.delete()
        return redirect(
            'reserva:inicio'
        )

    ctx['Reserva'] = Reserva

    return render(
        request,
        'directorio/reserva/eliminar_reserva.html',
        ctx
    )


@login_required
def editar_reserva(request, id_reserva):
    """
     Función para actualizar una directorio por su id

    :param request: Django request
    :param id_directorio: ID modelo directorio
    :return: Html
    """
    ctx = {}
    reserva = get_object_or_404(
        Reserva,
       id=id_reserva
    )

    if request.method == "POST":
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            obj = form.save()
            messages.success(
                request,
                u"reserva actualizada satisfactoriamente..."
                )

            return redirect(
                    'reserva:reservas'
            )
    else:
        form = ReservaForm(instance=reserva)

    ctx['Reserva'] = reserva
    ctx['form'] = form

    return render(
        request,
        'directorio/reserva/editar_reservas.html',
        ctx
    )
# LOGIN VIEWS
def iniciar_sesion(request):
    """
        Funcionar que permite a un usuario Django ingresar al sistema

    :param request: Django request
    :return: usuario ingresado
    """

    if request.method == "POST":
        print request.POST
        # viene un formulario
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:

                login(request, user)
                return redirect(
                    'reserva:inicio'
                )
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    u'Cuenta inactiva, comuniquese con el administrador'
                )
        else:
            messages.add_message(
                request,
                messages.WARNING,
                u'Error en su contraseña o nombre de usuario, vuelva a intentarlo.'
            )
    else:
        messages.add_message(
            request,
            messages.INFO,
            'Ingrese con su usuario'
        )

    return render(
        request,
        'registration/login.html'
    )


@login_required
def cerrar_sesion(request):
    """

    :param request:
    :return:
    """
    logout(request)
    return redirect(
        'login'
    )


# APIS

class PersonaViewSet(viewsets.ModelViewSet):
    http_method_names = ('get',)
    queryset = estudiante.objects.order_by('apellidos')
    serializer_class = estudianteSerializer
    filter_backends = (filters.SearchFilter, )
    # filter_fields = ('activo',)
    search_fields = ('nombres', 'apellidos', 'rut_sin_formato')


class ModuloViewSet(viewsets.ModelViewSet):
    http_method_names = ('get',)
    queryset = Modulos.objects.order_by('idSala')
    serializer_class = ModulosSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('idmodulo', 'isala', 'capacidad')


class asignaturaViewSet(viewsets.ModelViewSet):
    http_method_names = ('get',)
    queryset = asignatura.objects.order_by('nombreAsignatura')
    serializer_class = AsignaturaSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('idAsignatura', 'nombreAsignatura', 'facultad')


class salaViewSet(viewsets.ModelViewSet):
    http_method_names = ('get',)
    queryset = Sala.objects.order_by('idSala')
    serializer_class = SalaSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('idSala', 'nombre', 'capacidad')


class reservaViewSet(viewsets.ModelViewSet):
        http_method_names = ('get',)
        queryset = Reserva.objects.order_by('id1')
        serializer_class = ReservaSerializer
        filter_backends = (filters.SearchFilter,)
        search_fields = ('idreserva','id1', 'idasignatura','idModulos')


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    http_method_names = ('get', )
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('username',)
