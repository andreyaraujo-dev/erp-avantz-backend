from rest_framework import viewsets
from .models import Refbanco
from .serializers import RefBancoSerializers


class RefBancoViewSet(viewsets.ModelViewSet):
    queryset = Refbanco.objects.all()
    serializer_class = RefBancoSerializers
