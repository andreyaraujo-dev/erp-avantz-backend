from django.db import models


class Mails(models.Model):
    id_mails = models.AutoField(primary_key=True)
    id_pessoa_cod_fk = models.IntegerField()
    situacao = models.IntegerField()
    email = models.CharField(max_length=45, blank=True, null=True)
    data_criacao = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mails'
