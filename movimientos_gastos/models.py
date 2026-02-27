from django.db import models
from django.contrib.auth.models import User

class Categorias(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    tipo = models.TextField()
    
    def __str__(self):
        return self.nombre

class Movimientos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    monto = models.FloatField()
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)