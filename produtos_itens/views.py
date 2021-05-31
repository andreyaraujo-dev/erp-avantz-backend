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


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def update(request, id_product):
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)
    # user_id = request.user.id

    # if not verify_permission(40, user_id):
    #     raise exceptions.PermissionDenied(
    #         'Você não tem permissões para realizar esta operação.')

    try:
        item = ProdItens.objects.filter(
            id_instit=id_institution, id_matriz=id_matriz, id_produtos=id_product).first()

        item.bxest = request.data.get('bxest')
        item.est_minimo = request.data.get('est_minimo')
        item.est_fiscal = request.data.get('est_fiscal')
        item.est_frente = request.data.get('est_frente')
        item.est_dep1 = request.data.get('est_dep1')
        item.est_dep2 = request.data.get('est_dep2')
        item.est_dep3 = request.data.get('est_dep3')
        item.compra = request.data.get('compra')
        item.frete = request.data.get('frete')
        item.ipi = request.data.get('ipi')
        item.aliq = request.data.get('aliq')
        item.custo = request.data.get('custo')
        item.lucro = request.data.get('lucro')
        item.prvenda1 = request.data.get('prvenda1')
        item.prvenda2 = request.data.get('prvenda2')
        item.prvenda3 = request.data.get('prvenda3')
        item.locavel = request.data.get('locavel')
        item.prloc = request.data.get('prloc')
        item.vdatac = request.data.get('vdatac')
        item.qtdatac = request.data.get('qtdatac')
        item.pratac = request.data.get('pratac')
        item.loc_frente = request.data.get('loc_frente')
        item.loc_dep1 = request.data.get('loc_dep1')
        item.loc_dep2 = request.data.get('loc_dep2')
        item.loc_dep3 = request.data.get('loc_dep3')
        item.comissao_atv = request.data.get('comissao_atv')
        item.comissao_val = request.data.get('comissao_val')

        item.save()

        return Response({'detail': 'Dados de estoque atualizado com sucesso.'})
    except:
        raise exceptions.APIException(
            'Não foi possível atualizar os dados de estoque, tente novamente.')
