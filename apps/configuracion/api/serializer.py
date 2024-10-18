from rest_framework.serializers import ModelSerializer
from apps.configuracion.models import Configuracion

class ConfiguracionSerializer(ModelSerializer):
    class Meta:
        model = Configuracion
        fields = '__all__'