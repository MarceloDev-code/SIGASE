from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field, HTML, Div, Fieldset, Hidden, ButtonHolder, Button
from django import forms
from localflavor.cl.forms import CLRutField
from sello import models


class carreraForm(forms.ModelForm):
    class Meta:
        model = models.Carrera
        fields = '__all__'

        def __init_(self, *args, **kwargs):
            super(carreraForm, self).__init__(*args, **kwargs)
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
                    "<a href='{% url 'inicio' %}' class='btn btn-lg btn-dark'>"
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
    rut = CLRutField()

    class Meta:
        model = models.estudiante
        fields = [
            'rut',
            'username',
            'email',
            'apellidoMaterno',
            'nombres',
            'fechaNacimiento',
            'genero',
            'carrera',

        ]
        widgets = {
            "fechaNacimiento": forms.DateInput(format='%d/%m/%Y')

        }

    def __init__(self, *args, **kwargs):
            super(estudianteForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_id = 'id_estudianteForm'
            self.helper.form_method = 'post'
            self.helper.form_action = '.'
            self.helper.layout = Layout(
                'rut',
                'username',
                'email',
                'Apellido Materno',
                'nombre',
                'genero',
                'carrera',

                HTML(
                    "<br>"
                    "<div class='text-center'>"
                    "<div class='btn-group'>"
                    "<a href='{% url 'inicio' %}' class='btn btn-lg btn-dark'>"
                    "<i class='fa fa-arrow-left'></i> "
                    "Volver</a>"
                    "<button type='submit' class='btn btn-lg btn-primary'>"
                    "<i class='fa fa-save'></i> "
                    "Guardar </button>"
                    "</div>"
                    "</div>"
                ))


class encargadoForm(forms.ModelForm):
    rut = CLRutField()

    class Meta:
        model = models.encargado
        fields = [
            'rut',
            'nombre'
        ]

        def __init__(self, *args, **kwargs):
            super(encargadoForm, self).__init__(*args, **kwargs)
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
                    "<a href='{% url 'inicio' %}' class='btn btn-lg btn-dark'>"
                    "<i class='fa fa-arrow-left'></i> "
                    "Volver</a>"
                    "<button type='submit' class='btn btn-lg btn-primary'>"
                    "<i class='fa fa-save'></i> "
                    "Guardar </button>"
                    "</div>"
                    "</div>"
                )
            )


class cursoForm(forms.ModelForm):
    class Meta:
        model = models.curso
        fields = [
            'codigo',
            'nombre',
            'horas',
            'encargado'
        ]

        def __init_(self, *args, **kwargs):
            super(cursoForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_id = 'id_cursoForm'
            self.helper.form_method = 'post'
            self.helper.form_action = '.'
            self.helper.layout = Layout(
                HTML(
                    "<br>"
                    "<div class='text-center'>"
                    "<div class='btn-group'>"
                    "<a href='{% url 'inicio' %}' class='btn btn-lg btn-dark'>"
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
        model = models.matricula
        fields = [
            'estudiante',
            'curso',
        ]

    def __init__(self, *args, **kwargs):
         super(matriculaForm, self).__init__(*args, **kwargs)
         self.helper = FormHelper()
         self.helper.form_id = 'id_selloForm'
         self.helper.form_method = 'post'
         self.helper.form_action = '.'
         self.helper.layout = Layout(
             'estudiante',
             'curso',

            HTML(

                    "<br>"
                    "<div class='text-center'>"
                    "<div class='btn-group'>"
                    "<a href='{% url 'inicio' %}' class='btn btn-lg btn-dark'>"
                    "<i class='fa fa-arrow-left'></i> "
                    "Volver</a>"
                    "<button type='submit' class='btn btn-lg btn-primary'>"
                    "<i class='fa fa-save'></i> "
                    "Registrar </button>"
                    "</div>"
                    "</div>"

            ),
         )
