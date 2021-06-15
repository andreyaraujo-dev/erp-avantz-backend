from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.db import transaction
from django.utils import timezone
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


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
@transaction.atomic
def update(request):
    id_institution = request.user.instit_id

    try:
        configuracoes = Configs.objects.get(pk=id_institution)
        configuracoes.cfg1 = request.data.get('cfg1')
        configuracoes.cfg2 = request.data.get('cfg2')
        configuracoes.cfg3 = request.data.get('cfg3')
        configuracoes.cfg4 = request.data.get('cfg4')
        configuracoes.cfg5 = request.data.get('cfg5')
        configuracoes.cfg6 = request.data.get('cfg6')
        configuracoes.cfg7 = request.data.get('cfg7')
        configuracoes.cfg8 = request.data.get('cfg8')
        configuracoes.cfg9 = request.data.get('cfg9')
        configuracoes.cfg10 = request.data.get('cfg10')
        configuracoes.cfg11 = request.data.get('cfg11')
        configuracoes.cfg12 = request.data.get('cfg12')
        configuracoes.cfg13 = request.data.get('cfg13')
        configuracoes.cfg14 = request.data.get('cfg14')
        configuracoes.cfg15 = request.data.get('cfg15')
        configuracoes.cfg16 = request.data.get('cfg16')
        configuracoes.cfg17 = request.data.get('cfg17')
        configuracoes.cfg18 = request.data.get('cfg18')
        configuracoes.cfg19 = request.data.get('cfg19')
        configuracoes.cfg20 = request.data.get('cfg20')
        configuracoes.cfg21 = request.data.get('cfg21')
        configuracoes.cfg22 = request.data.get('cfg22')
        configuracoes.cfg23 = request.data.get('cfg23')
        configuracoes.cfg24 = request.data.get('cfg24')
        configuracoes.cfg25 = request.data.get('cfg25')
        configuracoes.cfg26 = request.data.get('cfg26')
        configuracoes.cfg27 = request.data.get('cfg27')
        configuracoes.cfg28 = request.data.get('cfg28')
        configuracoes.cfg29 = request.data.get('cfg29')
        configuracoes.cfg30 = request.data.get('cfg30')
        configuracoes.cfg31 = request.data.get('cfg31')
        configuracoes.cfg32 = request.data.get('cfg32')
        configuracoes.data_atualizacao = timezone.now()

        configuracoes.save()

        return Response({'detail': 'Configurações atualizadas com sucesso.'}, status=200)
    except:
        raise exceptions.APIException(
            'Não foi possível carregar as configurações.')
