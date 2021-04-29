from rest_framework.viewsets import ModelViewSet
from .models import ProdItens
from .serializers import DetalhesProdutoSerializer


class DetalhesProdutoViewSet(ModelViewSet):
    queryset = ProdItens.objects.all()
    serializer_class = DetalhesProdutoSerializer
