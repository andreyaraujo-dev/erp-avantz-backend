from rest_framework import viewsets
from .models import Pedidos
from .serializers import PedidosSerializers


class PedidosViewSet(viewsets.ModelViewSet):
    queryset = Pedidos.objects.all()
    serializer_class = PedidosSerializers
