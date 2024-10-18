from rest_framework.viewsets import ModelViewSet
from apps.configuracion.models import Configuracion
from apps.configuracion.api.serializer import ConfiguracionSerializer

class ConfiguracionViewSet(ModelViewSet):
    queryset = Configuracion.objects.all()
    serializer_class = ConfiguracionSerializer
    #permisos metodos
    #http_method_names = ['get', 'post']