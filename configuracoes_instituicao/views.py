from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.db import transaction
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from users.authentication import SafeJWTAuthentication
from .serializers import ConfiguracoesInstituticaoSerializer
from .models import Configs
from instituicao.views import search_matriz


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def list_all(request):
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)

    try:
        configuracoes = Configs.objects.get(pk=id_institution)
        configuracoes_serialized = ConfiguracoesInstituticaoSerializer(
            configuracoes)

        return Response(configuracoes_serialized.data)
    except:
        raise exceptions.APIException(
            'Não foi possível carregar as configurações.')
