"""SIGASE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from sello import views
app_name='sello'

urlpatterns = [
    path('admin/', admin.site.urls),
    url(
        r'^$',
        views.inicio,
        name='inicio'
    ),
    # Personas
    url(
        r'^personas/$',
        views.personas,
        name='personas'
    ),
    url(
        r'^personas/(?P<id_persona>[0-9]+)/$',
        views.mostrar_persona,
        name='mostrar_persona'
    ),
    url(
        r'^personas/nueva/$',
        views.crear_persona,
        name='crear_persona'
    ),
    url(
        r'^personas/(?P<id_persona>[0-9]+)/editar/$',
        views.editar_persona,
        name='editar_persona'
    ),
    url(
        r'^personas/(?P<id_persona>[0-9]+)/eliminar/$',
        views.eliminar_persona,
        name='eliminar_persona'
    ),
    # modulos

    url(
        r'^reserva/modulos/$',
        views.modulos,
        name='modulos'
    ),

    url(
        r'^modulos/nueva/$',
        views.crear_modulo,
        name='crear_modulo'
    ),
    url(
        r'^modulos/(?P<id_modulo>[0-9]+)/editar/$',
        views.editar_modulos,
        name='editar_modulos'
    ),
    url(
        r'^modulos/(?P<id_modulo>[0-9]+)/eliminar/$',
        views.eliminar_modulos,
        name='eliminar_modulos'
    ),

    # Directorios

    url(
        r'^asignatura/(?P<id_asignatura>[0-9]+)/editar/$',
        views.editar_asignatura,
        name='editar_asignatura'
    ),

    url(
        r'^asignatura/(?P<id_directorio>[0-9]+)/eliminar/$',
        views.eliminar_asignatura,
        name='eliminar_asignatura'
    ),

    url(
        r'^asignatura/nueva/$',
        views.crear_asignatura,
        name='crear_asignatura'
    ),

    # salas

    url(
        r'^Salas/(?P<id_sala>[0-9]+)/editar/$',
        views.editar_sala,
        name='editar_sala'
    ),

    url(
        r'^Salas/(?P<id_sala>[0-9]+)/eliminar/$',
        views.eliminar_sala,
        name='eliminar_sala'
    ),

    url(
        r'^Salas/nueva/$',
        views.crear_sala,
        name='crear_sala'
    ),

    url(
        r'^salas/$',
        views.salas,
        name='salas'
    ),
    # reserva

    url(
        r'^reserva/reservas/$',
        views.reservas,
        name='reservas'
    ),

    url(
        r'^reserva/(?P<id_reserva>[0-9]+)/editar/$',
        views.editar_reserva,
        name='editar_reserva'
    ),

    url(
        r'^reserva/(?P<id_reserva>[0-9]+)/eliminar/$',
        views.eliminar_reserva,
        name='eliminar_reserva'
    ),

    url(
        r'^reserva/nueva/$',
        views.crear_reserva,
        name='crear_reserva'
    ),
]
