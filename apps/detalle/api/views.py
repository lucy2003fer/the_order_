from rest_framework.viewsets import ModelViewSet
from apps.detalle.models import DetallePedidos
from apps.detalle.api.serializer import DetalleSerializer

class DetalleViewSet(ModelViewSet):
    queryset = DetallePedidos.objects.all()
    serializer_class = DetalleSerializer
    #permisos metodos
    #http_method_names = ['get', 'post']