from rest_framework import viewsets
from .models import Telefones
from .serializers import TelefoneSerializers


class EmailViewSet(viewsets.ModelViewSet):
    queryset = Telefones.objects.all()
    serializer_class = TelefoneSerializers
