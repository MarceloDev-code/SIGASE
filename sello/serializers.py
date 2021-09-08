from django.contrib.auth.models import User

from rest_framework import serializers

from sello.models import *

class estudianteSerializer(serializers.ModelSerializer):

    class Meta:
        model = estudiante
        fields = '__all__'
        read_only_fields = ['rut']

class carreraSerializer(serializers.ModelSerializer):

    class Meta:
        model = Carrera
        fields = '__all__'

class encargadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = encargado
        fields = '__all__'

class cursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = curso
        fields = '__all__'

class matriculaSerializer(serializers.ModelSerializer):

    class Meta:
        model = matricula
        fields = '__all__'