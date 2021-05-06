from rest_framework.response import Response
from rest_framework import exceptions
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt, csrf_protect
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status
from django.db import transaction

from .models import Instit
from .serializers import InstituicaoSerializer
from users.utils import check_superuser
from users.authentication import SafeJWTAuthentication


def search_matriz(id):
    try:
        instituicao = Instit.objects.get(pk=id)
        instituicao_serialized = InstituicaoSerializer(instituicao).data

        matriz = Instit.objects.filter(
            id_instituicao=instituicao_serialized['idmatriz']).get()
        matriz_serialized = InstituicaoSerializer(matriz).data
        return matriz_serialized['idmatriz']
    except:
        raise exceptions.APIException('Não foi possível encontrar a matriz')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def get_all(request, name=None):
    user_id = request.user.id

    if not check_superuser(user_id):
        raise exceptions.PermissionDenied(
            'Você não tem permissões para realizar esta operação.')

    if name == None:
        try:
            institutions = Instit.objects.all()
            institutions_serialized = InstituicaoSerializer(
                institutions, many=True)

            return Response(institutions_serialized.data)
        except:
            raise exceptions.APIException(
                'Não foi possível retornar os dados das instituições.')
    else:
        try:
            institutions = Instit.objects.filter(nome__contains=name)
            institutions_serialized = InstituicaoSerializer(
                institutions, many=True)

            return Response(institutions_serialized.data)
        except:
            raise exceptions.APIException(
                'Não foi possível retornar os dados das instituições.')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
@transaction.atomic
def create(request):
    user_id = request.user.id
    print(f'id usuario', user_id)
    if not check_superuser(user_id):
        raise exceptions.PermissionDenied(
            'Você não tem permissões para realizar esta operação.')
    print('tem permissao')

    id_pessoa_juridica = request.data.get('idpjur')
    print(id_pessoa_juridica)
    ativo = request.data.get('ativo')
    print(ativo)
    nome = request.data.get('nome')
    print(nome)
    razao_social = request.data.get('razsoc')
    print(razao_social)
    rua = request.data.get('end')
    print(rua)
    numero = request.data.get('endnum')
    print(numero)
    complemento = request.data.get('endcompl')
    print(complemento)
    bairro = request.data.get('bairro')
    print(bairro)
    cep = request.data.get('cep')
    print(cep)
    cidade = request.data.get('cidade')
    print(cidade)
    uf = request.data.get('uf')
    print(uf)
    cnpj = request.data.get('cnpj')
    print(cnpj)
    inscricao_estadual = request.data.get('iest')
    print(inscricao_estadual)
    inscricao_municipal = request.data.get('imun')
    print(inscricao_municipal)
    email1 = request.data.get('mail1')
    print(email1)
    email2 = request.data.get('mail2')
    print(email2)
    telefone1 = request.data.get('tel1')
    print(telefone1)
    telefone2 = request.data.get('tel2')
    print(telefone2)
    telefone3 = request.data.get('tel3')
    print(telefone3)
    slogan = request.data.get('slogan')
    print(slogan)
    modulos = request.data.get('modulos')
    print(modulos)

    try:
        institution = Instit(
            idpjur=id_pessoa_juridica,
            ativo=ativo,
            nome=nome,
            razsoc=razao_social,
            end=rua,
            endnum=numero,
            endcompl=complemento,
            bairro=bairro,
            cep=cep,
            cidade=cidade,
            uf=uf,
            cnpj=cnpj,
            iest=inscricao_estadual,
            imun=inscricao_municipal,
            mail1=email1,
            mail2=email2,
            tel1=telefone1,
            tel2=telefone2,
            tel3=telefone3,
            slogan=slogan,
            modulos=modulos
        )

        institution.save()
        print(f'salvou 1', institution)

        if request.data.get('idmatriz') != 0:
            institution.idmatriz = request.data.get('idmatriz')
            print('matriz 0')
        else:
            institution.idmatriz = institution.id_instituicao
            print('matriz id instit')

        institution.save()
        print(f'salvou 2', institution)

        return Response({'detail': 'Cadastro feito com sucesso'})
    except:
        raise exceptions.APIException(
            'Não foi possível cadastrar a instituição. Tente novamente.')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def details(request, id):
    user_id = request.user.id

    if not check_superuser(user_id):
        raise exceptions.PermissionDenied(
            'Você não tem permissões para realizar esta operação.')

    try:
        institution = Instit.objects.filter(id_instituicao=id).first()
        institution_serialized = InstituicaoSerializer(institution)

        return Response(institution_serialized.data)
    except:
        raise exceptions.APIException(
            'Não foi possível retornar os dados da instituição!')


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
@transaction.atomic
def update(request, id):
    user_id = request.user.id

    if not check_superuser(user_id):
        raise exceptions.PermissionDenied(
            'Você não tem permissões para realizar esta operação.')

    try:
        institution = Instit.objects.filter(id_instituicao=id).first()

        institution.idmatriz = request.data.get('idmatriz')
        institution.ativo = request.data.get('ativo')
        institution.nome = request.data.get('nome')
        institution.razsoc = request.data.get('razsoc')
        institution.end = request.data.get('end')
        institution.endnum = request.data.get('endnum')
        institution.endcompl = request.data.get('endcompl')
        institution.bairro = request.data.get('bairro')
        institution.cep = request.data.get('cep')
        institution.cidade = request.data.get('cidade')
        institution.uf = request.data.get('uf')
        institution.cnpj = request.data.get('cnpj')
        institution.iest = request.data.get('iest')
        institution.imun = request.data.get('imun')
        institution.mail1 = request.data.get('mail1')
        institution.mail2 = request.data.get('mail2')
        institution.tel1 = request.data.get('tel1')
        institution.tel2 = request.data.get('tel2')
        institution.tel3 = request.data.get('tel3')
        institution.slogan = request.data.get('slogan')
        institution.modulos = request.data.get('modulos')

        institution.save()

        return Response({'detail': 'Dados atualizados com sucesso'})
    except:
        raise exceptions.APIException(
            'Não foi possível atualizar os dados. Tente novamente.')


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def deactivate(request, id):
    user_id = request.user.id

    if not check_superuser(user_id):
        raise exceptions.PermissionDenied(
            'Você não tem permissões para realizar esta operação.')

    try:
        institution = Instit.objects.filter(id_instituicao=id, ativo=1).first()
        institution.ativo = 0
        institution.save()

        institutions = Instit.objects.all()
        institutions_serialized = InstituicaoSerializer(
            institutions, many=True)

        return Response(institutions_serialized.data)
    except:
        raise exceptions.APIException(
            'Não foi possível desativar a instituição, tente novamente.')


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def activate(request, id):
    user_id = request.user.id

    if not check_superuser(user_id):
        raise exceptions.PermissionDenied(
            'Você não tem permissões para realizar esta operação.')

    try:
        institution = Instit.objects.filter(id_instituicao=id).first()

        institution.ativo = 1

        institution.save()

        return Response({'details': 'Instituição ativada com sucesso.'})
    except:
        raise exceptions.APIException(
            'Não foi possível ativar a instituição, tente novamente.')
