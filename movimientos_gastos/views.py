from django.shortcuts import render, redirect
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView
)
from .models import *
from movimientos_gastos.formularios.forms import CategoriaForm, MovimientoForm

def home(request):
    return render(request, 'reportes.html')

class CreateViewCategoria(CreateView):
    model = Categorias
    form_class = CategoriaForm
    template_name = 'categoria/crear_categoria.html'
    success_url = '/home/'
    
class CreateViewMovimiento(CreateView):
    model = Movimientos
    form_class = MovimientoForm
    template_name = 'movimiento/crear_movimiento.html'
    success_url = '/home/'