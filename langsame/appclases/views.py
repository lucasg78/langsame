from django.http import HttpResponse
from django.shortcuts import render
from appclases.models import Clase

# Create your views here.
def inicio(request):
    return render(request, "appclases/index.html")

def clases(request):
    return render(request, "appclases/clases.html")

def profesores(request):
    return render(request, "appclases/profesores.html")

def alumnos(request):
    return render(request, "appclases/alumnos.html")

def entregables(request):
    return render(request, "appclases/entregables.html")

def aulas(request):
    return render(request, "appclases/aulas.html")


# def clases(request):
    #Obtenemos el listado de objetos en la BD
    #clases = Clase.objects.all()
    
    #cadena_respuesta = ""
    #for clase in clases:
    #    cadena_respuesta += f"Clase: {clase.nombre} - Comisión: {clase.comision}" + " " +"<br/>"
    
    #return HttpResponse(cadena_respuesta)