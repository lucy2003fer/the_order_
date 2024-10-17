from rest_framework.serializers import ModelSerializer
from apps.productos.models import Productos

class ProductosSerializer(ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'
