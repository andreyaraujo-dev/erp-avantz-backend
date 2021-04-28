from rest_framework.viewsets import ModelViewSet
from .serializers import FabricanteProdutoSerializer
from .models import Fabpro


class FabricanteProdutoViewSet(ModelViewSet):
    queryset = Fabpro.objects.all()
    serializer_class = FabricanteProdutoSerializer
