from rest_framework import serializers
from apps.factura.models import Factura

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ['id', 'pedido', 'total']

    def to_representation(self, instance):
        #étodo to_json para personalizar la salida de los datos 
        return instance.to_json()
