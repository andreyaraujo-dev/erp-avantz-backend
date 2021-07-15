from rest_framework.response import Response
from rest_framework import exceptions
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.db import transaction

from .models import Funcio
from .serializers import FuncionarioSerializer
from users.authentication import SafeJWTAuthentication
# from users.utils import verify_permission


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def get_all(request, name=None):
    id_institution = request.user.instit_id

    # user_id = request.user.id

    # if not verify_permission(40, user_id):
    #     raise exceptions.PermissionDenied(
    #         'Você não tem permissões para realizar esta operação.')

    if name == None:
        try:
            employees = Funcio.objects.filter(instit=id_institution, ativo=1)
            employees_serialized = FuncionarioSerializer(employees, many=True)

            return Response(employees_serialized.data)
        except:
            raise exceptions.APIException(
                'Não foi possível retornar os dados dos funcionários')
    else:
        try:
            employees = Funcio.objects.filter(
                nome__contains=name, instit=id_institution, ativo=1)
            employees_serialized = FuncionarioSerializer(employees, many=True)

            return Response(employees_serialized.data)
        except:
            raise exceptions.APIException(
                'Não foi possível retornar os dados dos funcionários')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
@transaction.atomic
def create(request):
    id_institution = request.user.instit_id

    # user_id = request.user.id

    # if not verify_permission(40, user_id):
    #     raise exceptions.PermissionDenied(
    #         'Você não tem permissões para realizar esta operação.')

    idpescod = request.data.get('idpescod')
    iduser = request.data.get('iduser')
    nome = request.data.get('nome')
    sit = request.data.get('sit')
    dtadm = request.data.get('dtadm')
    salario = request.data.get('salario')
    comissao = request.data.get('comissao')
    gratif = request.data.get('gratif')
    adiant = request.data.get('adiant')
    inss = request.data.get('inss')
    obs = request.data.get('obs')

    try:
        funcionario = Funcio(
            instit=id_institution,
            idpescod=idpescod,
            iduser=iduser,
            nome=nome,
            sit=sit,
            dtadm=dtadm,
            salario=salario,
            comissao=comissao,
            gratif=gratif,
            adiant=adiant,
            inss=inss,
            obs=obs
        )

        funcionario.save()

        return Response({'detail': 'Cadastro feito com sucesso.'})
    except:
        raise exceptions.APIException(
            'Não foi possível cadastrar o funcionário. Verifique os dados inseridos.')


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
@transaction.atomic
def delete(request, id):
    id_institution = request.user.instit_id
    # user_id = request.user.id

    # if not verify_permission(40, user_id):
    #     raise exceptions.PermissionDenied(
    #         'Você não tem permissões para realizar esta operação.')

    try:
        funcionario = Funcio.objects.filter(id=id).first()

        if not funcionario:
            return Response({'detail': 'Registro não encontrado'})

        funcionario.ativo = 0
        funcionario.save()

        funcionarios = Funcio.objects.filter(instit=id_institution, ativo=1)
        funcionarios_serialized = FuncionarioSerializer(
            funcionarios, many=True)

        return Response(funcionarios_serialized.data)
    except:
        raise exceptions.APIException(
            'Não foi possível deletar o registro, tente novamente.', code=500)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def show(request, id):
    # user_id = request.user.id

    # if not verify_permission(40, user_id):
    #     raise exceptions.PermissionDenied(
    #         'Você não tem permissões para realizar esta operação.')

    try:
        funcionario = Funcio.objects.get(pk=id)
        if not funcionario:
            raise exceptions.NotFound('Registro não encontrado.')

        funcionario_serialized = FuncionarioSerializer(funcionario)

        return Response(funcionario_serialized.data)
    except:
        raise exceptions.APIException(
            'Não foi possível retornar os dados do registro.')


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
@transaction.atomic
def update(request, id):
    # user_id = request.user.id

    # if not verify_permission(40, user_id):
    #     raise exceptions.PermissionDenied(
    #         'Você não tem permissões para realizar esta operação.')

    try:
        funcionario = Funcio.objects.get(pk=id)
        if not funcionario:
            raise exceptions.NotFound('Registro não encontrado.')

        funcionario.idpescod = request.data.get('idpescod')
        funcionario.iduser = request.data.get('iduser')
        funcionario.nome = request.data.get('nome')
        funcionario.sit = request.data.get('sit')
        funcionario.dtadm = request.data.get('dtadm')
        funcionario.salario = request.data.get('salario')
        funcionario.comissao = request.data.get('comissao')
        funcionario.gratif = request.data.get('gratif')
        funcionario.adiant = request.data.get('adiant')
        funcionario.inss = request.data.get('inss')
        funcionario.obs = request.data.get('obs')

        funcionario.save()
    except:
        raise exceptions.APIException(
            'Não foi possível atualizar os dados do funcionário, tente novamente.')


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
@transaction.atomic
def change_situation(request, id):
    id_institution = request.user.instit_id

    # user_id = request.user.id

    # if not verify_permission(40, user_id):
    #     raise exceptions.PermissionDenied(
    #         'Você não tem permissões para realizar esta operação.')

    try:
        funcionario = Funcio.objects.get(pk=id)
        if not funcionario:
            raise exceptions.NotFound('Registro não encontrado.')

        if funcionario.sit == 1:
            funcionario.sit = 0
        else:
            funcionario.sit = 1

        funcionario.save()

        funcionarios = Funcio.objects.filter(instit=id_institution, ativo=1)
        funcionarios_serialized = FuncionarioSerializer(
            funcionarios, many=True)

        return Response(funcionarios_serialized.data)
    except:
        raise exceptions.APIException(
            'Não foi possível atualizar os dados do funcionário, tente novamente.')
