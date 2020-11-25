from django.db import models


class Refbanco(models.Model):
    id_banco = models.AutoField(primary_key=True)
    id_pessoa_cod_fk = models.IntegerField()
    id_bancos_fk = models.IntegerField()
    situacao = models.IntegerField()
    agencia = models.CharField(max_length=6, blank=True, null=True)
    conta = models.CharField(max_length=10, blank=True, null=True)
    abertura = models.DateTimeField(blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    data_criacao = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'refbanco'
