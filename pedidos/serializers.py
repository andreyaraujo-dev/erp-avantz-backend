from rest_framework import serializers
from .models import Pedidos


class PedidosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pedidos
        fields = '__all__'