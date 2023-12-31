from django.urls import path
from appclases.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    
    path("clases/", clases, name="clases"),
    #path("clases/crear/", creacion_clase, name="clases-crear"),
    path("clases/buscar/", buscar_clase, name="clase-buscar"),
    path("clases/borrar/<id>/", borrar_clase, name="clase-borrar"),
    path("clases/buscar/resultados/", resultados_buscar_clase, name="clase-buscar-resultados"),
    path("clases/editar/<id>/", editar_clase, name="clase-editar"),
    
    path("profesores/", profesores, name="profesores"),
    path("profesores/crear/", creacion_profesor, name="profesor-crear"),
    path("profesores/crear2/", creacion_profesor2, name="profesor-crear2"),
    path("profesores/buscar/", buscar_profesor, name="profesor-buscar"),
    path("profesores/buscar/resultados/", resultados_buscar_profesor, name="profesor-buscar-resultados"),
    
    path("alumnos/", alumnos, name="alumnos"),
    path("alumnos/buscar/", buscar_alumno, name="alumno-buscar"),
    path("alumnos/buscar/resultados/", resultados_buscar_alumno, name="alumno-buscar-resultados"),
    
    #path("entregables/", entregables, name="entregables"),
    path("entregables/",EntregablesList.as_view(), name="entregables"), 
    path("entregables/detalle/<pk>/",EntregablesDetail.as_view(), name="entregables-detail"),  
    path("entregables/crear",EntregablesCreate.as_view(), name="entregables-create"),   
    path("entregables/editar/<pk>/",EntregablesUpdate.as_view(), name="entregables-update"),  
    path("entregables/borrar/<pk>/",EntregablesDelete.as_view(), name="entregables-delete"),   
    
    path("aulas/", aulas, name="aulas"),
    
    path("login/", iniciar_sesion, name="login"),
    
    path("test", test)
]
