from django.db import models


class Enderecos(models.Model):
    id_enderecos = models.AutoField(primary_key=True)
    situacao = models.IntegerField()
    origem = models.PositiveIntegerField()
    id_pessoa_cod_fk = models.IntegerField()
    endtip = models.PositiveIntegerField()
    rua = models.CharField(max_length=100, blank=True, null=True)
    numero = models.CharField(max_length=8, blank=True, null=True)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=40, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    cidade = models.CharField(max_length=20, blank=True, null=True)
    estado_endereco = models.CharField(max_length=3, blank=True, null=True)
    data_criacao = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enderecos'
