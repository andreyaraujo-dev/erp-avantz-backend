from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.db import transaction
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from users.authentication import SafeJWTAuthentication
from .serializers import UnidadeProdutoSerializer
from .models import Unidades
from instituicao.views import search_matriz
from users.utils import verify_permission


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def get_all(request):
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)
    user_id = request.user.id

    if not verify_permission(148, user_id):
        raise exceptions.PermissionDenied(
            'Você não tem permissões para realizar esta operação.')

    try:
        unidades = Unidades.objects.filter(ativo=1, instit=id_matriz)
        unidades_serialized = UnidadeProdutoSerializer(unidades, many=True)

        return Response(unidades_serialized.data)
    except:
        raise exceptions.NotFound(
            'Não foi possível pesquisar os dados de unidades.')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def create(request):
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)
    user_id = request.user.id

    if not verify_permission(151, user_id):
        raise exceptions.PermissionDenied(
            'Você não tem permissões para realizar esta operação.')

    try:
        unit = Unidades(
            instit=id_matriz,
            ativo=1,
            und=request.data.get('und'),
            descr=request.data.get('descr'),
            tipo=request.data.get('tipo')
        )

        unit.save()

        unidades = Unidades.objects.filter(ativo=1, instit=id_matriz)
        unidades_serialized = UnidadeProdutoSerializer(unidades, many=True)

        return Response(unidades_serialized.data)
    except:
        raise exceptions.APIException(
            'Não foi possível salvar os dados, tente novamente')


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def update(request, id):
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)
    user_id = request.user.id

    if not verify_permission(150, user_id):
        raise exceptions.PermissionDenied(
            'Você não tem permissões para realizar esta operação.')

    unit = Unidades.objects.filter(ativo=1, id=id, instit=id_matriz).first()
    if not unit:
        raise exceptions.NotFound('O registro não existe na base de dados.')

    try:
        unit.und = request.data.get('und')
        unit.descr = request.data.get('descr')
        unit.tipo = request.data.get('tipo')

        unit.save()

        unidades = Unidades.objects.filter(ativo=1, instit=id_matriz)
        unidades_serialized = UnidadeProdutoSerializer(unidades, many=True)

        return Response(unidades_serialized.data)
    except:
        raise exceptions.APIException(
            'Não foi possível atualizar os dados, tente novamente')


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def delete(request, id):
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)
    user_id = request.user.id

    if not verify_permission(149, user_id):
        raise exceptions.PermissionDenied(
            'Você não tem permissões para realizar esta operação.')

    unit = Unidades.objects.filter(ativo=1, id=id, instit=id_matriz).first()
    if not unit:
        raise exceptions.NotFound('O registro não existe na base de dados.')

    try:
        unit.ativo = 0

        unit.save()

        unidades = Unidades.objects.filter(ativo=1, instit=id_matriz)
        unidades_serialized = UnidadeProdutoSerializer(unidades, many=True)

        return Response(unidades_serialized.data)
    except:
        raise exceptions.APIException(
            'Não foi possível deletar o registro, tente novamente.')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def find_by_initials(request, initials):
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)
    # user_id = request.user.id

    # if not verify_permission(110, user_id):
    #     raise exceptions.PermissionDenied(
    #         'Você não tem permissões para realizar esta operação.')

    units = Unidades.objects.filter(
        ativo=1, und__contains=initials, instit=id_matriz)
    if not units:
        raise exceptions.NotFound('O registro não existe na base de dados.')

    units_serialized = UnidadeProdutoSerializer(units, many=True)
    return Response(units_serialized.data)
