from rest_framework.serializers import ModelSerializer
from apps.pedidos.models import Pedidos

class PedidosSerializer(ModelSerializer):
    class Meta:
        model = Pedidos
        fields = '__all__'