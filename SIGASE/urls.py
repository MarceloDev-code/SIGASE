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

app_name ='sello'

urlpatterns = [
    url(r'^admin/', admin.site.urls ),

    url(
        r'^login/$',
        views.login,
        name='login'
    ),

    url(r'^$', views.inicio, name='inicio'),

    url(r'^logout', views.logout, name='logout'),
    # estudiantes
    url(
        r'^estudiantes/$',
        views.estudiantes,
        name='estudiantes'
    ),
    url(
        r'^estudiante/(?P<id_estudiante>[0-9]+)/$',
        views.mostrar_estudiante,
        name='mostrar_estudiante'
    ),
    url(
        r'^estudiante/nuevo/$',
        views.crear_estudiante,
        name='crear_estudiante'
    ),
    url(
        r'^estudiante/(?P<id_estudiante>[0-9]+)/editar/$',
        views.editar_estudiante,
        name='editar_estudiante'
    ),
    url(
        r'^estudiante/(?P<id_estudiante>[0-9]+)/eliminar/$',
        views.eliminar_estudiante,
        name='eliminar_estudiante'
    ),
#Actividades sello
    url(
        r'^actividades/$',
        views.actividades,
        name='actividades'
    ),

    url(
        r'^actividad/nueva/$',
        views.crear_actividad,
        name='crear_actividad'
    ),

url(
        r'^actividad/matricula/$',
        views.matricula,
        name='matricula'
    ),
url(
        r'^matriculados/(?P',
        views.verAlumnosMatriculados,
        name='matriculados'
    ),

]