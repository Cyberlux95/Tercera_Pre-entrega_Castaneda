"""

------------------------------------ HABITACIONES -----------------------------------------



URL configuration for complejo_habitacional project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import form_residentes, form_visitantes, form_vehiculos, busqueda, home

urlpatterns = [

    path('', home , name="home"),
    path('formulario-residentes/',form_residentes, name="formulario-residentes"),
    path('formulario-vehiculos/', form_vehiculos, name="formulario-vehiculos"),
    path('formulario-visitantes/', form_visitantes, name ="formulario-visitantes"),
    path('busqueda/',busqueda, name="busqueda")
]
