from django.http import HttpResponse
from django.shortcuts import render
from appclases.models import Clase

# Create your views here.
def inicio(request):
    return render(request, "appclases/index.html")

def clases(request):
    clases = Clase.objects.all()
    
    cadena_respuesta = ""
    for clase in clases:
        cadena_respuesta += f"Clase: {clase.nombre} - Comisión: {clase.comision}" + " " +"<br/>"
    
    return HttpResponse(cadena_respuesta) 