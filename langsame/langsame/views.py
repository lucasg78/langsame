from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader


def vista_plantilla(request):
    # Abrimos el archivo
    archivo = open(r"G:\Mi unidad\Formación\Programación\Python\Práctica\langsame\langsame\langsame\templates\inicio.html")
    
    # Creamos el objeto "plantilla"
    plantilla = Template(archivo.read())
    
    # Cerramos el archivo para liberar recursos
    archivo.close()

    # Diccionario con datos para la plantilla
    datos = {
    "fecha": datetime.now().strftime("%d/%m/%Y"),
    "nombre": "Lucas",
    "apellido": "Gallo",
    "edad": 45,
    "email": "lucasgallo@gmail.com",
    }
    # Creamos el contexto
    contexto = Context(datos)

    # Renderizamos la plantilla para crear la respuesta
    documento = plantilla.render(contexto)
    
    # Retornamos la respuesta
    return HttpResponse(documento)


# LISTADO DE ALUMNOS
# ALTERNATIVA 1: CONTEXT
def vista_listado_alumnos(request):
    # Abrimos el archivo
    archivo = open(r"G:\Mi unidad\Formación\Programación\Python\Práctica\langsame\langsame\langsame\templates\listado_alumnos.html")
    
    # Creamos el template
    plantilla = Template(archivo.read())

    # Cerramos el archivo para liberar recursos
    archivo.close()

    # Creamos el diccionario de datos para la plantilla
    listado_alumnos = ["Lucas Gallo", "Juan Pérez", "Ernesto Filemundo", "Mariano Fernández", "Carlos Salvador Allende"]
    datos = {"tecnologia":"Python", "listado_alumnos": listado_alumnos}
    
    # Creamos el contexto
    contexto = Context(datos)

    documento = plantilla.render(contexto)
    
    return HttpResponse(documento)


# ALTERNATIVA 2: LOADER
def vista_listado_alumnos2(request):
    # Creamos el diccionario de datos para la plantilla
    listado_alumnos = ["Lucas Gallo", "Juan Pérez", "Ernesto Filemundo", "Mariano Fernández", "Carlos Salvador Allende"]
    datos = {"tecnologia":"Python", "listado_alumnos": listado_alumnos}

    # Creamos el template
    plantilla = loader.get_template("listado_alumnos.html")
    
    # Renderizamos el template
    documento = plantilla.render(datos)
    
    return HttpResponse(documento)