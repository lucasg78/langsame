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


# def clases(request):
    #clases = Clase.objects.all()
    
    #cadena_respuesta = ""
    #for clase in clases:
    #    cadena_respuesta += f"Clase: {clase.nombre} - Comisión: {clase.comision}" + " " +"<br/>"
    
    #return HttpResponse(cadena_respuesta)