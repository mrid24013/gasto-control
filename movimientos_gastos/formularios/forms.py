from django import forms
from movimientos_gastos.models import Categorias, Movimientos

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categorias
        #fields = ['nombre', 'tipo']
        fields = "__all__"
        labels = {
            'nombre': 'Nombre de la categoria',
            'tipo': 'Tipo de categoria',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'forms-control'}),
            'tipo': forms.TextInput(attrs={'class': 'forms-control'}),
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
            'fecha': forms.TextInput(attrs={'class': 'forms-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'forms-control'}),
        }