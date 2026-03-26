from django import forms
from movimientos_gastos.models import Categorias, Movimientos

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categorias
        exclude = ['user']
        opciones = [('Gasto','Gasto'), ('Ingreso','Ingreso')]
        labels = {
            'nombre': 'Nombre de la categoria',
            'tipo': 'Tipo de categoria',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(choices=opciones, attrs={'class': 'form-control'}),
        }
        
class MovimientoForm(forms.ModelForm):
    class Meta:
        model = Movimientos
        exclude = ['user']
        labels = {
            'monto': 'Cantidad de dinero del movimiento',
            'fecha': 'Fecha del movimiento',
            'descripcion': 'Descripcion del movimiento',
            'categoria': 'Categoria del movimiento',
        }
        widgets = {
            'monto': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateTimeInput( attrs={'class': 'form-control', 'type': 'datetime-local'}, 
                                         format='%Y-%m-%dT%H:%M'),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }