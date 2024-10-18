from rest_framework.viewsets import ModelViewSet
from apps.pedidos.models import Pedidos
from apps.pedidos.api.serializer import PedidosSerializer

class PedidosViewSet(ModelViewSet):
    queryset = Pedidos.objects.all()
    serializer_class = PedidosSerializer
    #permisos metodos
    #http_method_names = ['get', 'post']