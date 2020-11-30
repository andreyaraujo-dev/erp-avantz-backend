from rest_framework import viewsets
from .models import Referencias
from .serializers import ReferenciasSerializers


class EmailViewSet(viewsets.ModelViewSet):
    queryset = Referencias.objects.all()
    serializer_class = ReferenciasSerializers
