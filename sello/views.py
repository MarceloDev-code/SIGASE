from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from crispy_forms.utils import render_crispy_form
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
def estudiantes(request):

   #listado de estudiante
   
    ctx = {}
    listado_estudiante = estudiante.objects.all()
    filtro = request.GET.get('filtro', None)
    if filtro:
        listado_estudiante = listado_estudiante.filter(
            Q(nombres__icontains=filtro) |
            Q(rut__icontains=filtro)
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

    ctx['estudiantes'] = d_list

    return render(
        request,
        'directorio/estudiantes/estudiante.html',
        ctx
    )


@login_required
def mostrar_estudiante(request, id_estudiante):
    """
     Mostrar detalle de estudiante

    :param request: Django request
    :param id_estudiante: ID de modelo estudiante
    :return: Html
    """

    ctx = {}
    estudiantes = estudiante.objects.get(
        estudiante,
        rut=id_estudiante)
    ctx['estudiantes'] = estudiantes

    return render(
        request,
        'directorio/estudiantes/mostrar_estudiante.html',
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
                u"Estudiante <strong>{}</strong> creado satisfactoriamente...".format(
                    obj.nombre_completo()
                )
            )
            return redirect(
                'estudiante'
            )

    else:
        form = estudianteForm()

    ctx['form'] = form

    return render(
        request,
        'directorio/estudiantes/crear_estudiante.html',
        ctx
    )


@login_required
def editar_estudiante(request, id_estudiante):
    """
     Función para actualizar una estudiante por su id

    :param request: Django request
    :param id_estudiante: ID modelo Persona
    :return: Html
    """
    ctx = {}
    estudiantes = get_object_or_404(
        estudiante, id=id_estudiante

    )

    if request.method == "POST":
        form = estudianteForm(request.POST, instance=estudiantes)
        if form.is_valid():
            obj = form.save()
            messages.success(
                request,
                u"Persona <strong>{}</strong> actualizada satisfactoriamente...".format(
                    obj.nombre_completo()
                )
            )
            return redirect(
                'estudiante'
            )
    else:
        form = estudianteForm(instance=estudiantes)

    ctx['estudiante'] = estudiantes
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

    estudiantes = get_object_or_404(
        estudiante,
        pk=id_estudiante
    )

    if request.method == "POST":
        nombre = estudiante.nombreCompleto()

        messages.error(
            request,
            u"el estudiante <strong>{}</strong> ha sido eliminada satisfactoriamente...".format(
                nombre
            )
        )
        estudiante.delete()
        return redirect(
            'estudiante'
        )

    ctx['estudiante'] = estudiante

    return render(
        request,
        'directorio/estudiante/eliminar_estudiante.html',
        ctx
    )

### CRUD actividad ##
@login_required
def actividades(request):
    """
     Listado de actividades sello


    :param request: Django request
    :return: Html
    """
    ctx = {}
    listado_actividades = curso.objects.all()
    filtro = request.GET.get('filtro', None)
    if filtro:
        listado_adctividades = listado_actividades.filter(
            Q(codigo__icontains=filtro) |
            Q(nombre__icontains=filtro) |
            Q(encargado__icontains=filtro)
        )

    paginator = Paginator(listado_actividades, 10)

    page = request.GET.get('page')
    try:
        d_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        d_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        d_list = paginator.page(paginator.num_pages)

    ctx['curso'] = d_list

    return render(
        request,
        'directorio/actividad/actividades.html',
        ctx
    )

@login_required
def crear_actividad(request):
    """
     Crea un nuevo registro de directorio asociado al modelo
     directorio

    :param request: Django request
    :return: Html
    """
    ctx = {}

    if request.method == "POST":
        form = cursoForm(request.POST)
        if form.is_valid():
            obj = form.save()

            return redirect(
                'inicio'
            )

    else:
        form = cursoForm

    ctx['form'] = form

    return render(
        request,
        'directorio/actividad/crear_actividad.html',
        ctx
    )



@login_required
def eliminar_actividad(request, id_actividad):
    """
    Elimina una actividad

    :param request: Django request
    :param id_departamento: ID modelo Departamento
    :return:
    """
    ctx = {}

    actividades = get_object_or_404(
        pk=id_actividad
    )
    if request.method == "POST":
        id_actividad = actividades.codigo

        messages.error(
            request,
            u"La actividad <strong>{}</strong> ha sido eliminado satisfactoriamente...".format(
                id_actividad
            )
        )
        curso.delete()
        return redirect(
            'actividad:actividades'
        )

    ctx['curso'] = curso

    return render(
        request,
        'directorio/actividad/eliminar_actividad.html',
        ctx
    )



@login_required
def editar_actividad(request, id_actividad):
    """
     Función para actualizar una directorio por su id

    :param request: Django request
    :param id_directorio: ID modelo directorio
    :return: Html
    """
    ctx = {}
    modulo = get_object_or_404(
        curso,
       id=id_actividad
    )

    if request.method == "POST":
        form = cursoForm(request.POST, instance=curso)
        if form.is_valid():
            obj = form.save()
            messages.success(
                request,
                u"actividad actualizada satisfactoriamente..."
                )

            return redirect(
                    'sello:actividades'
            )
    else:
        form = cursoForm(instance=curso)

    ctx['curso'] = curso
    ctx['form'] = form

    return render(
        request,
        'directorio/actividad/editar_actividad.html',
        ctx
    )

@login_required
def matricula(request):
        """
         Crea un nuevo registro de matricula asociado al modelo
         matricula

        :param request: Django request
        :return: Html
        """
        ctx = {}

        if request.method == "POST":
            form = matriculaForm(request.POST)
            if form.is_valid():
                obj = form.save()
                messages.success(
                    request,
                    u"Registrado satisfactoriamente..."
                )
                return redirect(
                    'actividades'
                )

        else:
            form = matriculaForm()

        ctx['form'] = form

        return render(
            request,
            'directorio/actividad/matricula.html',
            ctx
        )

#Funcion para ver alumnos matriculados en un curso
def verAlumnosMatriculados(request, id_curso):

    ctx = {}
    matriculados = curso.objects.get(
        matricula,
        id=id_curso)
    ctx['matriculados'] = matriculados
    ctx['verCurso'] = matriculados.objects.filter(matriculados=matricula).order_by('id')

    return render(
        request,
        'directorio/vistas_profesor/estudiantes_matriculados.html',
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
        print(request.POST)
        # viene un formulario
        username = request.POST['rut']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:

                login(request, user)
                return redirect(
                    'directorio:inicio'
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



#LOGOUT
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



class actividadesViewSet(viewsets.ModelViewSet):
    http_method_names = ('get',)
    queryset = curso.objects.order_by('codigo')
    serializer_class = cursoSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('codigo', 'nombre', 'horas')


