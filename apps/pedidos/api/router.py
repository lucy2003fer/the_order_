from rest_framework.routers import DefaultRouter
from apps.pedidos.api.views import PedidosViewSet

router_pedidos = DefaultRouter()
router_pedidos.register(prefix="pedidos", basename="pedido", viewset=PedidosViewSet)