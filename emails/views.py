from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status

from users.authentication import SafeJWTAuthentication
from instituicao.models import Instit
from .models import Mails
from .serializers import EmailSerializers


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def index(request, id_person):
    try:
        mails = Mails.objects.filter(id_pessoa_cod_fk=id_person, situacao=1)
        mails_serialized = EmailSerializers(mails, many=True)
        return Response(mails_serialized.data)
    except:
        raise exceptions.APIException(
            'Não foi possivel pesquisar os e-mail deste registro.')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def store(request):
    mails_array = request.data.get('mails')

    for mail in mails_array:
        try:
            mail_registered = Mails(id_pessoa_cod_fk=mail['idPerson'],
                                    situacao=mail['situation'], email=mail['userMail'])
            mail_registered.save()
        except:
            raise exceptions.APIException(
                'Não foi possível salvar os dados de email')

    mails = Mails.objects.filter(
        id_pessoa_cod_fk=mails_array[0]['idPerson'], situacao=1)
    mails_serialized = EmailSerializers(mails, many=True)

    return Response(mails_serialized.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def update(request):
    mails_array = request.data.get('mails')

    for mail in mails_array:
        try:
            userMail = Mails.objects.get(pk=mail['idMail'])
            userMail.email = mail['userMail']
            userMail.save()
        except:
            raise exceptions.APIException(
                'Não foi possível atualizar o registor de email')
    return Response({'detail': 'Todos os dados de email foram atualizados'})


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def delete(request, id_mail):
    try:
        mail = Mails.objects.get(pk=id_mail)
        mail.situacao = 0
        mail.save()
        return Response({'detail': 'Apagado com sucesso!'})
    except:
        raise exceptions.APIException('Não foi possível deletar o registro')
