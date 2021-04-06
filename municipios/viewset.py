from rest_framework.viewsets import ModelViewSet
from .serializers import MunicipiosSerializer
from .models import Municipios


class MunicipiosViewSet(ModelViewSet):
    queryset = Municipios.objects.all()
    serializer_class = MunicipiosSerializer
