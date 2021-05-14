from rest_framework.viewsets import ModelViewSet
from .serializers import GrupoProdutoSerializer
from .models import ProdGrp


class GrupoProdutoViewSet(ModelViewSet):
    queryset = ProdGrp.objects.all()
    serializer_class = GrupoProdutoSerializer
