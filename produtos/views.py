from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status
from datetime import datetime
from django.utils import timezone
from django.db import transaction
from django.db.models import Q

from users.authentication import SafeJWTAuthentication
from .models import Produtos
from .serializers import ProdutoSerializer
from .utils import generate_product_code
from instituicao.views import search_matriz
from users.utils import verify_permission

from produtos_itens.models import ProdItens


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def get_all(request):
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)
    user_id = request.user.id

    if not verify_permission(110, user_id):
        raise exceptions.PermissionDenied(
            'Você não tem permissões para realizar esta operação.')

    try:
        produtos = Produtos.objects.filter(
            id_matriz=id_matriz).order_by('descr').order_by('-ativo')
        produtos_serialized = ProdutoSerializer(produtos, many=True)
        return Response(produtos_serialized.data)
    except:
        raise exceptions.APIException(
            'Não foi possível pesquisar os produtos.')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def find_products(request, condition):
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)
    estoque = []

    try:
        produtos = Produtos.objects.filter(
            Q(id_matriz=id_matriz, descres__contains=condition) |
            Q(id_matriz=id_matriz, descr__contains=condition) |
            Q(id_matriz=id_matriz, codprod__contains=condition)
        )
        produtos_serialized = ProdutoSerializer(produtos, many=True)

        for produto in produtos_serialized.data:
            dados = ProdItens.objects.filter(id_instit=id_institution, ativo=2, id_produtos=produto['id']).values(
                'id', 'id_produtos', 'est_frente', 'prvenda1', 'prvenda2', 'prvenda3', 'locavel').get()
            estoque.append(dados)

        return Response({'produtos': produtos_serialized.data, 'estoque': estoque})
    except:
        raise exceptions.APIException(
            'Não foi possível encontrar os produtos.', status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def details(request, id):
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)
    user_id = request.user.id

    if not verify_permission(152, user_id):
        raise exceptions.PermissionDenied(
            'Você não tem permissões para realizar esta operação.')

    try:
        product = Produtos.objects.filter(id=id, id_matriz=id_matriz).first()
        product_serialized = ProdutoSerializer(product)
        return Response(product_serialized.data)
    except:
        raise exceptions.APIException(
            'Não foi possível retornar os dados do produto.')


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
@transaction.atomic
def deactivate(request, id):
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)
    user_id = request.user.id

    if not verify_permission(143, user_id):
        raise exceptions.PermissionDenied(
            'Você não tem permissões para realizar esta operação.')

    product = Produtos.objects.filter(id=id, id_matriz=id_matriz).first()
    product_item = ProdItens.objects.filter(
        id_produtos=product.id, id_matriz=id_matriz).first()

    if not product:
        raise exceptions.NotFound('Registro não encontrado, tente novamente.')

    try:
        product.ativo = 1
        product.save()

        product_item.ativo = 1
        product_item.save()

        produtos = Produtos.objects.filter(
            id_matriz=id_matriz).order_by('descr').order_by('-ativo')
        produtos_serialized = ProdutoSerializer(produtos, many=True)
        return Response(produtos_serialized.data)
    except:
        raise exceptions.APIException(
            'Não foi possível realizar a operação, tente novamente.')


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
@transaction.atomic
def activate(request, id):
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)
    user_id = request.user.id

    if not verify_permission(144, user_id):
        raise exceptions.PermissionDenied(
            'Você não tem permissões para realizar esta operação.')

    product = Produtos.objects.filter(id=id, id_matriz=id_matriz).first()
    product_item = ProdItens.objects.filter(
        id_produtos=product.id, id_matriz=id_matriz).first()

    if not product:
        raise exceptions.NotFound('Registro não encontrado, tente novamente.')

    try:
        product.ativo = 2
        product.save()

        product_item.ativo = 2
        product_item.save()

        return Response({'detail': 'O registro do produto foi ativado com sucesso.'})
    except:
        raise exceptions.APIException(
            'Não foi possível realizar a operação, tente novamente.')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
