from django import forms

class ProfesorFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    

class ClaseFormulario(forms.Form):
    nombre = forms.CharField(min_length=3)    
    comision = forms.IntegerField()