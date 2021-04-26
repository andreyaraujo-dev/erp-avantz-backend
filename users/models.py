import re
from django.db import models
from django.core import validators
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings

from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created

from instituicao.models import Instit
from pescod.models import Pescod
from users_groups.models import UsersGrp


class UserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, email, idpescod, instit, ativo, idgrp, acess, password=None):
        if not username:
            raise ValueError(_('The given username must be set'))
        email = self.normalize_email(email)
        id_pescod = Pescod.objects.get(pk=idpescod)
        id_instit = Instit.objects.get(pk=instit)
        id_user_group = UsersGrp.objects.get(pk=idgrp)
        user = self.model(username=username, first_name=first_name, last_name=last_name, email=email, idpescod=id_pescod,
                          instit=id_instit, ativo=ativo, idgrp=id_user_group, acess=acess)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, email, password, idpescod, instit, ativo, idgrp, acess):
        # id_pescod = Pescod.objects.get(pk=idpescod)
        # id_instit = Instit.objects.get(pk=instit)
        # id_user_group = UsersGrp.objects.get(pk=idgrp)

        user = self.create_user(username, first_name=first_name, last_name=last_name, email=email, password=password,
                                idpescod=idpescod, instit=instit, ativo=ativo, idgrp=idgrp, acess=acess)
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=15, unique=True)
    first_name = models.CharField(
        _('first name'), max_length=30, blank=False, null=False,)
    last_name = models.CharField(
        _('last name'), max_length=30, blank=False, null=True,)
    email = models.EmailField(_('email address'), max_length=255, blank=False)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_trusty = models.BooleanField(_('trusty'), default=False,
                                    help_text=_('Designates whether this user has confirmed his account.'))
    idpescod = models.ForeignKey(
        Pescod, on_delete=models.DO_NOTHING, blank=False, verbose_name='registro pessoa')
    instit = models.ForeignKey(
        Instit, on_delete=models.DO_NOTHING, blank=False, verbose_name='instituição')
    ativo = models.PositiveIntegerField(blank=False, null=False, default=1)
    idgrp = models.ForeignKey(
        UsersGrp, on_delete=models.DO_NOTHING, blank=False, verbose_name='grupo')
    login = models.CharField(max_length=25, blank=True, null=True)
    nome = models.CharField(max_length=25, blank=True, null=True)
    numlog = models.PositiveIntegerField(blank=True, null=True)
    senha = models.CharField(max_length=20, blank=True, null=True)
    acess = models.CharField(max_length=255, blank=False, null=False,
                             default='0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
                             verbose_name='Acesso')
    foto = models.ImageField(
        upload_to='images/%Y/%m/%d', blank=True, null=True)
    desenv = models.PositiveIntegerField(
        blank=True, null=True, verbose_name='Desenvolvedor')
    datsenha = models.DateTimeField(blank=True, null=True)
    data_criacao = models.DateTimeField(
        blank=True, null=True, auto_now_add=True)
    data_atualizacao = models.DateTimeField(
        blank=True, null=True, auto_now_add=True)
    data_de_exclusao = models.DateTimeField(
        blank=True, null=True, auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'idpescod',
                       'instit', 'ativo', 'idgrp', 'acess', 'first_name', 'last_name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.username

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(
        reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )
