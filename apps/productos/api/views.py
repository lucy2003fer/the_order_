from rest_framework.viewsets import ModelViewSet
from apps.productos.models import Productos
from apps.productos.api.serializer import ProductosSerializer

class ProductosViewSet(ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer
    #permisos metodos
    #http_method_names = ['get', 'post']
    