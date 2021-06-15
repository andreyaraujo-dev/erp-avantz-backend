import aliquota_produto
from rest_framework import viewsets
from .models import Aliquotas
from .serializers import AliquotaSerializer


class AliquotaViewSet(viewsets.ModelViewSet):
    queryset = Aliquotas.objects.all()
    serializer_class = AliquotaSerializer
