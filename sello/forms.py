from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, HTML
from django import forms
from localflavor.cl.forms import CLRutField
from sello import models

class carreraForm(forms.ModelForm):
    rut = CLRutField()

    class Meta:
        model = models.Carrera
        fields = '__all__'

        def __init_(self,*args,**kwargs ):
         super(carreraForm, self).__init__(*args,**kwargs)
         self.helper = FormHelper()
         self.helper.form_id = 'id_carreraForm'
         self.helper.form_method = 'post'
         self.helper.form_action = '.'
         self.helper.layout = Layout(
             'codigo',
             'nombre',
             'duracion',
             HTML(
                 "<br>"
                 "<div class='text-center'>"
                 "<div class='btn-group'>"
                 "<a href='{% url 'sello:inicio' %}' class='btn btn-lg btn-dark'>"
                 "<i class='fa fa-arrow-left'></i> "
                 "Volver</a>"
                 "<button type='submit' class='btn btn-lg btn-primary'>"
                 "<i class='fa fa-save'></i> "
                 "Guardar </button>"
                 "</div>"
                 "</div>"
             )
         )
class estudianteForm(forms.ModelForm):
    class Meta:
        model = models.estudiante
        fields = [
            'rut',
            'apellidoParterno',
            'apellidoMaterno',
            'nombres',
            'fechaNaciemiento',
            'genero',
            'carrera'
        ]

        def __init_(self,*args,**kwargs ):
         super(carreraForm, self).__init__(*args,**kwargs)
         self.helper = FormHelper()
         self.helper.form_id = 'id_estudianteForm'
         self.helper.form_method = 'post'
         self.helper.form_action = '.'
         self.helper.layout = Layout(
             'Rut',
             'Apellido Paterno',
             'Apellido Materno',
             'Nombres',
             'Fecha de Nacimiento',
             'genero',
             'carrera',
             HTML(
                 "<br>"
                 "<div class='text-center'>"
                 "<div class='btn-group'>"
                 "<a href='{% url 'sello:inicio' %}' class='btn btn-lg btn-dark'>"
                 "<i class='fa fa-arrow-left'></i> "
                 "Volver</a>"
                 "<button type='submit' class='btn btn-lg btn-primary'>"
                 "<i class='fa fa-save'></i> "
                 "Guardar </button>"
                 "</div>"
                 "</div>"
             )
         )
class encargadoForm(forms.ModelForm):
    rut = CLRutField()
    class Meta:
        model = models.encargado
        fields = [
            'rut',
            'nombre'
        ]

        def __init_(self,*args,**kwargs ):
         super(carreraForm, self).__init__(*args,**kwargs)
         self.helper = FormHelper()
         self.helper.form_id = 'id_encargadoForm'
         self.helper.form_method = 'post'
         self.helper.form_action = '.'
         self.helper.layout = Layout(
             'Rut',
             'Nombre',
             HTML(
                 "<br>"
                 "<div class='text-center'>"
                 "<div class='btn-group'>"
                 "<a href='{% url 'sello:inicio' %}' class='btn btn-lg btn-dark'>"
                 "<i class='fa fa-arrow-left'></i> "
                 "Volver</a>"
                 "<button type='submit' class='btn btn-lg btn-primary'>"
                 "<i class='fa fa-save'></i> "
                 "Guardar </button>"
                 "</div>"
                 "</div>"
             )
         )

class selloForm(forms.ModelForm):
    class Meta:
        model = models.curso
        fields = [
            'codigo',
            'nombre',
            'horas',
            'encargado'
        ]

        def __init_(self,*args,**kwargs ):
         super(carreraForm, self).__init__(*args,**kwargs)
         self.helper = FormHelper()
         self.helper.form_id = 'id_selloForm'
         self.helper.form_method = 'post'
         self.helper.form_action = '.'
         self.helper.layout = Layout(
             'codigo',
             'nombre',
             'horas',
             'encargado',

             HTML(
                 "<br>"
                 "<div class='text-center'>"
                 "<div class='btn-group'>"
                 "<a href='{% url 'sello:inicio' %}' class='btn btn-lg btn-dark'>"
                 "<i class='fa fa-arrow-left'></i> "
                 "Volver</a>"
                 "<button type='submit' class='btn btn-lg btn-primary'>"
                 "<i class='fa fa-save'></i> "
                 "Guardar </button>"
                 "</div>"
                 "</div>"
             )
         )


class selloForm(forms.ModelForm):
    class Meta:
        model = models.curso
        fields = [
            'nombre',
            'horas',
            'encargado'
        ]

        def __init_(self, *args, **kwargs):
            super(carreraForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_id = 'id_selloForm'
            self.helper.form_method = 'post'
            self.helper.form_action = '.'
            self.helper.layout = Layout(
                'codigo',
                'nombre',
                'horas',
                'encargado',

                HTML(
                    "<br>"
                    "<div class='text-center'>"
                    "<div class='btn-group'>"
                    "<a href='{% url 'sello:inicio' %}' class='btn btn-lg btn-dark'>"
                    "<i class='fa fa-arrow-left'></i> "
                    "Volver</a>"
                    "<button type='submit' class='btn btn-lg btn-primary'>"
                    "<i class='fa fa-save'></i> "
                    "Guardar </button>"
                    "</div>"
                    "</div>"
                )
            )
class matriculaForm(forms.ModelForm):
    class Meta:
        model = models.curso
        fields = [
            'nombre',
            'estudiante',
            'curso',
        ]

        def __init_(self, *args, **kwargs):
            super(carreraForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_id = 'id_selloForm'
            self.helper.form_method = 'post'
            self.helper.form_action = '.'
            self.helper.layout = Layout(
                'codigo',
                'nombre',
                'horas',
                'encargado',

                HTML(
                    "<br>"
                    "<div class='text-center'>"
                    "<div class='btn-group'>"
                    "<a href='{% url 'sello:inicio' %}' class='btn btn-lg btn-dark'>"
                    "<i class='fa fa-arrow-left'></i> "
                    "Volver</a>"
                    "<button type='submit' class='btn btn-lg btn-primary'>"
                    "<i class='fa fa-save'></i> "
                    "Guardar </button>"
                    "</div>"
                    "</div>"
                )
            )