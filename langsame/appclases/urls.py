from django.urls import path
from appclases.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("clases/", clases, name="clases"),
    path("profesores/", profesores, name="profesores"),
    path("alumnos/", alumnos, name="alumnos"),
    path("entregables/", entregables, name="entregables")
]
