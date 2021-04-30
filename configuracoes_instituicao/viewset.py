from rest_framework.viewsets import ModelViewSet
from .serializers import ConfiguracoesInstituticaoSerializer
from .models import Configs


class ConfiguracoesInstituticaoViewSet(ModelViewSet):
    queryset = Configs.objects.all()
    serializer_class = ConfiguracoesInstituticaoSerializer
