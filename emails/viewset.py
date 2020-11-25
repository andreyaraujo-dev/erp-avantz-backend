from rest_framework import viewsets
from .models import Mails
from .serializers import EmailSerializers


class EmailViewSet(viewsets.ModelViewSet):
    queryset = Mails.objects.all()
    serializer_class = EmailSerializers
