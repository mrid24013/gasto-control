from django.shortcuts import render

def home(request):
    contexto = {
        'mensaje': 'Bienvenido al sistema de manejo de gastos',
        "user": request.user
    }
    
    return render(request, 'login.html', contexto)