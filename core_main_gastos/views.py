from django.shortcuts import render
from movimientos_gastos.models import Movimientos, Categorias
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

@login_required(login_url='/login')
def home(request):
    ingresos = Movimientos.objects.filter(user=request.user).filter(categoria__tipo='Ingreso' or '2').aggregate(total=Sum('monto'))['total'] or 0.00
    gastos = Movimientos.objects.filter(user=request.user).filter(categoria__tipo='Gasto' or '1').aggregate(total=Sum('monto'))['total'] or 0.00
    total = ingresos - gastos
    contexto = {
        'movimientos' : Movimientos.objects.filter(user=request.user),
        'categorias' : Categorias.objects.filter(user=request.user),
        'isPrimeraCategoria' : Categorias.objects.filter(user=request.user).count(),
        'ingresos' : ingresos,
        'gastos' : gastos,
        'total' : total
    }
    
    return render(request, 'reportes.html', contexto)