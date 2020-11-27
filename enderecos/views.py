from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status
from users.authentication import SafeJWTAuthentication

from instituicao.models import Instit
from .models import Enderecos
from .serializers import EnderecosSerializers


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def index(request, id_person):
    try:
        adresses = Enderecos.objects.filter(
            id_pessoa_cod_fk=id_person, situacao=1)
        adresses_serialized = EnderecosSerializers(adresses, many=True)
        return Response(adresses_serialized.data)
    except:
        raise exceptions.APIException(
            'Não foi possível pesquisar os endereços deste registro')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def store(request):
    adresses_array = request.data.get('adresses')

    for adress in adresses_array:
        try:
            if adress['origin'] == 1:
                adress_registred = Enderecos(situacao=1, origem=1, id_pessoa_cod_fk=adress['idPerson'], endtip=1, rua=adress['street'], numero=adress['numberHouse'],
                                             complemento=adress['complement'], bairro=adress['neighborhood'], cep=adress['zipCode'], cidade=adress['city'], estado_endereco=adress['stateAdress'])
                adress_registred.save()
            elif adress['origin'] == 2:
                adress_registred = Enderecos(situacao=1, origem=2, id_pessoa_cod_fk=adress['idPerson'], endtip=1, rua=adress['street'], numero=adress['numberHouse'],
                                             complemento=adress['complement'], bairro=adress['neighborhood'], cep=adress['zipCode'], cidade=adress['city'], estado_endereco=adress['stateAdress'])
                adress_registred.save()
        except:
            raise exceptions.APIException(
                'Não foi possível salvar todos os dados de endereço')

    return Response({'detail': 'Todos os dados de endereço foram salvos'})


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def update(request, id_adress):
    try:
        adress = Enderecos.objects.get(pk=id_adress)
        adress.rua = request.data.get('street')
        adress.numero = request.data.get('numberHouse')
        adress.complemento = request.data.get('complement')
        adress.bairro = request.data.get('neighborhood')
        adress.cep = request.data.get('zipCode')
        adress.cidade = request.data.get('city')
        adress.estado_endereco = request.data.get('stateAdress')
        adress.save()

        return Response({'detail': 'Endereço atualizado com sucesso'})
    except:
        raise exceptions.APIException('Não foi possível atualizar o endereço')


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def delete(request, id_adress):
    try:
        adress = Enderecos.objects.get(pk=id_adress)
        adress.situacao = 0
        adress.save()

        return Response({'detail': 'Endereço deletado com sucesso'})
    except:
        raise exceptions.APIException('Não foi possível deletar o endereço')
