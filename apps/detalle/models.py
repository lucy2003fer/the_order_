from django.db import models

# Create your models here.

class DetallePedidos(models.Model):
    MODO_ENTREGA = [
        ('Para llevar', 'llevar'),
        ('Para consumir en el sitio', 'aqui'),
    ]
    
    modo_entrega = models.CharField(max_length=50, choices=MODO_ENTREGA)
    pedido = models.ForeignKey('pedidos.Pedidos', related_name='detalles_pedido', on_delete=models.SET_NULL, null=True)
    producto = models.ForeignKey('productos.Productos', related_name='detalles_producto', on_delete=models.SET_NULL, null=True) 
    cantidad = models.PositiveIntegerField()
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} ({self.pedido.cliente})"