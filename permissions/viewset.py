from rest_framework import viewsets
from rest_framework import pagination
from .models import Rotinas
from .serializers import RotinasSerializer
from django.core.paginator import Paginator


class RotinasViewSet(viewsets.ModelViewSet):
    queryset = Rotinas.objects.all().order_by('-id')
    serializer_class = RotinasSerializer
    # pagination_class = Paginator(queryset, 20)
