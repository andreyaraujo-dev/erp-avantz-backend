from rest_framework.serializers import ModelSerializer
from .models import ProdItens


class ProdutosItensSerializer(ModelSerializer):
    class Meta:
        model = ProdItens
        fields = '__all__'
