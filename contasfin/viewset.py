from rest_framework import viewsets
from .models import ContasFin
from .serializers import ContasFinSerializers


class ContasFinViewSet(viewsets.ModelViewSet):
    queryset = ContasFin.objects.all()
    serializer_class = ContasFinSerializers
