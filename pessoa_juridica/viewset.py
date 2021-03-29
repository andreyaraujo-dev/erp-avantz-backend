from rest_framework.viewsets import ModelViewSet
from .serializers import PessoaJuridicaSerializer
from .models import Pesjur


class PessoaJuridicaViewSet(ModelViewSet):
    queryset = Pesjur.objects.all()
    serializer_class = PessoaJuridicaSerializer
