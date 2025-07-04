"""zoologico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from visitantes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('visitantes/', views.lista_visitantes, name='lista_visitantes'),
    path('visitantes/agregar/', views.agregar_visitantes, name='agregar_visitantes'),
    path('visitantes/editar/<str:Cédula_Visitante>/', views.editar_visitantes, name='editar_visitantes'),
    path('visitantes/eliminar/<str:Cédula_Visitante>/', views.eliminar_visitantes, name='eliminar_visitantes'),
    #Esta linea sirve para generar un reporte en PDF de visitantes
    path('visitantes/reporte/pdf/', views.generar_reporte_pdf, name='reporte_pdf'),  
    path('visitantes/dashboard/', views.dashboard_visitantes, name='dashboard_visitantes'), 
]
