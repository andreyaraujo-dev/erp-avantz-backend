from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt, csrf_protect
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
from django.db import transaction


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def profile(request):
    User = get_user_model()
    user_id = request.user.id
    try:
        user = User.objects.get(pk=user_id)
        serialized_user = UsersSerializers(user)
        return Response({'user': serialized_user.data})
    except:
        raise exceptions.APIException('Não foi possível pesquisar seus dados.')


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
            'Usuário e senha são obrigatórios')
    user = User.objects.filter(username=username).first()
    # check if the user was found
    if(user is None):
        raise exceptions.AuthenticationFailed('Usuário não econtrado')

    # check if the password has been correct
    if user.senha:
        if password != user.password:
            raise exceptions.AuthenticationFailed('Senha incorreta')
    else:
        match_check = check_password(password, user.password)
        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('Senha incorreta')

    # check if the user has been active
    if user.ativo == 0:
        raise exceptions.AuthenticationFailed('Este usuário está desativado')

    # check if the user has been deleted
    if user.is_deleted == 1:
        raise exceptions.AuthenticationFailed('Este usuário está desativado')

    instituicao = Instit.objects.get(pk=user.instit_id)

    # check if the institution has ben active
    if instituicao.ativo == 0:
        raise exceptions.AuthenticationFailed(
            'A instituição desse usuário está desativada')

    serialized_user = UsersSerializers(user).data

    access_token = generate_access_token(user)
    refresh_token = generate_refresh_token(user)

    response.set_cookie(key='refreshtoken',
                        value=refresh_token, path='/', max_age=3600, samesite='None', secure=True, httponly=True)
    # response.set_cookie(key='csrftoken', value=access_token, path='/', max_age=3600,
    #                     samesite='None', secure=True, httponly=True)
    response.data = {
        'access_token': access_token,
        'user': serialized_user,
        'institution': instituicao.nome
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
            'As credenciais de autenticação não foram fornecidas.')
    try:
        payload = jwt.decode(
            refresh_token, settings.REFRESH_TOKEN_SECRET, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise exceptions.AuthenticationFailed(
            'Token de atualização expirado, faça login novamente.')

    user = User.objects.filter(id=payload.get('user_id')).first()
    if user is None:
        raise exceptions.AuthenticationFailed('Usuário não encontrado')

    if not user.is_active:
        raise exceptions.AuthenticationFailed('Este usuário está desativado')
    # check if the user has been active
    if user.ativo == 0:
        raise exceptions.AuthenticationFailed('Este usuário está desativado')
    instituicao = Instit.objects.get(pk=user.instit)
    # check if the institution has ben active
    if instituicao.ativo == 0:
        raise exceptions.AuthenticationFailed(
            'A instituição deste usuário está desativada')

    access_token = generate_access_token(user)
    return Response({'access_token': access_token})


@api_view(['POST'])
@csrf_exempt
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@transaction.atomic
def register(request):
    User = get_user_model()
    username = request.data.get('username')
    password = request.data.get('password')
    first_name = request.data.get('firstName')
    last_name = request.data.get('lastName')
    email = request.data.get('email')
    person_id = request.data.get('idPerson')
    institution_id = request.data.get('idInstitution')
    group_id = request.data.get('idGroup')
    active = request.data.get('active')
    access = request.data.get('access')
    response = Response()

    try:
        user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email,
                                        idpescod=person_id, instit=institution_id, idgrp=group_id, ativo=active, acess=access)
        user.save()
        serialized_user = UsersSerializers(user)
        return Response({'user': serialized_user.data})
    except:
        raise exceptions.APIException('Não foi possível cadastrar o usuário')


@api_view(['POST', 'PUT'])
@csrf_exempt
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@transaction.atomic
def edit(request):
    User = get_user_model()
    first_name = request.data.get('firstName')
    last_name = request.data.get('lastName')
    email = request.data.get('email')
    id_user = request.user.id

    try:
        user = User.objects.get(pk=id_user)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        user_serialized = UsersSerializers(user)
        return Response({'detail': 'Seus dados foram atualizados com sucesso!', 'user': user_serialized.data})
    except:
        raise exceptions.APIException


