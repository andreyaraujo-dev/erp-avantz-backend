from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from users.authentication import SafeJWTAuthentication
from .models import UsersGrp
from .serializers import UserGroupsSerializer
import datetime


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def index(request):
    id_instituicao = request.user.instit_id
    try:
        groups = UsersGrp.objects.filter(instit=id_instituicao)
        groups_serialized = UserGroupsSerializer(groups, many=True).data
        return Response(groups_serialized)
    except:
        raise exceptions.APIException


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def details(request, id):
    try:
        group = UsersGrp.objects.get(pk=id)
        group_serializer = UserGroupsSerializer(group)
        return Response(group_serializer.data)
    except:
        raise exceptions.ErrorDetail


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def edit(request, id):
    name = request.data.get('nameGroup')
    access = request.data.get('accessGroup')

    try:
        group = UsersGrp.objects.get(pk=id)
        group.grupo = name
        group.acess = access

        group.save()
        return Response({'detail': 'Dados do grupo atualizados com sucesso!'})
    except:
        raise exceptions.APIException


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def delete(request, id):
    try:
        group = UsersGrp.objects.get(pk=id)
        group.delete()

        return Response({'detail': 'Grupo deletado com sucesso!'})
    except:
        raise exceptions.APIException


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def create(request):
    name = request.data.get('nameGroup')
    id_institution = request.user.instit_id
    access = request.data.get('access')
    # created_at = datetime.date.today()

    try:
        group = UsersGrp(grupo=name, instit=id_institution, acess=access)
        group.save()

        group_serialized = UserGroupsSerializer(group)
        return Response(group_serialized.data)
    except:
        raise exceptions.APIException
