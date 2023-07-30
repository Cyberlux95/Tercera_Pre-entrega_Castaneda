from django.contrib import admin
from .models import Residente, Vehiculos, Visitantes #  tuve que agregar .models agregar [ . ] si no, no funciona

# Register your models here.
admin.site.register(Residente)
admin.site.register(Vehiculos) 
admin.site.register(Visitantes)