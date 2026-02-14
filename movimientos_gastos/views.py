from django.shortcuts import render
from django.views.generic import (
    CreateView
)
from .models import Movimientos, Categorias
from movimientos_gastos.formularios.forms import CategoriaForm, MovimientoForm
from django.contrib.auth.mixins import LoginRequiredMixin #Para clases
from django.contrib.auth.decorators import login_required #Para funciones

@login_required(login_url='/')
def home(request):
    return render(request, 'reportes.html')

def index(request):
    data = Movimientos.objects.all()
    stu = {
        "student_number": data
    }
    return render_to_response("login/profile.html", stu)

class CreateViewCategoria(LoginRequiredMixin, CreateView):
    model = Categorias
    form_class = CategoriaForm
    template_name = 'categoria/crear_categoria.html'
    success_url = '/home/'
    
class CreateViewMovimiento(LoginRequiredMixin, CreateView):
    model = Movimientos
    form_class = MovimientoForm
    template_name = 'movimiento/crear_movimiento.html'
    success_url = '/home/'