from django.db import models

# Create your models here.
class Clase(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()
    
    def __str__(self):
        return f"Curso: {self.nombre} -> Comisión: {self.comision}"
    
class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return f"{self.apellido.upper()}, {self.nombre.capitalize()} [{self.email}]"
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)  
    
    def __str__(self):
        return f"{self.nombre.capitalize()} {self.apellido.upper()} -> {self.email}"
    
class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()   
    
    def __str__(self):
        return f"{self.nombre} -> {self.fechaDeEntrega}"

class Aula(models.Model):
    nombre = models.CharField(max_length=50)
    numero = models.IntegerField()
    ubicacion = models.CharField(max_length=50)  
    
    def __str__(self):
        return f"Aula: {self.nombre.capitalize()} -> Número: {self.numero} -> Ubicación: {self.ubicacion}"       