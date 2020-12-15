from rest_framework import viewsets
from .models import ContasMv
from .serializers import ContasMvSerializers


class ContasMvViewSet(viewsets.ModelViewSet):
    #queryset = ContasMv.objects.all().order_by('dat')
    queryset = ContasMv.objects.all()
    serializer_class = ContasMvSerializers
