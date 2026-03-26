from django.urls import path
from .views import *

class EditarMovimientoView(CreateView):
    form_class = MovimientoForm
    template_name = "Movimiento/editar_movimiento.html"

urlpatterns = [
    path('home/', home, name='home'),
    path('exportar/csv/', exportarCSV, name='exportar_csv'),
    path('exportar/csv/<int:year>/<int:month>/', exportarMesCSV, name='exportar_csv_mes'),

    path('categoria/crear/', CreateViewCategoria.as_view(), name='crear_categoria'),
    path('categorias/', lista_categoria, name='lista_categoria'),
    path('categoria/editar/<int:id>/', editar_categoria, name='editar_categoria'),
    path('categoria/eliminar/<int:id>/', eliminar_categoria, name='eliminar_categoria'),
    
    path('movimiento/crear/', CreateViewMovimiento.as_view(), name='crear_movimiento'),
    path('movimiento/editar/<int:id>/', editar_movimiento, name='editar_movimiento'),
    path('movimiento/eliminar/<int:id>/', eliminar_movimiento, name='eliminar_movimiento'),
]