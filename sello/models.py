from django.db import models
from django.contrib.auth.models import *
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
#from django.contrib.auth.models import User
# Create your models here.

#Clasee carrera contiene los campos codigo de carrera, nombre y duración

class Carrera(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion = models.IntegerField(default=5)

#Funcióon para mostrar en lenguaje natural la clave primaria
    def __str__(self):
        txt = "{0} (Duración: {1} año(s))"
        return txt.format(self.nombre, self.duracion)

#Clase Estudiante contiene rut, nombres, fecha de naciemiento, sexo y carrera, asi como la vigencia del perfil

class estudiante(AbstractUser):
    rut = models.CharField(max_length=20, unique=True)
    username = models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, verbose_name='username')
    email = models.EmailField(_('correo electronico'),unique=True)
    apellidoParterno = models.CharField(_('Apellido Paterno'),max_length=35)
    apellidoMaterno = models.CharField(_('Apellido Paterno'),max_length=35)
    nombres = models.CharField(max_length=35)
    fechaNacimiento = models.DateField(_('Fecha de Nacimiento'), )
    sexos = [
        ('F','FEMENINO'),
        ('M','MASCULINO'),
        ('O','OTRO')
    ]
    genero = models.CharField(max_length=1,choices=sexos,default='F')
    carrera = models.ForeignKey(Carrera,null=True, blank=False, on_delete=models.CASCADE)
    vigencia = models.BooleanField(default=True)
    contrasena = models.CharField(max_length=20)

    USERNAME_FIELD = 'rut'
    REQUIRED_FIELDS = ['username','nombres','email','fechaNacimiento','carrera','genero']


#Funcion para retornar nombre completo
    def nombreCompleto(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.apellidoParterno, self.apellidoMaterno, self.nombres)

    # Funcióon para mostrar en lenguaje natural la clave primaria

    def __str__(self):
        txt = "{0} / Carrera: {1} / {2}"
        if self.vigencia:
            estadoEstudiante = "VIGENTE"
        else:
            estadoEstudiante = "DE BAJA"
        return txt.format(self.nombreCompleto(), self.carrera, estadoEstudiante)

#Clase encargado con rut y nombre

class encargado(models.Model):
    rut= models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        txt = "rut: {0} | nombre: {1} "
        return txt.format(self.rut, self.nombre)

#Clase curso con campos codigo, nombre, horas y encargado
class curso(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    horas = models.IntegerField()
    encargado = models.ForeignKey(encargado,null=False,blank=False, on_delete=models.CASCADE)


    def __str__(self):
        txt = "{0} {1} / encargado: {2}"
        return txt.format(self.nombre, self.codigo,self.encargado.nombre)


class matricula(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(estudiante,null=False,blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(curso,null=False,blank=False,on_delete=models.CASCADE)
    fechaMatricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        txt = "{0} matriculad{1} en el curso {2} / Fecha: {3} "

        if self.estudiante.sexos == "F":
            letraSexo = "a"
        else:
            letraSexo = "o"
        fecMat = self.fechaMatricula.strftime("%A %d /%m/%Y %H:%M:%S")
        return txt.format(self.estudiante.nombreCompleto(),letraSexo,self.curso,fecMat)

    def matriculados(self):
        matriculados_show = estudiante.objects.all().prefetch_related('matricula_set')

estudiante = get_user_model()
