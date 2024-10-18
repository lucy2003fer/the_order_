from rest_framework.routers import DefaultRouter
from apps.factura.api.views import FacturaViewSet

router_factura = DefaultRouter()
router_factura.register(prefix="facturas", basename="factura", viewset=FacturaViewSet)