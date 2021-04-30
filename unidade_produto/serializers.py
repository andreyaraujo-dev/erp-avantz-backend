from rest_framework.serializers import ModelSerializer
from .models import Unidades


class UnidadeProdutoSerializer(ModelSerializer):
    class Meta:
        model = Unidades
        fields = ['id', 'instit', 'ativo', 'und', 'descr', 'tipo', ]
