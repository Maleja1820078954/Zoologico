from django.shortcuts import render, redirect  # Importa funciones para renderizar plantillas y redireccionar
from .models import Visitantes  # Importa el modelo Producto
from .forms import VisitantesForm, RegistroUsuarioForm  # Importa los formularios personalizados
from django.contrib.auth import authenticate, login, logout  # Importa funciones de autenticación
from django.contrib.auth.decorators import login_required  # Importa el decorador para requerir login
from django.template.loader import get_template    #importar función para cargar plantillas
from xhtml2pdf import pisa    #Importamos la libreria para generar PDFs
from django.http import HttpResponse

# Vista de inicio
def home(request):
    # Renderiza la plantilla 'home.html'
    return render(request, 'home.html')

# Registro de usuarios
def registro(request):
    if request.method == 'POST':  # Si el método es POST (envío de formulario)
        form = RegistroUsuarioForm(request.POST)  # Crea el formulario con los datos enviados
        if form.is_valid():  # Si el formulario es válido
            form.save()  # Guarda el nuevo usuario
            return redirect('login')  # Redirige a la página de login
    else:
        form = RegistroUsuarioForm()  # Si no es POST, crea un formulario vacío
    # Renderiza la plantilla de registro con el formulario
    return render(request, 'registro.html', {'form': form})


# Login de usuarios
def iniciar_sesion(request):
    if request.method == 'POST':  # Si el método es POST
        usuario = request.POST['username']  # Obtiene el nombre de usuario del formulario
        clave = request.POST['password']  # Obtiene la contraseña del formulario
        user = authenticate(request, username=usuario, password=clave)  # Autentica el usuario
        if user: # Si la autenticación es exitosa
            login(request, user) #Inicia sesión
            return redirect('lista_visitantes')  # Redirige a la página de inicio
        # Si no es POST o la autenticación falla, muestra el formulario de login
    return render(request, 'login.html')

# Logout de usuarios
def cerrar_sesion(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('login')  # Redirige a la página de login


# CRUD de productos

@login_required  # Requiere que el usuario esté autenticado
def lista_visitantes(request):
    visitantes = Visitantes.objects.all()  # Obtiene todos los visitantes de la base de datos
    # Renderiza la plantilla con la lista de visitantes
    return render(request, 'visitantes/lista.html', {'visitantes': visitantes})

@login_required
def agregar_visitantes(request):
    form = VisitantesForm(request.POST or None)  # Crea el formulario con los datos enviados
    if form.is_valid():  # Si el formulario es válido
        form.save()  # Guarda el nuevo visitante
        return redirect('lista_visitantes')  # Redirige a la lista de visitantes
    # Si no es válido o es GET, muestra el formulario
    return render(request, 'visitantes/form.html', {'form': form})

@login_required
def editar_visitantes(request, Cédula_Visitante):
    visitantes = Visitantes.objects.get(Cédula_Visitante=Cédula_Visitante)
    form = VisitantesForm(request.POST or None, instance=visitantes)
    if form.is_valid():
        form.save()
        return redirect('lista_visitantes')
    return render(request, 'visitantes/form.html', {'form': form})

@login_required
def eliminar_visitantes(request, Cédula_Visitante):
    visitantes = Visitantes.objects.get(Cédula_Visitante=Cédula_Visitante)  # Obtiene el visitante por su id
    visitantes.delete()  # Elimina el visitante
    return redirect('lista_visitantes')  # Redirige a la lista de visitantes

def generar_reporte_pdf(request):
    visitantes = Visitantes.objects.all()  #Obtiene todos los productos
    template_path= 'visitantes/reporte_pdf.html'#Ruta de la plantilla HTML para el PDF
    context = {'visitantes' : visitantes} #Contexto con los productos
    response = HttpResponse(content='application/pdf')  #Crea una respuesta HTTP con tipo PDF
    response['Content-Disposition']='attachment;filename="reporte_visitantes.pdf"'
    
    template =get_template(template_path) #Carga una plantilla
    html=template.render(context) #Renderizo la plantilla con el contexto
    
    pisa_status = pisa.CreatePDF(html, dest=response) #Genera el PDF a partir del html
    if pisa_status.err : #Si hay un error al generar el PDF
        return HttpResponse('Hubo un error al generar el PDF', status=500) # Devuelve el error
    return response #Devuelve el PDF generado

@login_required  # Requiere que el usuario esté autenticado
def dashboard_visitantes(request):
    visitantes = Visitantes.objects.all()  # Obtiene todos los visitantes

    nombres = [v.Nombre_Visitante for v in visitantes]  # Usa el campo correcto
    edades = [v.Edad_Visitante for v in visitantes]     # Campo numérico para el gráfico

    return render(request, 'visitantes/dashboard.html', {
        'labels': nombres,  # Eje X: nombres de los visitantes
        'data': edades      # Eje Y: edades
    })