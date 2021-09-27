from django.contrib import admin
from sello.models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Carrera)
admin.site.register(estudiante, UserAdmin)

admin.site.register(curso)
admin.site.register(matricula)
admin.site.register(encargado)