from rest_framework.viewsets import ModelViewSet
from .serializers import FotosSerializer
from .models import Fotos


class fotosViewSet(ModelViewSet):
    queryset = Fotos.objects.all()
    serializer_class = FotosSerializer
