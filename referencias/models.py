from django.db import models


class Referencias(models.Model):
    id_referencia = models.AutoField(primary_key=True)
    id_pessoa_cod_fk = models.IntegerField()
    situacao = models.IntegerField()
    tipo = models.CharField(max_length=15, blank=True, null=True)
    nome = models.CharField(max_length=50, blank=True, null=True)
    tel = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    data_criacao = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'referencias'
