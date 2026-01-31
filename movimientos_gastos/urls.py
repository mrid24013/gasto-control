from django.urls import path
from .views import *

urlpatterns = [
    #path('movimientos/', home, name= 'home'),
    path('', home, name= 'home'),
    
    path('categoria/crear/', CreateViewCategoria.as_view(), name='crear_categoria'),
    path('movimiento/crear/', CreateViewMovimiento.as_view(), name='crear_movimiento'),
]