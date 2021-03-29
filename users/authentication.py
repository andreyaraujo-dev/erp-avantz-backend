import jwt
from rest_framework.authentication import BaseAuthentication
from django.middleware.csrf import CsrfViewMiddleware
from rest_framework import exceptions
from django.conf import settings
from django.contrib.auth import get_user_model
from instituicao.models import Instit


class CSRFCheck(CsrfViewMiddleware):
    def _reject(self, request, reason):
        # Return the failure reason instead of an HttpResponse
        return reason


class SafeJWTAuthentication(BaseAuthentication):
    '''
        custom authentication class for DRF and JWT
        https://github.com/encode/django-rest-framework/blob/master/rest_framework/authentication.py
    '''

    def authenticate(self, request):
        User = get_user_model()
        authorization_heaader = request.headers.get('Authorization')

        if not authorization_heaader:
            return None
        try:
            # header = 'Token xxxxxxxxxxxxxxxxxxxxxxxx'
            access_token = authorization_heaader.split(' ')[1]
            payload = jwt.decode(
                access_token, settings.SECRET_KEY, algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed(
                'Token de acesso expirado, faça login novamente')
        except IndexError:
            raise exceptions.AuthenticationFailed('Prefixo do token ausente')

        user = User.objects.filter(id=payload['user_id']).first()
        if user is None:
            raise exceptions.AuthenticationFailed('Usuário não encontrado')

        if not user.is_active:
            raise exceptions.AuthenticationFailed(
                'Este usuário está desativado')
        # check if the user has been active
        if user.ativo == 0:
            raise exceptions.AuthenticationFailed(
                'Este usuário está desativado')
        instituicao = Instit.objects.get(pk=user.instit_id)
        # check if the institution has ben active
        if instituicao.ativo == 0:
            raise exceptions.AuthenticationFailed(
                'A instituição deste usuário está desativada')

        self.enforce_csrf(request)
        return (user, None)

    def enforce_csrf(self, request):
        """
        Enforce CSRF validation
        """
        # check = CSRFCheck()
        # # populates request.META['CSRF_COOKIE'], which is used in process_view()
        # check.process_request(request)
        # reason = check.process_view(request, None, (), {})
        # if reason:
        #     # CSRF failed, bail with explicit error message
        #     raise exceptions.PermissionDenied('CSRF Failed: %s' % reason)
        return
