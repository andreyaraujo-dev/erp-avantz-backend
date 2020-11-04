from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from users.authentication import SafeJWTAuthentication
from .models import Rotinas
from .serializers import RotinasSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def index(request):
    try:
        permissions = Rotinas.objects.filter(sit=1)
        permissions_serialized = RotinasSerializer(permissions, many=True)
        return Response({"permissions": permissions_serialized.data})
    except:
        raise exceptions.APIException
