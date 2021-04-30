from rest_framework.viewsets import ModelViewSet
from .serializers import UnidadeProdutoSerializer
from .models import Unidades


class UnidadeProdutoViewSet(ModelViewSet):
    queryset = Unidades.objects.all()
    serializer_class = UnidadeProdutoSerializer
