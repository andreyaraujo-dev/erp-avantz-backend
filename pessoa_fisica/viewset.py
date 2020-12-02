from rest_framework import viewsets
from .models import Pesfis
from .serializers import PessoaFisicaSerializers


class PessoaFisicaViewSet(viewsets.ModelViewSet):
    queryset = Pesfis.objects.all()
    serializer_class = PessoaFisicaSerializers
