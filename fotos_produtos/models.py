from django.db import models
from instituicao.models import Instit
from produtos.models import Produtos


class Fotos(models.Model):
    id_foto = models.AutoField(primary_key=True)
    id_instituicao = models.ForeignKey(
        Instit, models.DO_NOTHING, db_column='id_instituicao')
    id_produto = models.ForeignKey(
        Produtos, models.DO_NOTHING, db_column='id_produto')
    nome_arquivo = models.ImageField(
        upload_to='products/%Y/%m/%d', blank=True, null=True)
    data_criacao = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fotos'
