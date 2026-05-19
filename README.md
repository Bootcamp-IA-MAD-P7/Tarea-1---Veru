1. ¿Qué es un CRUD y cuál es su propósito en el desarrollo de aplicaciones web?
Añade un ejemplo de aplicación web que use una estructura de CRUD

CRUD se refiere a las cuatro operaciones básicas que una aplicación debería poder hacer- "Create - Crear", "Read - Leer", "Update - Actualizar" y "Delete - eliminar"

En una aplicación, el usuario debe de ser capaz de crear datos, poder leerlos y tener acceso a ellos desde la interfaz gráfica, actualizar o editar los datos y ser capaz de eliminarlos.

Las aplicaciones CRUD completas, consisten de 3 partes: una API (o servidor), una base de datos y una interfaz de usuario (IU/UI - user interface).

La API contiene código y métodos, la base de datos almacena y ayuda al usuario a extraer información, mientras que la interfaz de usuario ayuda a los usuarios a interactuar con la aplicación.

**Wordpress es un ejemplo, ya que depende en gran medida de las operaciones CRUD** para gestionar el contenido almacenado en sus bases de datos.

2. ¿Qué son los patrones de arquitectura en desarrollo de software?
Un patrón arquitectónico es una solución general y reutilizable a un problema común en la arquitectura de software dentro de un contexto dado. Los patrones arquitectónicos son similares al patrón de diseño de software pero tienen un alcance más amplio.

○ ¿Qué es el patrón MVC (Modelo–Vista–Controlador)?
Este patrón, también conocido como patrón MVC, divide una aplicación interactiva en 3 partes, como

modelo — contiene la funcionalidad y los datos básicos
vista : muestra la información al usuario (se puede definir más de una vista)
controlador : maneja la entrada del usuario
Esto se hace para separar las representaciones internas de información de las formas en que se presenta y acepta la información del usuario. Desacopla los componentes y permite la reutilización eficiente del código.

○ ¿Qué es el patrón MVT (Modelo–Vista–Template)?
En Django, el controlador sigue estando presente, nada más que de una manera intrínseca, ya que todo el framework Django es el controlador.

Modelo: Maneja todo lo relacionado con la información, esto incluye como acceder a esta, la validación, relación entre los datos y su comportamiento.

Vista: Es un enlace entre el modelo y el template. Decide que información sera mostrada y por cual template.

Template: Decide como sera mostrada la información.

○ Diferencias entre MVC y MVT.
M se escribe todo como Modelo, que principalmente encapsula el acceso a la capa de la base de datos y realiza operaciones de agregar, eliminar, modificar y verificar datos en la base de datos.

V se escribe como Ver, que se utiliza para encapsular el resultado y generar el contenido html que se muestra en la página.

C se escribe como controlador, que se usa para recibir solicitudes, procesar la lógica comercial, interactuar con el modelo y la vista, y devolver resultados.

M se escribe como Model, que tiene la misma función que M en MVC, y es responsable de interactuar con la base de datos y procesar los datos.

V se escribe como View, que tiene la misma función que C en MVC. Recibe solicitudes, procesa negocios y devuelve respuestas.

T está escrito como Template, que tiene la misma función que V en MVC, y es responsable de encapsular y construir el html devuelto.

○ ¿Cuál de estos dos patrones se usa en Django?
MVC

3. ¿Cómo se estructura un proyecto en Django? Explicar brevemente el rol de los
modelos, vistas, templates y URLs.

En Django, una aplicación es un módulo independiente que se utiliza para organizar nuestro código. Una aplicación puede contener varios modelos, vistas y templates. Las aplicaciones se organizan en carpetas dentro de la carpeta app del proyecto. Cada aplicación tiene su propio directorio y contiene los siguientes archivos importantes:

models.py: El archivo donde definimos nuestros modelos, que son clases que representan los datos de nuestra base de datos.
views.py: Un módulo que contiene las vistas, que son funciones que manejan las solicitudes HTTP y devuelven respuestas.
templates: La carpeta donde almacenamos nuestros templates HTML para renderizar las páginas web.

○ ¿Para qué se usa el signo “%%” en los templates?


4. ¿Cuál es el flujo de datos entre un formulario HTML y la base de datos en Django?
Django proporciona una clase Form que se utiliza para crear formularios HTML, o mejor dicho, sus campos, ya que con los mismos podemos describir cuales son los campos, de qué tipo (enteros, flotantes, campos de textos, listados...) y cómo funciona y aparece. Es similar a la clase ModelForm que crea un formulario utilizando el modelo, pero no requiere el modelo, por lo tanto, son más manuales y flexibles que estos últimos.

Un formulario en Django es una clase de Python que representa una estructura de entrada de datos, mapea campos HTML (<input>, <select>, etc.) y aplica validaciones automáticas.

5. ¿Qué herramientas o comandos ofrece Django para facilitar el desarrollo de un
CRUD, para qué es cada una? (Por ejemplo: startapp, makemigrations, migrate,
runserver, ModelForm, admin, etc.)

django-admin startproject <project_name>
creará un directorio/carpeta con el proporcionado en el comando dentro del directorio de trabajo actual.

python manage.py makemigrations
Para convertir el código de Python escrito para las clases modelo (que además representa tablas en la base de datos) en consultas de base de datos.

python manage.py migrate
Necesitamos ejecutar este comando para crear tablas en la base de datos especificada en función de los modelos de clase de Python definidos.

python manage.py startapp <app_name>

Un proyecto Django es una colección de aplicaciones y configuraciones para un sitio web. Un proyecto puede tener varias aplicaciones dentro y una aplicación puede incluirse en varios proyectos de Django. Este comando es necesario para crear una aplicación Django dentro del proyecto Django que generará la estructura de directorio básica de una aplicación Django.

python manage.py runserver 
Necesitamos este comando para verificar y probar nuestras aplicaciones y sitios web de Django ejecutándolos en el servidor local. 



6. ¿Cómo funciona el Admin de Django?
Django Admin es una aplicación que viene instalada por defecto en cualquier proyecto creado con el comando:

django-admin startproject
Su objetivo es ofrecer una interfaz de gestión para los modelos de tu aplicación. Gracias a este panel, puedes crear usuarios, agregar productos, revisar comentarios o administrar categorías sin construir un panel desde cero.

7. ¿Django usa la arquitectura REST? ¿Qué es Django Rest Framework?
   
Django Rest Framework es una aplicación Django que permite construir proyectos software bajo la arquitectura REST, incluye gran cantidad de código para reutilizar (Views, Resources, etc.) y una interfaz administrativa desde la cual es posible realizar pruebas sobre las operaciones HTTP como lo son: POST y GET.

