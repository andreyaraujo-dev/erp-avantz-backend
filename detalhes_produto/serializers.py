from rest_framework.serializers import ModelSerializer
from .models import ProdItens


class DetalhesProdutoSerializer(ModelSerializer):
    class Meta:
        model = ProdItens
        fields = '__all__'
