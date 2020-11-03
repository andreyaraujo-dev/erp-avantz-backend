from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from users.authentication import SafeJWTAuthentication
from .models import UsersGrp
from .serializers import UserGroupsSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def index(request):
    id_instituicao = request.user.instit_id
    try:
        groups = UsersGrp.objects.filter(instit=id_instituicao)
        groups_serialized = UserGroupsSerializer(groups, many=True).data
        return Response({"groups": groups_serialized})
    except:
        raise exceptions.APIException
