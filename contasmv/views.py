from django.contrib.auth import get_user_model
#from django.views.decorators.csrf import csrf_protect
#from django.contrib.auth.hashers import check_password
#from django.contrib.auth import update_session_auth_hash
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from users.authentication import SafeJWTAuthentication
from .models import ContasMv
from contasfin.models import ContasFin
from .serializers import ContasMvSerializers
from .forms import CtFinForm

def filter_list(request):
   context = {}
   ctfin = ContasFin.objects.all()
   context['ctfin'] = ctfin
   return render(request, 'filter_list.html', context)

def filter_dropdown(request):
   context = {}
   context['form'] = CtFinForm
   return render(request, 'filter_dropdown.html', context)

@api_view(['GET'])
#@ensure_csrf_cookie
#@permission_classes([AllowAny])
#@permission_classes([IsAuthenticated])
#@authentication_classes([SafeJWTAuthentication])
def list_all(request):
#   User = get_user_model()
#   id_instit = request.user.instit_id
   try:
      acc_registers = ContasMv.objects.filter(instit_id=14)
      acc_registers_serialized = ContasMvSerializers(acc_registers, many=True).data

      return Response({'acc_registers': acc_registers_serialized})
   except:
      raise exceptions.APIException

