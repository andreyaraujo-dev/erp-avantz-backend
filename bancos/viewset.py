from rest_framework import viewsets
from .models import Bancos
from .serializers import BancoSerializers


class BancoViewSet(viewsets.ModelViewSet):
    queryset = Bancos.objects.all()
    serializer_class = BancoSerializers
