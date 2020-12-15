from django.contrib.auth import get_user_model
#from django.views.decorators.csrf import csrf_protect
#from django.contrib.auth.hashers import check_password
#from django.contrib.auth import update_session_auth_hash
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from users.authentication import SafeJWTAuthentication
from .models import ContasFin
from .serializers import ContasFinSerializers


@api_view(['GET'])
#@ensure_csrf_cookie
#@permission_classes([AllowAny])
#@permission_classes([IsAuthenticated])
#@authentication_classes([SafeJWTAuthentication])

def list_all(request):
#   User = get_user_model()
#   id_instit = request.user.instit_id
   try:
      acc_registers = ContasFin.objects.filter(instit_id=14)
      acc_registers_serialized = ContasFinSerializers(acc_registers, many=True).data

      return Response({'acc_registers': acc_registers_serialized})
   except:
      raise exceptions.APIException