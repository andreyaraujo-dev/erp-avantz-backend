from django.db import models
from cloudinary.models import CloudinaryField

from users.models import Users
from instituicao.models import Instit


class ImagensUsuarios(models.Model):
    user = models.ForeignKey(
        Users, on_delete=models.DO_NOTHING, blank=False, verbose_name='id usuario')
    instit = models.ForeignKey(
        Instit, on_delete=models.DO_NOTHING, blank=False, verbose_name='id instituicao')
    imagem = CloudinaryField(blank=False, verbose_name='imagem')
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
