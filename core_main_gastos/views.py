from django.shortcuts import render
from movimientos_gastos.models import Movimientos, Categorias
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponseRedirect

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
    
    if request.user.is_superuser:
        return render(request, 'reportesAdmin.html', contexto)
    return render(request, 'reportes.html', contexto)

def custom_redirect_view(request):
    return HttpResponseRedirect('/login/')