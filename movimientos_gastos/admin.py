from django.contrib import admin
from .models import *
from import_export import resources 
from import_export.admin import ImportExportModelAdmin 

class MovimientosResource(resources.ModelResource): 
    class Meta: 
        model = Movimientos 
    
class MovimientosAdmin(ImportExportModelAdmin): 
    resource_class = MovimientosResource
    
class CategoriasResource(resources.ModelResource): 
    class Meta: 
        model = Categorias 
    
class CategoriasAdmin(ImportExportModelAdmin): 
    resource_class = CategoriasResource

admin.site.register(Movimientos, MovimientosAdmin)
admin.site.register(Categorias, CategoriasAdmin)