from django.db import models
from apps.productos.models import Productos

# Create your models here.

class Pedidos(models.Model): 
    ESTADOS = [
        ('espera', 'Espera'),
        ('preparación', 'Preparación'),
        ('terminado', 'Terminado'),
    ]

    cliente = models.CharField(max_length=255)
    estado = models.CharField(max_length=50, choices=ESTADOS, default='espera')
    fecha = models.DateTimeField(auto_now_add=True)

    productos = models.ManyToManyField(Productos, through='detalle.DetallePedidos')

    def __str__(self):
        return self.cliente