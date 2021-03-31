from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status

from users.authentication import SafeJWTAuthentication
from instituicao.models import Instit
from .models import Pesfis
from .serializers import PessoaFisicaSerializers


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([SafeJWTAuthentication])
# @ensure_csrf_cookie
# def index(request):
#     id_institution = request.user.instit_id
#     try:
#         physical_person = Pesfis.objects.filter()
