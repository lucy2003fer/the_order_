from rest_framework.serializers import ModelSerializer
from apps.detalle.models import DetallePedidos

class DetalleSerializer(ModelSerializer):
    class Meta:
        model = DetallePedidos
        fields = '__all__'