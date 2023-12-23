from django.urls import path
from appclases.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("clases/", clases, name="clases"),
    path("clases/crear/", creacion_clase, name="clases-crear"),
    path("profesores/", profesores, name="profesores"),
    path("profesores/crear/", creacion_profesor, name="profesor-crear"),
    path("profesores/crear2/", creacion_profesor2, name="profesor-crear2"),
    path("alumnos/", alumnos, name="alumnos"),
    path("entregables/", entregables, name="entregables"),
    path("aulas/", aulas, name="aulas"),
]
