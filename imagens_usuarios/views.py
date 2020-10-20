from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from cloudinary.templatetags import cloudinary

from .serializers import ImagensUsuariosSerializer
from .models import ImagensUsuarios
from users.models import Users
from users.authentication import SafeJWTAuthentication


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def get_image_perfil(request):
    user_id = request.user.id
    imagens = ImagensUsuarios.objects.filter(user=user_id).last()

    try:
        serializer = ImagensUsuariosSerializer(imagens)
        return Response(data=serializer.data)
    except:
        return Response({'error': exceptions.APIException})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def upload_image(request):
    serializer = ImagensUsuariosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"detail": "imagem enviada com sucesso"}, status=status.HTTP_201_CREATED)
    else:
        return Response({"detail": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
