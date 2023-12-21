from django.contrib import admin

# Register your models here.
from appclases.models import *

admin.site.register(Clase)
admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Entregable)
admin.site.register(Aula)