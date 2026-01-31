from django.urls import path
from .views import *

urlpatterns = [
    
    path('usuarios/', home, name= 'home')
    
]