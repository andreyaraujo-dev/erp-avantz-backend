from django.db import models

# Create your models here.


class Telefones(models.Model):
    id_telefone = models.AutoField(primary_key=True)
    id_pessoa_cod_fk = models.IntegerField()
    situacao = models.IntegerField()
    tel = models.CharField(max_length=20, blank=True, null=True)
    data_criacao = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'telefones'
