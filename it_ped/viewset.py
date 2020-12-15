from rest_framework import viewsets
from .models import It_Ped
from .serializers import ItPedSerializers


class ItPedViewSet(viewsets.ModelViewSet):
    queryset = It_Ped.objects.all()
    serializer_class = ItPedSerializers
