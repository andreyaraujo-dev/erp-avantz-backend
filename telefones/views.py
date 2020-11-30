from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status
from datetime import datetime

from users.authentication import SafeJWTAuthentication
from instituicao.models import Instit
from .models import Telefones
from .serializers import TelefoneSerializers


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def index(request, id_person):
    try:
        phones = Telefones.objects.filter(
            id_pessoa_cod_fk=id_person, situacao=1)
        phones_serialized = TelefoneSerializers(phones, many=True)
        return Response(phones_serialized.data)
    except:
        raise exceptions.APIException(
            'Não foi possivel pesquisar os contatos deste registro.')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def store(request):
    phones_array = request.data.get('phones')

    for phone in phones_array:
        try:
            phone_registered = Telefones(id_pessoa_cod_fk=phone['idPerson'],
                                         situacao=phone['phoneSituation'], tel=phone['phoneNumber'], data_criacao=datetime.now())
            phone_registered.save()
        except:
            raise exceptions.APIException(
                'Não foi possível salvar os dados de contato')

    return Response({'detail': 'Todos os dados de contato foram salvos'})


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def update(request):
    phones_array = request.data.get('phones')

    for phone in phones_array:
        try:
            person_phone = Telefones.objects.get(pk=phone['idPhone'])
            person_phone.tel = phone['phoneNumber']
            person_phone.save()
        except:
            raise exceptions.APIException(
                'Não foi possível atualizar o registor de contato')
    return Response({'detail': 'Todos os dados de contato foram atualizados'})


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def delete(request, id_phone):
    try:
        phone = Telefones.objects.get(pk=id_phone)
        phone.situacao = 0
        phone.save()
        return Response({'detail': 'Apagado com sucesso!'})
    except:
        raise exceptions.APIException('Não foi possível deletar o registro')
