from django.db import models
# Create your models here.
    


class Residente(models.Model):
    nombre = models.CharField(max_length=60, blank=True)
    apellido = models.CharField(max_length=60, blank=True)
    edad = models.PositiveBigIntegerField(blank=True)
    telefono = models.PositiveBigIntegerField (blank=True)
    dni = models.CharField(max_length=18, blank=True, verbose_name="Codigo de DNI")
    habitacion = models.PositiveBigIntegerField(blank=True)
    
    def __str__(self):
        return f"{self.nombre},{self.apellido}, de la habitacion: {self.habitacion} "

class Vehiculos(models.Model):
    marca = models.CharField(max_length=100, blank=True, verbose_name="Marca del Vehiculo")
    modelo = models.CharField(max_length=100, blank=True, verbose_name="Modelo del Vehiculo")
    año = models.PositiveSmallIntegerField(blank=True, verbose_name="Año del Vehiculo")
    placas = models.CharField(max_length=10, blank=True, verbose_name="Placas del Vehiculo")
    conductor = models.CharField(max_length=100, blank=True, verbose_name="Nombre del conductor")

    def __str__(self):
        return f"{self.marca},{self.modelo}, conducido por: {self.conductor} "


class Visitantes(models.Model):
    residente = models.CharField(max_length=60, blank=True, verbose_name="Nombre del residente que visita")
    nombre = models.CharField(max_length=60, blank=True)
    apellido = models.CharField(max_length=60, blank=True)
    telefono = models.PositiveBigIntegerField(blank=True)
    dni = models.CharField(max_length=18, blank=True, verbose_name="Codigo de DNI")

    def __str__(self):
        return f"{self.nombre},{self.apellido}, "

