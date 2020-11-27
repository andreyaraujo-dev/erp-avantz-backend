from rest_framework import viewsets
from .models import Enderecos
from .serializers import EnderecosSerializers


class EnderecosViewSet(viewsets.ModelViewSet):
    queryset = Enderecos.objects.all()
    serializer_class = EnderecosSerializers
