from django.db import models
from cloudinary.models import CloudinaryField

from users.models import Users
from instituicao.models import Instit


class ImagensUsuarios(models.Model):
    user_id = models.ForeignKey(
        Users, on_delete=models.DO_NOTHING, blank=False, verbose_name='id usuario')
    instit_id = models.ForeignKey(
        Instit, on_delete=models.DO_NOTHING, blank=False, verbose_name='id instituicao')
    imagem = CloudinaryField(blank=False, verbose_name='imagem')
