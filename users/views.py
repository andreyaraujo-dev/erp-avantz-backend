from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status
from rest_framework import generics
from .serializers import UsersSerializers, ChangePasswordSerializer
from .utils import generate_access_token, generate_refresh_token
from .authentication import SafeJWTAuthentication
from instituicao.models import Instit


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def profile(request):
    user = request.user
    serialized_user = UsersSerializers(user).data
    return Response({'user': serialized_user})


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    User = get_user_model()
    username = request.data.get('username')
    password = request.data.get('password')
    response = Response()
    # checks if the username and password have been sent
    if (username is None) or (password is None):
        raise exceptions.AuthenticationFailed(
            'username and password required')
    user = User.objects.filter(username=username).first()
    # check if the user was found
    if(user is None):
        raise exceptions.AuthenticationFailed('user not found')

    # check if the password has been correct
    if user.senha:
        if password != user.password:
            raise exceptions.AuthenticationFailed('wrong password')
    else:
        match_check = check_password(password, user.password)
        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('wrong password')

    # check if the user has been active
    if user.ativo == 0:
        raise exceptions.AuthenticationFailed('disabled user')

    instituicao = Instit.objects.get(pk=user.instit_id)

    # check if the institution has ben active
    if instituicao.ativo == 0:
        raise exceptions.AuthenticationFailed('disabled institution')

    serialized_user = UsersSerializers(user).data

    access_token = generate_access_token(user)
    refresh_token = generate_refresh_token(user)

    response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)
    response.data = {
        'access_token': access_token,
        'user': serialized_user,
    }

    return response


@api_view(['POST'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def refresh_token_view(request):
    '''
    To obtain a new access_token this view expects 2 important things:
        1. a cookie that contains a valid refresh_token
        2. a header 'X-CSRFTOKEN' with a valid csrf token, client app can get it from cookies "csrftoken"
    '''
    User = get_user_model()
    refresh_token = request.COOKIES.get('refreshtoken')
    if refresh_token is None:
        raise exceptions.AuthenticationFailed(
            'Authentication credentials were not provided.')
    try:
        payload = jwt.decode(
            refresh_token, settings.REFRESH_TOKEN_SECRET, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise exceptions.AuthenticationFailed(
            'expired refresh token, please login again.')

    user = User.objects.filter(id=payload.get('user_id')).first()
    if user is None:
        raise exceptions.AuthenticationFailed('User not found')

    if not user.is_active:
        raise exceptions.AuthenticationFailed('user is inactive')
    # check if the user has been active
    if user.ativo == 0:
        raise exceptions.AuthenticationFailed('disabled user')
    instituicao = Instit.objects.get(pk=user.instit)
    # check if the institution has ben active
    if instituicao.ativo == 0:
        raise exceptions.AuthenticationFailed('disabled institution')

    access_token = generate_access_token(user)
    return Response({'access_token': access_token})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def register(request):
    User = get_user_model()
    username = request.data.get('username')
    password = request.data.get('password')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    email = request.data.get('email')
    id_pessoa = request.data.get('id_pessoa')
    id_instituicao = request.data.get('id_instituicao')
    id_grupo = request.data.get('id_grupo')
    ativo = request.data.get('ativo')
    acesso = request.data.get('acesso')
    response = Response()

    user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email,
                                    idpescod=id_pessoa, instit=id_instituicao, idgrp=id_grupo, ativo=ativo, acess=acesso)
    user.save()
    serialized_user = UsersSerializers(user).data
    return Response({'user': serialized_user})


@api_view(['POST', 'PUT'])
@ensure_csrf_cookie
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
def edit(request):
    User = get_user_model()
    first_name = request.data.get('firstName')
    last_name = request.data.get('lastName')
    email = request.data.get('email')
    id_user = request.data.get('userId')
    response = Response()

    try:
        user = User.objects.get(pk=id_user)

        print(user)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        return Response({'detail': 'Your data has been successfully changed'})
    except:
        raise exceptions.APIException


class ChangePasswordView(generics.UpdateAPIView):
    User = get_user_model()
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SafeJWTAuthentication,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }
            # make sure the user stays logged in
            update_session_auth_hash(request, self.object)
            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
