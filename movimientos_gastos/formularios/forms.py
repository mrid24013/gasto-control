from django import forms
from movimientos_gastos.models import Categorias, Movimientos, User

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = "__all__"
        opciones = [('1','Gasto'), ('2','Ingreso')]
        labels = {
            'nombre': 'Nombre de la categoria',
            'tipo': 'Tipo de categoria',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'forms-control'}),
            'tipo': forms.Select(choices=opciones),
        }
        
class MovimientoForm(forms.ModelForm):
    class Meta:
        model = Movimientos
        fields = "__all__"
        labels = {
            'monto': 'Cantidad de dinero del movimiento',
            'fecha': 'Fecha del movimiento',
            'descripcion': 'Descripcion del movimiento',
        }
        widgets = {
            'monto': forms.TextInput(attrs={'class': 'forms-control'}),
            'fecha': forms.DateInput(attrs={'class': 'forms-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'forms-control'}),
        }