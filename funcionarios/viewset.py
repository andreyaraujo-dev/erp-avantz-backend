from rest_framework.viewsets import ModelViewSet
from .serializers import FuncionarioSerializer
from .models import Funcio


class FuncionarioViewSet(ModelViewSet):
    queryset = Funcio.objects.all()
    serializer_class = FuncionarioSerializer
