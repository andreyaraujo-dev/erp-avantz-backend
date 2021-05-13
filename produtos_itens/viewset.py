from rest_framework.viewsets import ModelViewSet
from .serializers import ProdutosItensSerializer
from .models import ProdItens


class ProdutosViewSet(ModelViewSet):
    queryset = ProdItens.objects.all()
    serializer_class = ProdutosItensSerializer
