# para crear la funcion de pagina de inicio debemos importar
from django.shortcuts import render

# 1- definimos funcion y de argumento request
def inicio(request):
    # 2- devolvemos render
    return render(
        request,
        # 3- y devolver la plantilla que vamos a usar cuando lleguemos a la pagina de inicio
        'inicio.html',
    )