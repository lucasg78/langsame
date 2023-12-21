from django.db import models

# Create your models here.
class Clase(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()
    
class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()  
    
class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()   

class Aula(models.Model):
    nombre = models.CharField(max_length=50)
    numero = models.IntegerField()
    ubicacion = models.CharField(max_length=50)         