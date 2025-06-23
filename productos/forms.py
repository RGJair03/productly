# esta seccion funcionara para crearle a los usuarios su propia interfaz de administradores para que puedan interactuar
# con los productos
# existe en django una dependencia llamada ModelForm para crear estos formularios en html, csss y validarlos:
# ModelForms: tomara los productos que ya creamos en el archivo model y en base en ellos creara las formularios

# 1- importar modelos
from . import models

# 2- importar paquete de django
from django.forms import ModelForm

# 3- crear clase y extender de ModelForm
class ProductoForm(ModelForm):
    # 4- crear clase dentro de modelform
    class Meta:
        # 5- indicar el modelo que debe utilizar para crear el formulario
        model = models.Producto
        # 6- indicar los campos que queremos que utilice el formulario que creamos de ProductForm:
        # esto se realizara en base a una lista donde se encontrara los campos como viene exacto de los campos que
        # se encontraran dentro de nuestro formulario
        fields = ['nombre', 'stock', 'puntaje', 'categoria']

# 7- Instalar django.forms ---> ir a settings.py en la carpeta de productly en este caso
# 8- registar la nueva ruta en urls ---> ir a urls de la carpeta productos en este caso
# 9- ir a views dentro de la carpeta productos en este caso
# 10- ir a templates y crear nuevo archivo con el nombre de la plantilla asignada en views