from django.db import models
from apps.pedidos.models import Pedidos
from apps.detalle.models import DetallePedidos

# Create your models here.

class Factura(models.Model):
    pedido = models.ForeignKey(Pedidos, related_name='facturas', on_delete=models.SET_NULL, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.total = sum(detalle.producto.precio * detalle.cantidad for detalle in DetallePedidos.objects.filter(pedido=self.pedido))
        super().save(*args, **kwargs)

    def to_json(self):
        detalles = [
            {
                "productos": detalle.producto.nombre,
                "cantidad": detalle.cantidad,
                "modo_entrega":detalle.modo_entrega
            }
            for detalle in DetallePedidos.objects.filter(pedido=self.pedido)
        ]
        return {
            "id": self.id,
            "pedido": {
                "cliente": self.pedido.cliente
            },
            "detalle": detalles,
            "total": f"{self.total:.2f}"
        }

