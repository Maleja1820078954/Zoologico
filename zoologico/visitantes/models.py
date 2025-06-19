from django.db import models

# Create your models here.
#Modelo Visitantes
class Visitantes(models.Model):
    Cedula_Visitante = models.CharField(max_length=10, primary_key=True)
    Nombre_Visitante = models.CharField(max_length=100)
    Edad_Visitante = models.IntegerField()
    
    def __str__(self):
        return self.Nombre_Visitante
    
