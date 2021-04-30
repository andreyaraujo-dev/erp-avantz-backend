from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.db import transaction
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from users.authentication import SafeJWTAuthentication
from .serializers import DetalhesProdutoSerializer
from .models import ProdItens


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def get_data_for_quick_search(request):
    pass
