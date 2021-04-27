from rest_framework.viewsets import ModelViewSet
from .serializers import ProdutoSerializer
from .models import Produtos


class ProdutosViewSet(ModelViewSet):
    queryset = Produtos.objects.all()
    serializer_class = ProdutoSerializer
