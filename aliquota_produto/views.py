from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from users.authentication import SafeJWTAuthentication
from .serializers import AliquotaSerializer
from .models import Aliquotas
from instituicao.views import search_matriz


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def find_all(request):
    id_institution = request.user.instit_id
    id_matriz = search_matriz(id_institution)

    try:
        aliquots = Aliquotas.objects.filter(instit=id_matriz)
        aliquots_serializer = AliquotaSerializer(aliquots, many=True)

        return Response(aliquots_serializer.data)
    except:
        raise exceptions.APIException(
            'Não foi possível retornar as alíquotas dos produtos.')
