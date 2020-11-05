from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from users.authentication import SafeJWTAuthentication
from .serializers import PescodSerializer
from .models import Pescod


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def index(request):
    id_institution = request.user.instit_id
    try:
        persons = Pescod.objects.filter(id_instituicao_fk=id_institution)
        persons_serialized = PescodSerializer(persons, many=True)
        return Response(persons_serialized.data)
    except:
        raise exceptions.APIException
