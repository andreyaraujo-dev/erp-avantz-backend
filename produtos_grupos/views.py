from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.utils import timezone

from users.authentication import SafeJWTAuthentication
from users.utils import verify_permission
from instituicao.views import search_matriz
from .models import ProdGrp
from .serializers import GrupoProdutoSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def get_all(request):
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)
    # user_id = request.user.id

    # if not verify_permission(40, user_id):
    #     raise exceptions.PermissionDenied(
    #         'Você não tem permissões para realizar esta operação.')

    try:
        groups = ProdGrp.objects.filter(instit=id_matriz)
        groups_serialized = GrupoProdutoSerializer(groups, many=True)

        return Response(groups_serialized.data)
    except:
        raise exceptions.APIException(
            'Não foi possível retornar os dados dos grupos dos produtos.')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def create_group(request):
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)
    # user_id = request.user.id

    # if not verify_permission(40, user_id):
    #     raise exceptions.PermissionDenied(
    #         'Você não tem permissões para realizar esta operação.')

    try:
        group = ProdGrp(
            instit=id_matriz,
            niv=1,
            nv1=request.data.get('nv1'),
            data=timezone.now()
        )

        group.save()

        all_groups = ProdGrp.objects.filter(instit=id_matriz)
        all_groups_serialized = GrupoProdutoSerializer(all_groups, many=True)

        return Response(all_groups_serialized.data)
    except:
        raise exceptions.APIException(
            'Não foi possível criar o grupo, tente novamente.')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def create_subgroup_level1(request, id_group):
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)
    # user_id = request.user.id

    # if not verify_permission(40, user_id):
    #     raise exceptions.PermissionDenied(
    #         'Você não tem permissões para realizar esta operação.')

    try:
        group = ProdGrp.objects.filter(instit=id_matriz, id=id_group).first()
        subgroup = ProdGrp(
            instit=id_matriz,
            niv=2,
            nv1=group.nv1,
            nv2=request.data.get('nv2'),
            nv1id=group.id,
            data=timezone.now()
        )

        subgroup.save()

        all_groups = ProdGrp.objects.filter(instit=id_matriz)
        all_groups_serialized = GrupoProdutoSerializer(all_groups, many=True)

        return Response(all_groups_serialized.data)
    except:
        raise exceptions.APIException(
            'Não foi possível criar o subgrupo, tente novamente.')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def create_subgroup_level2(request, id_subgroup):
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)
    # user_id = request.user.id

    # if not verify_permission(40, user_id):
    #     raise exceptions.PermissionDenied(
    #         'Você não tem permissões para realizar esta operação.')

    try:
        subgroup = ProdGrp.objects.filter(
            instit=id_matriz, id=id_subgroup).first()
        subgroup_level2 = ProdGrp(
            instit=id_matriz,
            niv=3,
            nv1=subgroup.nv1,
            nv2=subgroup.nv2,
            nv1id=subgroup.nv1id,
            nv3=request.data.get('nv3'),
            nv2id=id_subgroup,
            data=timezone.now()
        )

        subgroup_level2.save()

        all_groups = ProdGrp.objects.filter(instit=id_matriz)
        all_groups_serialized = GrupoProdutoSerializer(all_groups, many=True)

        return Response(all_groups_serialized.data)
    except:
        raise exceptions.APIException(
            'Não foi possível criar o subgrupo, tente novamente.')


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def delete(request, id):
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)
    # user_id = request.user.id

    # if not verify_permission(40, user_id):
    #     raise exceptions.PermissionDenied(
    #         'Você não tem permissões para realizar esta operação.')

    try:
        group = ProdGrp.objects.filter(
            instit=id_matriz, id=id).first()

        group.delete()

        all_groups = ProdGrp.objects.filter(instit=id_matriz)
        all_groups_serialized = GrupoProdutoSerializer(all_groups, many=True)

        return Response(all_groups_serialized.data)
    except:
        raise exceptions.APIException(
            'Não foi possível deletar o grupo, tente novamente.')


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def update(request, id):
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)
    # user_id = request.user.id

    # if not verify_permission(40, user_id):
    #     raise exceptions.PermissionDenied(
    #         'Você não tem permissões para realizar esta operação.')

    try:
        group = ProdGrp.objects.filter(
            instit=id_matriz, id=id).first()

        group.nv1 = request.data.get('nv1')
        group.nv2 = request.data.get('nv2')
        group.nv3 = request.data.get('nv3')

        group.save()

        all_groups = ProdGrp.objects.filter(instit=id_matriz)
        all_groups_serialized = GrupoProdutoSerializer(all_groups, many=True)

        return Response(all_groups_serialized.data)
    except:
        raise exceptions.APIException(
            'Não foi possível atualizar o grupo, tente novamente.')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def details(request, id):
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)
    # user_id = request.user.id

    # if not verify_permission(40, user_id):
    #     raise exceptions.PermissionDenied(
    #         'Você não tem permissões para realizar esta operação.')

    try:
        group = ProdGrp.objects.filter(
            instit=id_matriz, id=id).first()

        group_serialized = GrupoProdutoSerializer(group)

        return Response(group_serialized.data)
    except:
        raise exceptions.APIException(
            'Não foi possível retornar os dados do grupo, tente novamente.')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def get_sections(request):
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)

    try:
        sections = []
        groups = ProdGrp.objects.filter(instit=id_matriz).order_by(
            'nv1').values('id', 'nv1').distinct()

        i = 0
        for g in groups:
            if len(sections) == 0:
                sections.append(dict(id=g['id'], nv1=g['nv1']))

            while sections[i]['nv1'] != g['nv1']:
                sections.append(dict(id=g['id'], nv1=g['nv1']))
                i += 1

        return Response(sections)
    except:
        raise exceptions.APIException(
            'Não foi possível retornar os dados de seções de produto.')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def get_groups(request):
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)

    try:
        groups = []
        data = ProdGrp.objects.filter(instit=id_matriz).order_by(
            'nv1').values('id', 'nv2').distinct()

        i = 0
        for g in data:
            if len(groups) == 0:
                groups.append(dict(id=g['id'], nv2=g['nv2']))

            while groups[i]['nv2'] != g['nv2']:
                groups.append(dict(id=g['id'], nv2=g['nv2']))
                i += 1

        return Response(groups)
    except:
        raise exceptions.APIException(
            'Não foi possível retornar os dados dos grupos do produto.')
