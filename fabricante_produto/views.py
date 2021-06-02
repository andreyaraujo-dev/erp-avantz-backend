from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from users.authentication import SafeJWTAuthentication
from .models import Fabpro
from .serializers import FabricanteProdutoSerializer
from instituicao.views import search_matriz
from users.utils import verify_permission


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def get_all(request):
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)
    id_user = request.user.id

    if not verify_permission(139, id_user):
        raise exceptions.PermissionDenied(
            'Você não tem permissões para realizar esta operação.')

    try:
        fabricantes = Fabpro.objects.filter(instit=id_matriz)
        fabricantes_serialized = FabricanteProdutoSerializer(
            fabricantes, many=True)

        return Response(fabricantes_serialized.data)
    except:
        raise exceptions.NotFound('Não foi possível pesquisar os fabricantes.')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def create(request):
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)
    id_user = request.user.id

    if not verify_permission(111, id_user):
        raise exceptions.PermissionDenied(
            'Você não tem permissões para realizar esta operação.')

    try:
        fabricante = Fabpro(
            instit=id_matriz,
            marca=request.data.get('marca'),
            fabr=request.data.get('fabr'),
            data_criacao=timezone.now()
        )

        fabricante.save()

        fabricantes = Fabpro.objects.filter(instit=id_matriz)
        fabricantes_serialized = FabricanteProdutoSerializer(
            fabricantes, many=True)

        return Response(fabricantes_serialized.data)
    except:
        raise exceptions.APIException(
            'Não foi possível cadastrar o fabricante, tente novamente')


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def delete(request, id):
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)
    id_user = request.user.id

    if not verify_permission(140, id_user):
        raise exceptions.PermissionDenied(
            'Você não tem permissões para realizar esta operação.')

    try:
        fabricante = Fabpro.objects.filter(instit=id_matriz, id=id)
        fabricante.delete()

        fabricantes = Fabpro.objects.filter(instit=id_matriz)
        fabricantes_serialized = FabricanteProdutoSerializer(
            fabricantes, many=True)

        return Response(fabricantes_serialized.data)
    except:
        raise exceptions.APIException(
            'Não foi possível remover o registro de fabricante, tente novamente.')


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def update(request, id):
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)
    id_user = request.user.id

    if not verify_permission(141, id_user):
        raise exceptions.PermissionDenied(
            'Você não tem permissões para realizar esta operação.')

    try:
        fabricante = Fabpro.objects.filter(instit=id_matriz, id=id).first()
        fabricante.marca = request.data.get('marca')
        fabricante.fabr = request.data.get('fabr')

        fabricante.save()

        fabricantes = Fabpro.objects.filter(instit=id_matriz)
        fabricantes_serialized = FabricanteProdutoSerializer(
            fabricantes, many=True)

        return Response(fabricantes_serialized.data)
    except:
        raise exceptions.APIException(
            'Não foi possível atualizar o registro de fabricante, tente novamente.')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def find_by_id(request, id):
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)
    # id_user = request.user.id

    # if not verify_permission(110, user_id):
    #     raise exceptions.PermissionDenied(
    #         'Você não tem permissões para realizar esta operação.')

    fabricante = Fabpro.objects.filter(instit=id_matriz, id=id).first()

    if not fabricante:
        raise exceptions.NotFound(
            'Nenhum fabricante foi encontrado com este ID')

    fabricante_serialized = FabricanteProdutoSerializer(fabricante)

    return Response(fabricante_serialized.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def find_by_brand(request, brand):
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)
    # id_user = request.user.id

    # if not verify_permission(110, user_id):
    #     raise exceptions.PermissionDenied(
    #         'Você não tem permissões para realizar esta operação.')

    fabricante = Fabpro.objects.filter(
        instit=id_matriz, marca__contains=brand)

    if not fabricante:
        raise exceptions.NotFound(
            'Nenhum fabricante foi encontrado com esta marca')

    fabricante_serialized = FabricanteProdutoSerializer(fabricante, many=True)

    return Response(fabricante_serialized.data)
