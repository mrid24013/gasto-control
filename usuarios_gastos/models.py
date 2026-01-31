from django.db import models
from django.contrib.auth.models import User

class usuario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    puesto = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    fecha_inicio = models.DateTimeField(auto_now_add=True)