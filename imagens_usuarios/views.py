from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from cloudinary.templatetags import cloudinary

from .serializers import ImagensUsuariosSerializer
from .models import ImagensUsuarios
from users.models import Users


class ImagemUsuarioCloud(APIView):
    parser_classes = (MultiPartParser, FormParser,)
    serializer_class = ImagensUsuariosSerializer

    def get(self, request, format=None):
        user_id = request.data.get('userId')
        user = Users.objects.get(pk=user_id)
        imagens = ImagensUsuarios.objects.filter(user_id=user)
        serializer = ImagensUsuariosSerializer(imagens, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "imagem enviada com sucesso"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
