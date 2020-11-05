from rest_framework.viewsets import ModelViewSet
from .serializers import PescodSerializer
from .models import Pescod


class PescodViewSet(ModelViewSet):
    queryset = Pescod.objects.all()
    serializer_class = PescodSerializer
