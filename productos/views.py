# para devolver no un elemeto si no devolver un listado de todos los productos
# para ello por ahora sera un json y se debe importar desde django.http incluimos jsonResponse

from django.http import Http404, HttpResponse, HttpResponseRedirect #JsonResponse

# importar respuesta
from django.shortcuts import render, get_object_or_404

from .forms import ProductoForm

# para listar elementos en la url de /productos
#1- en ves de devolver 'Hola Mundo' vamos a devolver datos
# 2- importar nuestro modelo
from .models import Producto

# Create your views here.

#  Para definir nuestras vistas debemos crear una funcion
# la cual esta funcion se va a urls.py
# siempre recibira el argumento de request y retornar  httpsresponse 
def index(request):
    # return HttpResponse('Hola Mundo')

    # 3- crear variable con valor de la clase Producto y seleccionar el metodo con propiedad de objects
    # 4- al mismo objects se le asigna el metodo de all este nos va a permitir buscar todos los registros que se encuentran
    #      dentro de nuestra base de datos

    # forma con http
    # productos = Producto.objects.all()

    # forma con json: agregar .values() para indicar a productos que nos devulva los valores con su metodo
    productos = Producto.objects.all()#.values()

    # pasos para platillas
    return render(
        request,
        'index.html', #  crear la plantilla porque aun no esta creada
        context={'productos': productos}
    ) 

# para crear plantillas debemos crear una carpeta dentro de productos llamada templates y crear el archivo tal cual aparece
# index.html --> ir al archivo

    # opcion con http
    # print(productos)
    # return HttpResponse('Hola Mundo')

    # acceder a producto 1 con http
    # return HttpResponse(productos[0].nombre)

    # reponder con json: solo puede devolver datos que son diccionarios por ello productos lo volvemos un listado
    # y agregar como segundo parametro safe=False
    # return JsonResponse(list(productos), safe=False)

    # de esta forma podremos pasarle argumentos nombrados que van a permitir que nuestras consultas sean un poco mas complejas
    # en este caso los productos tienen un puntaje asi que puedo buscar productos por puntaje y eso se le agrega como argumento
    # forma 1:
    # productos = Producto.objects.filter(puntaje=3)
    # forma 2: para buscar un valor de mayor o igual a 3 se agregan argumentos nombrados magicos
    # productos = Producto.objects.filter(puntaje__gte=3) 

    # Para buscar un producto en particular
    # productos = Producto.objects.get(id=3)
    # o por primary key
    # productos = Producto.objects.get(pk=3)

    

# en este paso podemos verificar desde la terminar ejecutar: python manage.py runserver

# corregir errores de compilador
# 1- para ello debemos instalar un pylint para que funcione en conjunto de pylintrc
# 2- escribir en la terminal integrada pipenv install pylint-django
# 3- crear un nuevo archivo dentro de productly en este caso al nivel de pipfile.lock, manage.py etc
#     con nombre .pylintrc
# 4- una vez instalado ir al archivo para ver instrucciones


# Trabajar con plantillas en django debemos cambiar la implementacion de la funcion creada index que trabajamos con json
# 1- quitar la importancion de jsonResponse y dentro de la funcion eliminar el return de json y el metodo de .values() en productos
# 2- y retornar en la funcion la funcion de render recibiendo como argumentos el parametro mismo de la funcion osea request
# 3- seguir con el argumento con str de donde se encuentra la plantilla y su nombre 
# 4- despues otro argumento sera de indicar los datos que le vamos a pasar a esta plantilla para que los renderice despues
#      y se los muestre al usuario y eso se hace con el argumento de context ={} este recibe el nombre de la propiedad que en este caso
#      es productos en forma de dato str y pasarle el valor que vamos a listar con : que son los productos

# def detalle(request, producto_id):
#     return HttpResponse(producto_id)

# obtener un elemento
def detalle(request, producto_id):
    # try:
    producto = get_object_or_404(Producto, id=producto_id)
    # producto = Producto.objects.get(id=producto_id)

    return render(
        request,
        'detalle.html',
        context={'producto': producto })

    # except Producto.DoesNotExist: 
    #     raise Http404()

    # formulario
    # 1- definir nueva funcion
def formulario(request):
    # guardando formularios si esque este es post 
    if request.method == 'POST':
        
    
    # para mostrar un formulario dentro de una plantilla html:
    # crear un formulario  en base a la clase que acabamos de crear
    # importar ProductoForm
    # guardar formulario darselo de argumento
        form = ProductoForm(request.POST)
        # validar formulario e insertarlo en nuestra base de datos
        if form.is_valid():
            form.save() # este insertara el formulario dentro de la base de datos
            return HttpResponseRedirect('/productos') # esto hara que redirigira al usuario a una nueva url
    else:
        form = ProductoForm()


    return render(
        request,

        # plantilla que vamos a renderizar
        'producto_form.html',

        # contexto que queremos que tenga la plantilla anterior:
        # pasar el formulario
        {'form': form}
    )