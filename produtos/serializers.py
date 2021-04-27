from rest_framework.serializers import ModelSerializer
from .models import Produtos


class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produtos
        fields = '__all__'
