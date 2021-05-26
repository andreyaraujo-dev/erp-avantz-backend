from django.utils import timezone
from rest_framework.response import Response
from rest_framework import exceptions
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt, csrf_protect
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status
from django.db import transaction

from .models import Fotos
from .serializers import FotosSerializer
from users.utils import check_superuser
from users.authentication import SafeJWTAuthentication
from instituicao.models import Instit
from produtos.models import Produtos


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def upload(request, product_id):
    user_id = request.user.id
    id_institution = request.user.instit_id

    # if not check_superuser(user_id):
    #     raise exceptions.PermissionDenied(
    #         'Você não tem permissões para realizar esta operação.')

    produto = Produtos.objects.get(pk=product_id)
    instit = Instit.objects.get(pk=id_institution)

    try:
        files = request.FILES['files']
        photo = Fotos(
            id_instituicao=instit,
            id_produto=produto,
            nome_arquivo=files,
            data_criacao=timezone.now()
        )

        photo.save()

        return Response({'detail': 'Upload finalizado com sucesso.'})
    except:
        raise exceptions.APIException(
            'Não foi possível fazer upload das imagens')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def find_by_product_id(request, product_id):
    user_id = request.user.id
    id_institution = request.user.instit_id

    # if not check_superuser(user_id):
    #     raise exceptions.PermissionDenied(
    #         'Você não tem permissões para realizar esta operação.')

    produto = Produtos.objects.get(pk=product_id)
    instit = Instit.objects.get(pk=id_institution)

    try:
        photos = Fotos.objects.filter(
            id_instituicao=instit, id_produto=produto)
        photos_serialized = FotosSerializer(photos, many=True)

        return Response(photos_serialized.data)
    except:
        raise exceptions.APIException('Não foi possível encontrar as imagens')
