# ya creada este archivo con los pasos anteriores estando desde nuestro interprete productly
# debemos crear una variable llamada urlpatterns y sera igual a un listado
# cuando importamos urls,py lo hacemos con la funcion de include y esta esta esperando una variable
# que se llame urlpatterns y en el listado se indican los patrones de las urls que queremos seguir y mapear con
# nuestas funciones

# Para mapear las urls con las funciones se usara en el listado la funcion de path para ello se debe importar
from django.urls import path

# import views: si se hace de esta forma puede existir un modulo general que se este usando como dependencia
# que se llame views entonces si solo importamos views (import views): va a importar ese modulo
# o paquete que es una dependencia y no va a importar el archivo views que se encuentra
# en la carpeta de productos para ello se debe importar de la siguiente forma # el ounto hace referencia a la carpeta
# donde estamos:
from . import views


# primer argumento de path: se deja vacio ya que esto generaria otra direccion ejemplo productos/lala
# segundo argumento indicar funcion que se encuentra dentro de el archivo de view que debe ejecutar
# y darle de propiedad el nombre de la funcion que le vamos a pasar y debemos crear
# como tercer argumento se indica cual es el nombre de esta ruta en conjunto con esta funcion
# ahora debemos crear el archivo index en el arhivo views.py

app_name = 'productos'
urlpatterns = [
    path('', views.index, name='index'),
        # formulario de Productos:
    path('formulario', views.formulario, name='formulario'),
    path(
        '<int:producto_id>',
        views.detalle,
        name='detalle'
    ),
]