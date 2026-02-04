from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
    path('home/', home, name='home'),

    path('categoria/crear/', CreateViewCategoria.as_view(), name='crear_categoria'),
    path('movimiento/crear/', CreateViewMovimiento.as_view(), name='crear_movimiento'),
]