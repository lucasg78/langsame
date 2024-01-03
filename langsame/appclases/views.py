from django.http import HttpResponse

# Shortcuts
from django.shortcuts import render, redirect

# Models
from appclases.models import Clase, Profesor, Alumno, Entregable

# Forms
from appclases.forms import ProfesorFormulario, ClaseFormulario

# Dependencias para resolver apertura de archivos usando rutas relativas 
from langsame.settings import BASE_DIR
import os

# Class Based Views (CBV)
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate



# Inicio
def inicio(request):
    return render(request, "appclases/index.html")


# Login
def iniciar_sesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=password)

            if user is not None:
                login(request, user)
                return render(
                    request,
                    "appclases/index.html",
                )
            else:
                return render(
                    request,
                    "appclases/login_error.html",
                    {"mensaje": "Datos Incorrectos. Intente nuevamente."},
                )

        else:
            return render(
                request,
                "appclases/login_error.html",
                {"mensaje": "Datos Incorrectos. Intente nuevamente."},
            )

    form = AuthenticationForm()

    return render(request, "appclases/login.html", {"form": form})


# Clases
def clases(request):
    
    errores = ""
    
    # Validamos tipo de petición
    if request.method == "POST":
        # Cargamos los datos en el formulario
        formulario = ClaseFormulario(request.POST)
        # Validamos los datos
        if formulario.is_valid():
            # Recuperamos los datos limpios
            data = formulario.cleaned_data
            # Creamos la clase
            clase = Clase(nombre=data["nombre"], comision=data["comision"])
            # Guardamos la clase
            clase.save()
        else:
            # Si el formulario no es válido, guardamos los errores para mostrarlos
            errores = formulario.errors
    # Recuperamos todas las clases de la BD
    clases = Clase.objects.all() # Obtener todos los registros de ese modelo
    # Creamos el formulario vacío
    formulario = ClaseFormulario()
    # Creamos el contexto
    contexto = {"listado_clases": clases, "formulario": formulario, "errores": errores}
    # Retornamos la respuesta
    return render(request, "appclases/clases.html", contexto)

""" def creacion_clase(request):
    if request.method == "POST":
        nombre_clase = request.POST["clase"]
        numero_comision = request.POST["comision"] 
        clase = Clase(nombre=nombre_clase, comision=numero_comision)
        clase.save()
    return render(request, "appclases/clase_formulario.html") """

def buscar_clase(request):
    return render(request, "appclases/clase_buscar.html")

def resultados_buscar_clase(request):
    print(request.GET)
    clase = request.GET["clase"]
    clases = Clase.objects.filter(nombre__icontains=clase)
    return render(request, "appclases/resultados_buscar_clase.html", {"clases": clases})

def editar_clase(request, id):
    clase = Clase.objects.get(id=id)
    if request.method == "POST":
        formulario = ClaseFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            clase.nombre = data["nombre"]
            clase.comision = data["comision"]
            clase.save()
            return redirect("clases")
        else:
            return render(request, "appclases/clase_editar.html", {"formulario": formulario, "errores": formulario.errors})
    else:
        formulario = ClaseFormulario(initial={"nombre":clase.nombre, "comision":clase.comision})    
        return render(request, "appclases/clase_editar.html", {"formulario": formulario, "errores": ""})
        
def borrar_clase(request, id):
    clase = Clase.objects.get(id=id)
    clase.delete()
        
    return redirect("clases")


# Profesores
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

def creacion_profesor2(request):
    if request.method == "POST":
        formulario = ProfesorFormulario(request.POST)
        # Validamos que el formulario no tenga problemas
        if formulario.is_valid():
            # Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data
            profesor = Profesor(nombre=data["nombre"], apellido=data["apellido"], email=data["email"])
            profesor.save()        
    formulario = ProfesorFormulario()
    contexto = {"formulario": formulario}            
    return render(request, "appclases/profesor_formulario2.html", contexto)

def buscar_profesor(request):
    return render(request, "appclases/profesor_buscar.html")

def resultados_buscar_profesor(request):
    print(request.GET)
    apellido_profesor = request.GET["apellido"]
    profesores = Profesor.objects.filter(apellido__icontains=apellido_profesor)
    return render(request, "appclases/resultados_buscar_profesor.html", {"profesores": profesores})


# Alumnos
def alumnos(request):
    return render(request, "appclases/alumnos.html")

def buscar_alumno(request):
    return render(request, "appclases/alumno_buscar.html")

def resultados_buscar_alumno(request):
    print(request.GET)
    apellido_alumno = request.GET["apellido"]
    alumnos = Alumno.objects.filter(apellido__icontains=apellido_alumno)
    return render(request, "appclases/resultados_buscar_alumno.html", {"alumnos": alumnos})


# Entregables
def entregables(request):
    return render(request, "appclases/entregables.html")

class EntregablesList(ListView): 
    model = Entregable
    template_name = "appclases/entregables.html"

class EntregablesDetail(DetailView):
    model = Entregable
    template_name = "appclases/entregables_detalle.html"
    
class EntregablesCreate(CreateView):
    model = Entregable
    success_url = "/clases/entregables/"
    fields = ["nombre", "fechaDeEntrega", "entregado"]   
    template_name = "appclases/entregable_form.html"

class EntregablesUpdate(UpdateView):
    model = Entregable
    success_url = "/clases/entregables/"
    fields = ["nombre", "fechaDeEntrega", "entregado"]    

class EntregablesDelete(DeleteView):
    model = Entregable
    success_url = "/clases/entregables/"
                

# Aulas
def aulas(request):
    return render(request, "appclases/aulas.html")




# def clases(request):
    #Obtenemos el listado de objetos en la BD
    #clases = Clase.objects.all()
    
    #cadena_respuesta = ""
    #for clase in clases:
    #    cadena_respuesta += f"Clase: {clase.nombre} - Comisión: {clase.comision}" + " " +"<br/>"
    
    #return HttpResponse(cadena_respuesta)
    
    
def test(request):
    ruta = os.path.join(BASE_DIR, "appclases/templates/appclases/base.html")
    print(BASE_DIR, __file__)
    file = open(ruta)
    
    return HttpResponse(file.read())