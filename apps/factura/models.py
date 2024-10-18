from django.db import models
from apps.pedidos.models import Pedidos
from apps.detalle.models import DetallePedidos

class Factura(models.Model):
    pedido = models.ForeignKey(Pedidos, related_name='facturas', on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Calcula el total sumando el precio del producto por la cantidad en cada detalle
        self.total = sum(detalle.producto.precio * detalle.cantidad for detalle in DetallePedidos.objects.filter(pedido=self.pedido))
        super().save(*args, **kwargs)
