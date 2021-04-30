from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from users.authentication import SafeJWTAuthentication
from .models import Fabpro
from .serializers import FabricanteProdutoSerializer
from instituicao.views import search_matriz


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def get_all(request):
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)

    try:
        fabricantes = Fabpro.objects.filter(instit=id_matriz)
        fabricantes_serialized = FabricanteProdutoSerializer(
            fabricantes, many=True)

        return Response(fabricantes_serialized.data)
    except:
        raise exceptions.NotFound('Não foi possível pesquisar os fabricantes.')
