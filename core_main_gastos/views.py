from django.shortcuts import render
from movimientos_gastos.models import Movimientos, Categorias
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponseRedirect
from collections import defaultdict

@login_required(login_url='/login')
def home(request):
    movimientos = Movimientos.objects.filter(user=request.user).order_by('fecha')
        
    data_mensual = []
        
    for m in movimientos:
        clave = (m.fecha.year, m.fecha.month)
        encontrado = next((item for item in data_mensual if item['clave'] == clave), None)
    
        if not encontrado:
            data_mensual.append({
                'clave': clave,
                'mes': m.fecha.strftime('%B %Y'),
                'year': m.fecha.year,
                'month': m.fecha.month,
                'movimientos': [],
                'ingresos': 0,
                'gastos': 0,
                'total': 0
            })
            encontrado = data_mensual[-1]
        encontrado['movimientos'].append(m)

        if m.categoria.tipo == "Ingreso":
            encontrado['ingresos'] += m.monto
        else:
            encontrado['gastos'] += m.monto

        encontrado['total'] = encontrado['ingresos'] - encontrado['gastos']
    
    ingresos = movimientos.filter(categoria__tipo='Ingreso').aggregate(total=Sum('monto'))['total'] or 0.00
    gastos = movimientos.filter(categoria__tipo='Gasto').aggregate(total=Sum('monto'))['total'] or 0.00
    total = ingresos - gastos
    
    contexto = {
        'data_mensual': data_mensual,
        'movimientos' : movimientos,
        'isPrimerMovimiento' : movimientos.count(),
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