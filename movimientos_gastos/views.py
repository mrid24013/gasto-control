from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import (
    CreateView
)
from .models import Movimientos, Categorias
from movimientos_gastos.formularios.forms import CategoriaForm, MovimientoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import pandas as pd

@login_required(login_url='/')
def home(request):
    return render(request, 'reportes.html')

class CreateViewCategoria(LoginRequiredMixin, CreateView):
    model = Categorias
    form_class = CategoriaForm
    template_name = 'Categoria/crear_categoria.html'
    success_url = '/categorias/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@login_required(login_url='/login')
def exportarCSV(request):
    movimientos = Movimientos.objects.filter(user=request.user).order_by('-fecha')

    datos = []
    for m in movimientos:
        datos.append({
            'Monto': m.monto,
            'Descripcion': m.descripcion,
            'Categoria': m.categoria.nombre,
            'Tipo': m.categoria.tipo,
            'Fecha': m.fecha.strftime('%Y-%m-%d %H:%M')
        })

    df = pd.DataFrame(datos)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="movimientos_{request.user}.csv"'

    df.to_csv(response, index=False, encoding='utf-8-sig')
    return response

@login_required(login_url='/login')
def exportarMesCSV(request, year, month):
    movimientos = Movimientos.objects.filter(
        user=request.user,
        fecha__year=year,
        fecha__month=month
    ).order_by('fecha')

    datos = []
    for m in movimientos:
        datos.append({
            'Monto': m.monto,
            'Descripcion': m.descripcion,
            'Categoria': m.categoria.nombre,
            'Tipo': m.categoria.tipo,
            'Fecha': m.fecha.strftime('%Y-%m-%d %H:%M')
        })

    df = pd.DataFrame(datos)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="movimientos_{year}_{month}.csv"'

    df.to_csv(response, index=False, encoding='utf-8-sig')
    return response

@login_required(login_url='/')
def lista_categoria(request):
    if Categorias.objects.filter(user=request.user).count() == 0:
        return redirect('/home/')
    else:
        categorias = Categorias.objects.filter(user=request.user)
        return render(request, 'Categoria/lista_categoria.html', {
            'categorias': categorias
        })
    
@login_required(login_url='/')
def editar_categoria(request, id):
    categoria = get_object_or_404(Categorias, id=id, user=request.user)

    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('/categorias/')
    else:
        form = CategoriaForm(instance=categoria)

    return render(request, 'Categoria/editar_categoria.html', {'form': form})


@login_required(login_url='/')
def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categorias, id=id, user=request.user)
    existe = Movimientos.objects.filter(user=request.user,categoria=categoria).exists()
    
    if existe:
        messages.warning(request, "No puedes eliminar una categoría con movimientos")
        return redirect('/categorias/')
    elif request.method == 'POST':
        categoria.delete()
        return redirect('/categorias/')
    
class CreateViewMovimiento(LoginRequiredMixin, CreateView):
    model = Movimientos
    form_class = MovimientoForm
    template_name = 'Movimiento/crear_movimiento.html'
    success_url = '/home/'
    
    def dispatch(self, request, *args, **kwargs):
        if not Categorias.objects.filter(user=request.user).exists():
            messages.warning(
                request,
                'Debes crear al menos una categoría antes de registrar movimientos.'
            )
            return redirect('/home/')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['categoria'].queryset = Categorias.objects.filter(
            user=self.request.user
        )
        return form
    
@login_required(login_url='/')
def editar_movimiento(request, id):
    movimiento = get_object_or_404(Movimientos, id=id, user=request.user)

    if request.method == 'POST':
        form = MovimientoForm(request.POST, instance=movimiento)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MovimientoForm(instance=movimiento)

    # Filtrar categorías del usuario
    form.fields['categoria'].queryset = Categorias.objects.filter(user=request.user)

    return render(request, 'Movimiento/editar_movimiento.html', {'form': form})

@login_required(login_url='/')
def eliminar_movimiento(request, id):
    movimiento = get_object_or_404(Movimientos, id=id, user=request.user)

    if request.method == 'POST':
        movimiento.delete()
        return redirect('home')

    return redirect('home')