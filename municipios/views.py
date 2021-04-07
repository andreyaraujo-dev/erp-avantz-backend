from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status
from datetime import datetime
from django.utils import timezone
from django.db import transaction
from django.db.models import Count

from users.authentication import SafeJWTAuthentication

from .models import Municipios
from .serializers import MunicipiosSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def index(request):
    try:
        counties = Municipios.objects.all()
        counties_serialized = MunicipiosSerializer(counties, many=True)
        return Response(counties_serialized.data)
    except:
        raise exceptions.APIException(
            'Não foi possível pesquisar os municípios', code=400)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def select_ufs(request):
    try:
        counties = Municipios.objects.order_by(
            'uf_sigla').values('uf_sigla').distinct()
        # counties_serialized = MunicipiosSerializer(counties, many=True)

        return Response(counties)
    except:
        raise exceptions.APIException(
            'Não foi possível pesquisar os municípios', code=400)
