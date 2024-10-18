from rest_framework.viewsets import ModelViewSet
from apps.factura.models import Factura
from apps.factura.api.serializer import FacturaSerializer

class FacturaViewSet(ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
    #permisos metodos
    #http_method_names = ['get', 'post']
    