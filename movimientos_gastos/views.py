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

class CreateViewCategoria(LoginRequiredMixin, CreateView):
    model = Categorias
    form_class = CategoriaForm
    template_name = 'categoria/crear_categoria.html'
    success_url = '/home/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class CreateViewMovimiento(LoginRequiredMixin, CreateView):
    model = Movimientos
    form_class = MovimientoForm
    template_name = 'movimiento/crear_movimiento.html'
    success_url = '/home/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['categoria'].queryset = Categorias.objects.filter(
            user=self.request.user
        )
        return form