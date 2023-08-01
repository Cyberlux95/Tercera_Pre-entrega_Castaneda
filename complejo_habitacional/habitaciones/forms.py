from django import forms
from .models import Residente, Vehiculos, Visitantes

class formResidente(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.CharField()
    telefono = forms.IntegerField()
    dni = forms.CharField()
    habitacion = forms.CharField()
    

class formVehiculos(forms.Form):
    marca = forms.CharField()
    modelo = forms.CharField()
    año = forms.IntegerField()
    placas = forms.CharField()
    conductor = forms.ModelChoiceField(queryset=Residente.objects.all())

    
class formVisitante(forms.Form):
    nombre_residente = forms.ModelChoiceField(queryset=Residente.objects.all())
    nombre = forms.CharField()
    apellido = forms.CharField()
    telefono = forms.IntegerField()
    dni = forms.CharField()

    