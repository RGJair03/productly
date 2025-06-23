from django.contrib import admin

# Register your models here.
# 1- Importarlos
from .models import Categoria, Producto

# Para personalizar lo que se mostrara en el panel de administracion tendremos que crear
# una nueva clase que servira para poder representar las cosas que queremos mostrar o ocultar en el panel de adm
# para ello se le pasa como segundo argumento en el modelo registrado
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre') # de esta forma se mostraran los atributos en la carpeta

class ProductoAdmin(admin.ModelAdmin):
    
    #ocultar secciones en el panel de adm
    exclude = ('creado_en', ) # al ser una tupla se debe agregar un espacio para que reconozca que no es un str envuelto en un parentesis

    # columnas a mostrar en el panel de adm
    list_display = ('id', 'nombre', 'stock', 'creado_en')

# 2- Registrar modelos, para ello debemos llamar a un metodo
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
