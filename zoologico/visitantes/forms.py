from django import forms 
from .models import Visitantes
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Formulario para productos
class VisitantesForm(forms.ModelForm):
    class Meta:
        model = Visitantes
        fields = '__all__'
        
# Formulario para registro de usuarios
class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']