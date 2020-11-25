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
    id_person = request.data.get('idPerson')
    situation = request.data.get('situation')
    mail = request.data.get('mailUser')

    mail_registered = Mails.objects.create(id_person, situation, mail)
    mail_serialized = EmailSerializers(mail_registered)
    return Response(mail_serialized.data)
