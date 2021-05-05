from rest_framework.response import Response
from rest_framework import exceptions
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt, csrf_protect
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status

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
def create(request):
    user_id = request.user.id

    if not check_superuser(user_id):
        raise exceptions.PermissionDenied(
            'Você não tem permissões para realizar esta operação.')

    id_pessoa_juridica = request.data.get('idLegalPerson')
    nome = request.data.get('name')
    razao_social = request.data.get('companyName')
    rua = request.data.get('street')
    numero = request.data.get('numberAddress')
    complemento = request.data.get('complement')
    bairro = request.data.get('neighborhood')
    cep = request.data.get('zipCode')
    cidade = request.data.get('city')
    uf = request.data.get('UF')
    cnpj = request.data.get('CNPJ')
    inscricao_estadual = request.data.get('stateRegistration')
    inscricao_municipal = request.data.get('municipalRegistration')
    email1 = request.data.get('mail1')
    email2 = request.data.get('mail2')
    telefone1 = request.data.get('phone1')
    telefone2 = request.data.get('phone2')
    telefone3 = request.data.get('phone3')
    slogan = request.data.get('slogan')
    modulos = request.data.get('modules')

    try:
        institution = Instit(
            idpjur=id_pessoa_juridica,
            ativo=1,
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
        institution = Instit.objects.filter(id_instituicao=id, ativo=1).first()
        institution_serialized = InstituicaoSerializer(institution)

        return Response(institution_serialized.data)
    except:
        raise exceptions.APIException(
            'Não foi possível retornar os dados da instituição!')


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def update(request, id):
    user_id = request.user.id

    if not check_superuser(user_id):
        raise exceptions.PermissionDenied(
            'Você não tem permissões para realizar esta operação.')

    try:
        institution = Instit.objects.filter(id_instituicao=id, ativo=1).first()

        institution.ativo = request.data.get('active')
        institution.nome = request.data.get('name')
        institution.razsoc = request.data.get('companyName')
        institution.end = request.data.get('street')
        institution.endnum = request.data.get('numberAddress')
        institution.endcompl = request.data.get('complement')
        institution.bairro = request.data.get('neighborhood')
        institution.cep = request.data.get('zipCode')
        institution.cidade = request.data.get('city')
        institution.uf = request.data.get('UF')
        institution.cnpj = request.data.get('CNPJ')
        institution.iest = request.data.get('stateRegistration')
        institution.imun = request.data.get('municipalRegistration')
        institution.mail1 = request.data.get('mail1')
        institution.mail2 = request.data.get('mail2')
        institution.tel1 = request.data.get('phone1')
        institution.tel2 = request.data.get('phone2')
        institution.tel3 = request.data.get('phone3')
        institution.slogan = request.data.get('slogan')
        institution.modulos = request.data.get('modules')

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

        return Response({'details': 'Instituição desativada com sucesso.'})
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
