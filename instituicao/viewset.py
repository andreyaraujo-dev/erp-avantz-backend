from rest_framework.viewsets import ModelViewSet
from .serializers import InstituicaoSerializer
from .models import Instit


class InstituicaoViewSet(ModelViewSet):
    queryset = Instit.objects.all()
    serializer_class = InstituicaoSerializer
