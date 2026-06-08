1. ¿Qué es un CRUD y cuál es su propósito en el desarrollo de aplicaciones web?
CRUD se refiere a las cuatro operaciones básicas que una aplicación debería poder realizar: Create (Crear), Read (Leer), Update (Actualizar) y Delete (Eliminar).

En una aplicación, el usuario debe poder:

Crear datos.
Leerlos y acceder a ellos desde la interfaz gráfica.
Actualizarlos o editarlos.
Eliminarlos.
Las aplicaciones CRUD completas constan de tres partes:

API (servidor) — contiene código y métodos.
Base de datos — almacena y permite extraer la información.
Interfaz de usuario (UI) — permite la interacción del usuario con la aplicación.
Ejemplo: WordPress depende en gran medida de las operaciones CRUD para gestionar el contenido almacenado en sus bases de datos.

2. ¿Qué son los patrones de arquitectura en desarrollo de software?
Un patrón arquitectónico es una solución general y reutilizable a un problema común en la arquitectura de software dentro de un contexto dado. Tienen un alcance más amplio que los patrones de diseño.

¿Qué es el patrón MVC (Modelo–Vista–Controlador)?
MVC divide una aplicación en tres partes:

Modelo — contiene la funcionalidad y los datos básicos.
Vista — muestra la información al usuario (puede haber varias vistas).
Controlador — maneja la entrada del usuario.
Objetivo: separar la representación interna de la información de las formas de presentación y aceptación de datos, favoreciendo el desacoplamiento y la reutilización.

¿Qué es el patrón MVT (Modelo–Vista–Template)?
En Django el "controlador" está integrado en el framework; la separación es:

Modelo — maneja acceso a datos, validación y comportamiento.
Vista — enlace entre modelo y template; decide qué mostrar y qué template usar.
Template — define cómo se presenta la información (HTML).
Diferencias clave (MVC vs MVT)
Elemento	MVC	MVT (Django)
M	Modelo: interactúa con la BD	Model: misma función
V	Vista: genera HTML	View: similar al controlador de MVC
C / T	Controlador: recibe solicitudes y controla flujo	Template: responsable del HTML
Nota: Django implementa la variante conocida como MVT, que conceptualmente se alinea con MVC.

3. ¿Cómo se estructura un proyecto en Django?
En Django, un proyecto está compuesto por una o varias aplicaciones (apps). Cada app suele contener:

models.py — clases que representan tablas y datos de la base de datos.
views.py — funciones o clases que manejan solicitudes HTTP y devuelven respuestas.
templates/ — archivos HTML para renderizar páginas.
urls.py — mapeo de rutas URL a vistas (a nivel de app y proyecto).
Flujo básico
El navegador solicita una URL.
urls.py dirige la solicitud a una view.
La view utiliza models para obtener o modificar datos.
La view renderiza un template y retorna la respuesta HTML.
¿Para qué se usa el signo %% en los templates?
No es sintaxis estándar de Django. En Django se usan:

{% ... %} para tags (lógica).
{{ ... }} para variables.
%% puede aparecer en otros motores o como escape en ciertas herramientas, pero en templates Django no tiene significado propio.

4. Flujo de datos entre un formulario HTML y la base de datos en Django
Form define estructura y validaciones de formularios HTML (campos, tipos, validadores).
ModelForm genera un formulario a partir de un modelo (mapea campos del modelo al formulario).
Flujo típico:

La view muestra un formulario (instancia de Form o ModelForm) en un template.
El usuario envía el formulario (método POST).
La view instancia el formulario con request.POST y llama a is_valid().
Si es válido, ModelForm.save() (o manipulación directa del Model) crea/actualiza registros en la BD.
La view redirige o renderiza la respuesta adecuada.
py


# Ejemplo mínimo en views.py
from django.shortcuts import render, redirect
from .forms import MiModeloForm

def crear_objeto(request):
    if request.method == "POST":
        form = MiModeloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = MiModeloForm()
    return render(request, 'miapp/form.html', {'form': form})
5. Herramientas y comandos de Django útiles para CRUD
django-admin startproject <project_name> — crea la estructura inicial del proyecto.
python manage.py startapp <app_name> — crea una app dentro del proyecto.
python manage.py makemigrations — genera migraciones a partir de los modelos.
python manage.py migrate — aplica migraciones y crea/actualiza tablas en la BD.
python manage.py runserver — ejecuta el servidor de desarrollo local.
ModelForm — facilita create/update basado en modelos.
admin — panel administrativo para gestionar modelos (CRUD).
6. ¿Cómo funciona el Admin de Django?
Django Admin es una aplicación incluida por defecto que proporciona una interfaz de gestión para los modelos. Permite crear, editar y eliminar registros sin construir un panel desde cero; hay que registrar los modelos en admin.py para que aparezcan.

py


# admin.py
from django.contrib import admin
from .models import MiModelo

@admin.register(MiModelo)
class MiModeloAdmin(admin.ModelAdmin):
    list_display = ('id', 'campo1', 'campo2')
7. ¿Django usa la arquitectura REST? ¿Qué es Django REST Framework?
Django no es un framework REST por sí mismo, pero permite construir APIs HTTP.
Django REST Framework (DRF) es una librería que facilita crear APIs RESTful: serializers, vistas genéricas, routers, autenticación y una interfaz de exploración de la API para probar operaciones HTTP (GET, POST, PUT, DELETE, ...).
py


# Ejemplo mínimo con DRF (views.py)
from rest_framework import viewsets
from .models import MiModelo
from .serializers import MiModeloSerializer

class MiModeloViewSet(viewsets.ModelViewSet):
    queryset = MiModelo.objects.all()
    serializer_class = MiModeloSerializer