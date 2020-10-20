from rest_framework import viewsets
from .models import ImagensUsuarios
from .serializers import ImagensUsuariosSerializer


class ImagemUsuarioViewSet(viewsets.ModelViewSet):
    queryset = ImagensUsuarios.objects.all()
    serializer_class = ImagensUsuariosSerializer
