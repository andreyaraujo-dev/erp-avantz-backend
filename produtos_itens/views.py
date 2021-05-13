from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status
from datetime import datetime
from django.utils import timezone
from django.db import transaction

from users.authentication import SafeJWTAuthentication
from .models import ProdItens
from .serializers import ProdutosItensSerializer
from users.utils import verify_permission
from instituicao.views import search_matriz


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def find_by_product_id(request, id):
    user_id = request.user.id
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)

    if not verify_permission(40, user_id):
        raise exceptions.PermissionDenied(
            'Você não tem permissões para realizar esta operação.')

    try:
        item = ProdItens.objects.filter(
            id_produtos=id, id_matriz=id_matriz).first()
        item_serialized = ProdutosItensSerializer(item)

        return Response(item_serialized.data)
    except:
        raise exceptions.NotFound(
            'Não foi possível retornar os dados para este ID.')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def find_by_matriz(request):
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)
    user_id = request.user.id

    if not verify_permission(40, user_id):
        raise exceptions.PermissionDenied(
            'Você não tem permissões para realizar esta operação.')

    try:
        itens = ProdItens.objects.filter(id_instit=id_matriz)
        itens_serialized = ProdutosItensSerializer(itens, many=True)

        return Response(itens_serialized.data)
    except:
        raise exceptions.APIException(
            'Não foi possível retornar os dados requisitados.')
