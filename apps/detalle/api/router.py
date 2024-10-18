from rest_framework.routers import DefaultRouter
from apps.detalle.api.views import DetalleViewSet

router_detalle = DefaultRouter()
router_detalle.register(prefix="detalles", basename="detalle", viewset=DetalleViewSet)