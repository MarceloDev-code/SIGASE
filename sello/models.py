from django.db import models

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

class estudiante(models.Model):
    rut = models.CharField(max_length=9,primary_key=True)
    apellidoParterno = models.CharField(max_length=35)
    apellidoMaterno = models.CharField(max_length=35)
    nombres = models.CharField(max_length=35)
    fechaNaciemiento = models.DateField()
    sexos = [
        ('F','FEMENINO'),
        ('M','MASCULINO'),
        ('O','OTRO')
    ]
    genero = models.CharField(max_length=1,choices=sexos,default='F')
    carrera = models.ForeignKey(Carrera,null=False, blank=False, on_delete=models.CASCADE)
    vigencia = models.BooleanField(default=True)


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
    rut= models.CharField(max_length=9,primary_key=True,null=False,blank=False)
    nombre = models.CharField(max_length=100)

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
