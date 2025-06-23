from django.db import models

# importar tiempo para indicar fecha actual
from django.utils import timezone

# Create your models here.

# Para realizar consultas desde python se debe:
# 1- crear una clase
# 2- darle de argumento models.Model para extender de nuestra clase de model
#      esto nos dara todos los metodos y propiedades que necesitamos para poder
#      interactuar con la base de datos utilizando python y no sql
class Categoria(models.Model):

    #Agregamos la primera propiedad
    # indicar el tipo de dato en las bases de datos se usan otros tipos de datos  
    # el primero es: models.CharField() --> cadena de texto limitada indicar en el argumento este tiene que ser nombrado
    #                                                             como max_length=255 (ejemplo)
    nombre = models.CharField(max_length=255)

    # para redefinir el lnombre del listado de las categorias  en el panel de administración dentro de la pagina
    # para ello se redefine el metodo magico de __str__ ya que esto muestra el nombre de la carpeta por defecto
    # 1- crear funcion 
    # 2- aplicarlo a todas las clases
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=255)

    #crear conteo que existe en stock
    stock = models.IntegerField()

    # puntaje del producto
    puntaje = models.FloatField()

# crear relacion entre las clases en este caso cuando creemos un producto sera relacionado a una categoria
# se creara un metodo para models llamado ForeignKey y se le dara como valor a una variable
# como argumento debemos de pasarle cual es el modelo con el cual vamos a generar esta relacion
# como segundo argumento que es mandatorio el cual es on_Delete= el cual debemos indicar la estrategia a seguir
# la clase de productos cuando eliminemos una categoria que se encuentra asignada a ese producto las indicaciones son las siguientes:
# CASCADE: elimina el producto si esque se elimina la categoria
# PROTECT:  lanza un error y no dejara eliminar la categoria 
# RESTRICT: no dejara eliminar la categoria a menos que se eliminen todos los productos
# SET_NULL: hara setear un valor nullo (actualiza a valor nulo)
# SET_DEFAULT: asignar el valor por defecto
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )

# Para siguiente paso se debe cargar los modelos en la base de datos
# Para ello son las migraciones
# en la terminal escribir: python manage.py makemigrations
# ahora nos movemos a settings

# ACTUALIZANDO MODELOS
# se creara ahora una variante que contendra una funcion para tener un registro
# de cuando fue creado un producto de forma automatica para ello debemos importar
# desde django.utils import timezone y se dejara sin ejecutar ya si se hace marcara el mismo dia para todos los productos
    creado_en = models.DateTimeField(default=timezone.now)

# Ahora para continuar con la actualizacion escribir en la terminal: python manage.py makemigrations
# despues se crea un archivo y debemos ejecutar esa migracion con: python manage.py migrate
# podemos verificar en la base de datos con sqlite browser

# GESTIONAR NUESTROS MODELOS EN EL PANEL DE ADMINISTRACION
# 1- ejecutar nuestro servidor de desarrollo escribiendo en la terminal:
# python manage.py runserver
# ahora debemos crear un nuevo administrador para ello debemos escribir en la terminal:
# python manage.py createsuperuser seguir instrucciones

# ahora para ver los modelos en la pagina se deben configurar
# para ello nos vamos al archivo de admin -->

    def __str__(self):
        return self.nombre