@transaction.atomic
def create(request):
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)
    product_code = generate_product_code(id_matriz)
    user_id = request.user.id

    if not verify_permission(5, user_id):
        raise exceptions.PermissionDenied(
            'Você não tem permissões para realizar esta operação.')

    try:
        product = Produtos(
            id_matriz=id_matriz,
            codprod=product_code,
            ativo=request.data.get('ativo'),
            descr=request.data.get('descr'),
            descres=request.data.get('descres'),
            und=request.data.get('und'),
            grupo=request.data.get('grupo'),
            tam=request.data.get('tam'),
            larg=request.data.get('larg'),
            alt=request.data.get('alt'),
            cubag=request.data.get('cubag'),
            peso=request.data.get('peso'),
            codbarra=request.data.get('codbarra'),
            fabr=request.data.get('fabr'),
            forn=request.data.get('forn'),
            caract=request.data.get('caract'),
            ncm=request.data.get('ncm'),
            cest=request.data.get('cest'),
            desnf=request.data.get('desnf'),
            foto=request.data.get('foto'),
            usuatz=user_id
        )

        product.save()
    except Exception:
        raise Exception
        # raise exceptions.APIException(
        #     'Não foi possível cadastrar o produto, tente novamente.')

    try:
        product_item = ProdItens(
            id_produtos=product.id,
            id_instit=id_institution,
            id_matriz=id_matriz,
            codprod=product_code,
            ativo=request.data.get('ativo'),
            bxest=request.data.get('bxest'),
            est_minimo=request.data.get('est_minimo'),
            est_fiscal=request.data.get('est_fiscal'),
            est_frente=request.data.get('est_frente'),
            est_dep1=request.data.get('est_dep1'),
            est_dep2=request.data.get('est_dep2'),
            est_dep3=request.data.get('est_dep3'),
            compra=request.data.get('compra'),
            frete=request.data.get('frete'),
            ipi=request.data.get('ipi'),
            aliq=request.data.get('aliq'),
            custo=request.data.get('custo'),
            lucro=request.data.get('lucro'),
            prvenda1=request.data.get('prvenda1'),
            prvenda2=request.data.get('prvenda2'),
            prvenda3=request.data.get('prvenda3'),
            locavel=request.data.get('locavel'),
            prloc=request.data.get('prloc'),
            vdatac=request.data.get('vdatac'),
            qtdatac=request.data.get('qtdatac'),
            pratac=request.data.get('pratac'),
            loc_frente=request.data.get('loc_frente'),
            loc_dep1=request.data.get('loc_dep1'),
            loc_dep2=request.data.get('loc_dep2'),
            loc_dep3=request.data.get('loc_dep3'),
            comissao_atv=request.data.get('comissao_atv'),
            comissao_val=request.data.get('comissao_val'),
            usuatz=user_id
        )

        product_item.save()
    except Exception:
        raise Exception
        # raise exceptions.APIException(
        #     'Não foi possível cadastrar os itens do produto, tente novamente.')

    return Response({'detail': 'Cadastro feito com sucesso.', 'product_id': product.id})


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
@transaction.atomic
def update(request, id):
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)
    user_id = request.user.id

    if not verify_permission(144, user_id):
        raise exceptions.PermissionDenied(
            'Você não tem permissões para realizar esta operação.')

    try:
        product = Produtos.objects.get(id=id, id_matriz=id_matriz)

        product.ativo = request.data.get('ativo')
        product.descr = request.data.get('descr')
        product.descres = request.data.get('descres')
        product.und = request.data.get('und')
        product.grupo = request.data.get('grupo')
        product.tam = request.data.get('tam')
        product.larg = request.data.get('larg')
        product.alt = request.data.get('alt')
        product.cubag = request.data.get('cubag')
        product.peso = request.data.get('peso')
        product.codbarra = request.data.get('codbarra')
        product.fabr = request.data.get('fabr')
        product.forn = request.data.get('forn')
        product.caract = request.data.get('caract')
        product.ncm = request.data.get('ncm')
        product.cest = request.data.get('cest')
        product.desnf = request.data.get('desnf')
        product.foto = request.data.get('foto')
        product.usuatz = user_id

        product.save()
    except:
        raise exceptions.APIException(
            'Não foi possível cadastrar o produto, tente novamente.')

    try:
        product_item = ProdItens.objects.get(
            id_produtos=id, id_matriz=id_matriz)

        product_item.ativo = request.data.get('ativo')
        product_item.bxest = request.data.get('bxest')
        product_item.est_minimo = request.data.get('est_minimo')
        product_item.est_fiscal = request.data.get('est_fiscal')
        product_item.est_frente = request.data.get('est_frente')
        product_item.est_dep1 = request.data.get('est_dep1')
        product_item.est_dep2 = request.data.get('est_dep2')
        product_item.est_dep3 = request.data.get('est_dep3')
        product_item.compra = request.data.get('compra')
        product_item.frete = request.data.get('frete')
        product_item.ipi = request.data.get('ipi')
        product_item.aliq = request.data.get('aliq')
        product_item.custo = request.data.get('custo')
        product_item.lucro = request.data.get('lucro')
        product_item.prvenda1 = request.data.get('prvenda1')
        product_item.prvenda2 = request.data.get('prvenda2')
        product_item.prvenda3 = request.data.get('prvenda3')
        product_item.locavel = request.data.get('locavel')
        product_item.prloc = request.data.get('prloc')
        product_item.vdatac = request.data.get('vdatac')
        product_item.qtdatac = request.data.get('qtdatac')
        product_item.pratac = request.data.get('pratac')
        product_item.loc_frente = request.data.get('loc_frente')
        product_item.loc_dep1 = request.data.get('loc_dep1')
        product_item.loc_dep2 = request.data.get('loc_dep2')
        product_item.loc_dep3 = request.data.get('loc_dep3')
        product_item.comissao_atv = request.data.get('comissao_atv')
        product_item.comissao_val = request.data.get('comissao_val')
        product_item.usuatz = user_id

        product_item.save()
    except:
        raise exceptions.APIException(
            'Não foi possível cadastrar os itens do produto, tente novamente.')

    return Response({'detail': 'Registro atualizado com sucesso.'})


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
@transaction.atomic
def delete(request, id):
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)
    user_id = request.user.id

    if not verify_permission(142, user_id):
        raise exceptions.PermissionDenied(
            'Você não tem permissões para realizar esta operação.')

    product = Produtos.objects.filter(id=id, id_matriz=id_matriz).first()
    if not product:
        raise exceptions.NotFound('Registro não encontrado, tente novamente.')

    product_item = ProdItens.objects.filter(
        id_produtos=product.id, id_matriz=id_matriz).first()

    try:
        product.delete()

        product_item.delete()

        produtos = Produtos.objects.filter(
            id_matriz=id_matriz).order_by('descr').order_by('-ativo')
        produtos_serialized = ProdutoSerializer(produtos, many=True)
        return Response(produtos_serialized.data)
    except:
        raise exceptions.APIException(
            'Não foi possível realizar a operação, tente novamente.')
