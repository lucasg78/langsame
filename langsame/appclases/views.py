from django.http import HttpResponse
from django.shortcuts import render
from appclases.models import Clase, Profesor

# Create your views here.
def inicio(request):
    return render(request, "appclases/index.html")

def clases(request):
    return render(request, "appclases/clases.html")

def creacion_clase(request):

    if request.method == "POST":
        nombre_clase = request.POST["clase"]
        numero_comision = request.POST["comision"]
        
        clase = Clase(nombre=nombre_clase, comision=numero_comision)
        clase.save()
    
    return render(request, "appclases/clase_formulario.html")

def profesores(request):
    return render(request, "appclases/profesores.html")

def creacion_profesor(request):

    if request.method == "POST":
        nombre_profesor = request.POST["nombre"]
        apellido_profesor = request.POST["apellido"]
        email_profesor = request.POST["email"]
        
        profesor = Profesor(nombre=nombre_profesor, apellido=apellido_profesor, email=email_profesor)
        profesor.save()
        
    return render(request, "appclases/profesor_formulario.html")

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