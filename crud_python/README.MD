1. ¿Qué es un CRUD y cuál es su propósito en el desarrollo de aplicaciones web?
CRUD se refiere a las cuatro operaciones básicas que una aplicación debería poder realizar: Create (Crear), Read (Leer), Update (Actualizar) y Delete (Eliminar).

En una aplicación, el usuario debe poder crear datos, leerlos y acceder a ellos desde la interfaz gráfica, actualizarlos o editarlos y eliminarlos.

Las aplicaciones CRUD completas constan de tres partes: API (servidor), base de datos e interfaz de usuario (UI). La API contiene código y métodos; la base de datos almacena y permite extraer la información; la UI permite la interacción del usuario con la aplicación.

Ejemplo: WordPress depende en gran medida de las operaciones CRUD para gestionar el contenido almacenado en sus bases de datos.

2. ¿Qué son los patrones de arquitectura en desarrollo de software?
Un patrón arquitectónico es una solución general y reutilizable a un problema común en la arquitectura de software dentro de un contexto dado. Tienen un alcance más amplio que los patrones de diseño.

¿Qué es el patrón MVC (Modelo–Vista–Controlador)? MVC divide una aplicación en tres partes: modelo (contiene la funcionalidad y los datos básicos), vista (muestra la información al usuario) y controlador (maneja la entrada del usuario). El objetivo es separar la representación interna de la información de las formas de presentación y aceptación de datos, favoreciendo el desacoplamiento y la reutilización.

¿Qué es el patrón MVT (Modelo–Vista–Template)? En Django el "controlador" está integrado en el framework; la separación es: modelo (maneja acceso a datos, validación y comportamiento), vista (enlace entre modelo y template; decide qué mostrar y qué template usar) y template (define cómo se presenta la información en HTML).

Diferencias clave (MVC vs MVT): M tiene la misma función en ambos (interactuar con la BD). En MVC la V genera HTML y C es el controlador; en MVT la View actúa como el controlador de MVC y el Template es responsable del HTML.

3. ¿Cómo se estructura un proyecto en Django? Explicar brevemente el rol de los modelos, vistas, templates y URLs.
En Django, un proyecto está compuesto por una o varias aplicaciones (apps). Cada app suele contener models.py (clases que representan tablas y datos de la base de datos), views.py (funciones o clases que manejan solicitudes HTTP y devuelven respuestas), templates/ (archivos HTML para renderizar páginas) y urls.py (mapeo de rutas URL a vistas, a nivel de app y de proyecto).

Flujo básico: el navegador solicita una URL; urls.py dirige la solicitud a una view; la view utiliza models para obtener o modificar datos; la view renderiza un template y retorna la respuesta HTML.

El signo %% no es sintaxis estándar de Django. En templates Django se usan {% ... %} para tags y {{ ... }} para variables; %% puede aparecer en otros motores o como escape en ciertas herramientas, pero en templates Django no tiene significado propio.

4. ¿Cuál es el flujo de datos entre un formulario HTML y la base de datos en Django?
Django proporciona la clase Form para definir la estructura y validaciones de formularios HTML. ModelForm genera un formulario a partir de un modelo (mapea campos del modelo al formulario).

Flujo típico: la view muestra un formulario (Form o ModelForm) en un template; el usuario envía el formulario (POST); la view instancia el formulario con request.POST y llama a is_valid(); si es válido, con ModelForm.save() (o manipulando el modelo manualmente) se crean/actualizan registros en la base de datos; la view redirige o renderiza la respuesta adecuada.

5. ¿Qué herramientas o comandos ofrece Django para facilitar el desarrollo de un CRUD, para qué es cada una?
django-admin startproject <project_name> — crea la estructura inicial del proyecto.
python manage.py startapp <app_name> — crea una app dentro del proyecto.
python manage.py makemigrations — genera migraciones a partir de los modelos.
python manage.py migrate — aplica migraciones y crea/actualiza tablas en la base de datos.
python manage.py runserver — ejecuta el servidor de desarrollo local.
ModelForm — clase que facilita create/update basado en modelos.
admin — panel administrativo que permite gestionar modelos y realizar operaciones CRUD sin construir un panel desde cero.

6. ¿Cómo funciona el Admin de Django?
Django Admin es una aplicación incluida por defecto que proporciona una interfaz de gestión para los modelos del proyecto. Permite crear, editar y eliminar registros (usuarios, productos, comentarios, categorías, etc.) sin necesidad de construir un panel desde cero; hay que registrar cada modelo en admin.py para que aparezca en el panel.

7. ¿Django usa la arquitectura REST? ¿Qué es Django Rest Framework?
Django por sí mismo no es un framework REST, pero permite construir APIs HTTP. Django REST Framework (DRF) es una librería que facilita crear APIs RESTful con Django: ofrece serializers, vistas genéricas, routers, autenticación y una interfaz de exploración de la API para probar operaciones HTTP (GET, POST, PUT, DELETE, etc.).