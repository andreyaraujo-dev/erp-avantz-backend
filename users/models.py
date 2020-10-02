import re
from django.db import models
from django.core import validators
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings

from instituicao.models import Instit
from pescod.models import Pescod
from users_groups.models import UsersGrp


class UserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, email, idpescod, instit, ativo, idgrp, acess, password=None):
        if not username:
            raise ValueError(_('The given username must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, first_name=first_name, last_name=last_name, email=email, idpescod=idpescod,
                          instit=instit, ativo=ativo, idgrp=idgrp, acess=acess)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, idpescod, instit, ativo, idgrp, acess):
        user = self.create_user(username, email=email, password=password,
                                idpescod=idpescod, instit=instit, ativo=ativo, idgrp=idgrp, acess=acess)
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=15, unique=True)
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    email = models.EmailField(_('email address'), max_length=255)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_trusty = models.BooleanField(_('trusty'), default=False,
                                    help_text=_('Designates whether this user has confirmed his account.'))
    idpescod = models.ForeignKey(
        Pescod, on_delete=models.DO_NOTHING, verbose_name='ID registro pessoa')
    instit = models.ForeignKey(
        Instit, on_delete=models.DO_NOTHING, verbose_name='ID instituição')
    ativo = models.PositiveIntegerField(blank=True, null=True)
    idgrp = models.ForeignKey(
        UsersGrp, on_delete=models.DO_NOTHING, verbose_name='ID grupo')
    login = models.CharField(max_length=25)
    nome = models.CharField(max_length=25, blank=True, null=True)
    numlog = models.PositiveIntegerField(blank=True, null=True)
    senha = models.CharField(max_length=20)
    acess = models.CharField(max_length=255,
                             default='0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
                             verbose_name='Acesso')
    desenv = models.PositiveIntegerField(
        blank=True, null=True, verbose_name='Desenvolvedor')
    datsenha = models.DateTimeField(blank=True, null=True)
    data_criacao = models.DateTimeField(
        blank=True, null=True, auto_now_add=True)
    data_atualizacao = models.DateTimeField(
        blank=True, null=True, auto_now_add=True)
    data_de_exclusao = models.DateTimeField(
        blank=True, null=True, auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'

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
