from django.db import models

# Create your models here.

class Vehiculos(models.model):
    marca = models.CharField(max_length=100, blank=True, verbose_name="Marca del Vehiculo")
    modelo = models.CharField(max_length=100, blank=True, verbose_name="Modelo del Vehiculo")
    año = models.PositiveSmallIntegerField(blank=True), verbose_name="Año del Vehiculo")
    placas = models.CharField(max_length=10, blank=True, verbose_name="Placas del Vehiculo")
    conductor = models.CharField(max_length=100, blank=True, verbose_name="Nombre del conductor")


class Residente(models.model):
    nombre = 
    apellido = 
    edad =
    telefono = 
    dni =
    habitacion =
    

class Visitantes(models.model):
    residente =
    nombre =
    apellido =
    telefono =
    dni =


