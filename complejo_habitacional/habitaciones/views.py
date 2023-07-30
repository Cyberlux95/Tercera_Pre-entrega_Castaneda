from django.shortcuts import render
from .forms import formResidente, formVehiculos, formVisitante
from .models import Residente, Vehiculos, Visitantes
from django.contrib import messages

# Create your views here.
def form_residentes(request):
    if request.method == 'POST':
        formulario = formResidente(request.POST) #se conecta con forms.py
        
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            
            residente = Residente(nombre=informacion['nombre'],
                                 apellido=informacion['apellido'], 
                                 edad=informacion['edad'], 
                                 telefono=informacion['telefono'], 
                                 dni=informacion['dni'],
                                 habitacion=informacion['habitacion'])
            residente.save()
            
            # Mensaje de éxito 
            messages.success(request, f'Residente: "{residente.nombre}" guardado correctamente.')
            
            
            # Redireccionar a la misma página para evitar reenvío del formulario
            return redirect('formulario-Residentes') #aqui va el url de este formulario
            
    else:
        formulario1 = formResidente() #se conecta con forms.py
        
    return render(request, 'residentes.html', {'formulario1': formulario1})


def form_visitantes(request):
    if request.method == 'POST':
        formulario = formResidente(request.POST)  #se conecta con forms.py
        
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            
            visitante = Visitantes(noresidente =informacion['residente'],
                                 nombre=informacion['nombre'], 
                                 apellido=informacion['apellido'], 
                                 telefono=informacion['telefono'], 
                                 dni=informacion['dni'],
                                 )
            visitante.save()
            
            # Mensaje de éxito 
            messages.success(request, f'Visitante: "{visitante.nombre}" guardado correctamente.')
            
            
            # Redireccionar a la misma página para evitar reenvío del formulario
            return redirect('formulario-Visitante') #aqui va el url de este formulario
            
    else:
        formulario1 = formVisitante() #se conecta con forms.py
        
    return render(request, 'visitantes.html', {'formulario1': formulario1})


def form_vehiculos(request):
    if request.method == 'POST':
        formulario = formVehiculos(request.POST) #se conecta con forms.py
        
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            
            vehiculo = Vehiculos(marca=informacion['marca'],
                                 modelo=informacion['modelo'], 
                                 año=informacion['año'], 
                                 placas=informacion['placas'], 
                                 conductor=informacion['conductor'],
                                 )
            vehiculo.save()
            
            # Mensaje de éxito 
            messages.success(request, f'Visitante: "{vehiculo.marca}" guardado correctamente.')
            
            
            # Redireccionar a la misma página para evitar reenvío del formulario
            return redirect('formulario-Visitante') #aqui va el url de este formulario
            
    else:
        formulario1 = formVehiculos() #se conecta con forms.py
        
    return render(request, 'vehiculos.html', {'formulario1': formulario1})


def busqueda(request):
    if request.method == 'POST':
        palabra_clave = request.POST.get('palabra_clave', '')

        # Realizar las consultas para obtener los resultados de la búsqueda
        resultados_residentes = Residente.objects.filter(nombre__icontains=palabra_clave)
        resultados_visitantes = Visitantes.objects.filter(nombre__icontains=palabra_clave)
        resultados_vehiculos = Vehiculos.objects.filter(nombre__icontains=palabra_clave)

        return render(request, 'busqueda.html', {
            'palabra_clave': palabra_clave,
            'resultados_residentes': resultados_residentes,
            'resultados_visitantes': resultados_visitantes,
            'resultados_vehiculos': resultados_vehiculos,
        })
    else:
        return render(request, 'busqueda.html')