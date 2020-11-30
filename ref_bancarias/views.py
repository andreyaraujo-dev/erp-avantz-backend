from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status
from datetime import datetime

from users.authentication import SafeJWTAuthentication
from instituicao.models import Instit
from .models import Refbanco
from .serializers import RefBancoSerializers


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def index(request, id_person):
    try:
        banking_references = Refbanco.objects.filter(
            id_pessoa_cod_fk=id_person, situacao=1)
        banking_references_serialized = RefBancoSerializers(
            banking_references, many=True)
        return Response(banking_references_serialized.data)
    except:
        raise exceptions.APIException(
            'Não foi possível pesquisar as referências bancárias deste registro.')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def store(request):
    references_array = request.data.get('bankingReferences')

    for reference in references_array:
        try:
            reference_registred = Refbanco(id_pessoa_cod_fk=reference['idPerson'], id_bancos_fk=reference['idBanking'], situacao=reference['situation'],
                                           agencia=reference['agency'], conta=reference['account'], abertura=reference['opening'], tipo=reference['type'], data_criacao=datetime.now())
            reference_registred.save()
        except:
            raise exceptions.APIException(
                'Não foi possível salvar os dados de refenrências bancárias')

    return Response({'detail': 'Todos os dados de referências foram salvos'})


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def update(request):
    references_array = request.data.get('bankingReferences')

    for reference in references_array:
        try:
            banking_reference = Refbanco.objects.get(
                pk=reference['idReference'])
            banking_reference.id_bancos_fk = reference['idBanking']
            banking_reference.agencia = reference['agency']
            banking_reference.conta = reference['account']
            banking_reference.abertura = reference['opening']
            banking_reference.tipo = reference['type']

            banking_reference.save()
        except:
            raise exceptions.APIException(
                'Não foi possível atualizar o registro de referência bancária')

    return Response({'detail': 'Todos os dados de referências bancárias foram atualizados'})


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def delete(request, id_reference):
    try:
        banking_reference = Refbanco.objects.get(pk=id_reference)
        banking_reference.situacao = 0
        banking_reference.save()
        return Response({'detail': 'Apagado com sucesso!'})
    except:
        raise exceptions.APIException('Não foi possível deletar o registro')
