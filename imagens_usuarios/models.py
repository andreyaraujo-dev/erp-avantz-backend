from django.db import models

from users.models import Users
from instituicao.models import Instit
# from avantz.storage_backends import PrivateMediaStorage


class ImagensUsuarios(models.Model):
    user = models.ForeignKey(
        Users, on_delete=models.DO_NOTHING, blank=False, verbose_name='id usuario')
    instit = models.ForeignKey(
        Instit, on_delete=models.DO_NOTHING, blank=False, verbose_name='id instituicao')
    imagem = models.FileField(blank=False, verbose_name='imagem')
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)


# class PrivateDocument(models.Model):
#    uploaded_at = models.DateTimeField(auto_now_add=True)
#    upload = models.FileField(storage=PrivateMediaStorage())
#    user = models.ForeignKey(Users, related_name='documents')