@api_view(['GET'])
@ensure_csrf_cookie
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@transaction.atomic
def list_all(request, userName=None):
    User = get_user_model()
    id_instit = request.user.instit_id
    if userName == None:
        try:
            users = User.objects.filter(instit_id=id_instit, is_deleted=0)
            users_serialized = UsersSerializers(users, many=True).data

            return Response({'users': users_serialized})
        except:
            raise exceptions.APIException
    else:
        try:
            users = User.objects.filter(
                instit_id=id_instit, first_name__contains=userName, is_deleted=0)
            users_serialized = UsersSerializers(users, many=True).data

            return Response({'users': users_serialized})
        except:
            raise exceptions.APIException


@api_view(['PUT'])
@csrf_exempt
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@transaction.atomic
def admin_edit(request, id):
    """ 
    FUNCTION FOR THE ADMINISTRATOR TO EDIT THE USER DATA OF THEIR RESPECTIVE INSTITUTION
    """
    User = get_user_model()
    username = request.data.get('username')
    first_name = request.data.get('firstName')
    last_name = request.data.get('lastName')
    email = request.data.get('email')
    acess = request.data.get('access')
    idgrp_id = request.data.get('idGroupUser')
    idpescod_id = request.data.get('idPerson')

    try:
        user = User.objects.get(pk=id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        user.idgrp_id = idgrp_id
        user.idpescod_id = idpescod_id
        user.acess = acess
        user.save()

        user_serialized = UsersSerializers(user)
        return Response({'detail': 'Os dados foram alterados com sucesso!', 'user': user_serialized.data})
    except:
        raise exceptions.APIException


@api_view(['PUT'])
@ensure_csrf_cookie
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@transaction.atomic
def disabled_user(request, id):
    User = get_user_model()
    id_instit = request.user.instit_id
    # user_id = request.data.get('userId')

    user = User.objects.filter(
        id=id, ativo=1, is_active=1, is_deleted=0).first()
    if not user:
        return Response({'detail': 'Registro não encontrado, tente novamente.'}, status=status.HTTP_404_NOT_FOUND)

    try:
        user.ativo = 0
        user.is_active = 0
        user.save()

        users = User.objects.filter(instit_id=id_instit, is_deleted=0)
        users_serialized = UsersSerializers(users, many=True)

        return Response(users_serialized.data)
    except:
        return Response({'detail': exceptions.APIException})


@api_view(['PUT'])
@ensure_csrf_cookie
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@transaction.atomic
def delete(request, id):
    User = get_user_model()
    id_instit = request.user.instit_id
    # user_id = request.data.get('userId')

    user = User.objects.filter(
        id=id, is_deleted=0).first()
    if not user:
        return Response({'detail': 'Registro não encontrado, tente novamente.'}, status=status.HTTP_404_NOT_FOUND)

    try:
        user.is_deleted = 1
        user.save()

        users = User.objects.filter(instit_id=id_instit, is_deleted=0)
        users_serialized = UsersSerializers(users, many=True)

        return Response(users_serialized.data)
    except:
        return Response({'detail': exceptions.APIException})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def details(request, id):
    User = get_user_model()

    try:
        user = User.objects.get(pk=id)
        user_serialized = UsersSerializers(user).data
        return Response(user_serialized)
    except:
        # return Response({'detail': 'Não foi possível pesquisar os dados do usuário'})
        raise exceptions.APIException


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def upload_image(request):
    User = get_user_model()
    try:
        user_id = request.user.id
        user = User.objects.get(pk=user_id)
        user.foto = request.FILES['foto']
        user.save()

        user_updated = User.objects.get(pk=user_id)
        image_url = user_updated.foto.url
        return Response({"detail": "imagem enviada com sucesso", "imageURL": image_url}, status=status.HTTP_201_CREATED)
    except:
        return Response({"detail": exceptions.APIException}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def get_access(request):
    User = get_user_model()
    user_id = request.user.id

    try:
        access = User.objects.filter(id=user_id).values('acess').get()

        return Response(access)
    except:
        raise exceptions.APIException(
            'Não foi possível retornar as permissões do usuário.')


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
                return Response({"old_password": ["Senha incorreta."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'detail': 'Sua senha foi atualizada com sucesso!',
                'data': []
            }
            # make sure the user stays logged in
            update_session_auth_hash(request, self.object)
            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
