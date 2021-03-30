from django.db import models


class Pesjur(models.Model):
    id_pessoa_juridica = models.AutoField(primary_key=True)
    id_pessoa_cod_fk = models.IntegerField()
    fantasia = models.CharField(max_length=50, blank=True, null=True)
    ramo = models.CharField(max_length=255, blank=True, null=True)
    inscricao_estadual = models.CharField(max_length=20, blank=True, null=True)
    inscricao_municipal = models.CharField(
        max_length=20, blank=True, null=True)
    tipo_empresa = models.CharField(max_length=100, blank=True, null=True)
    capsocial = models.DecimalField(max_digits=15, decimal_places=2)
    faturamento = models.DecimalField(max_digits=15, decimal_places=2)
    tribut = models.PositiveIntegerField()
    contato = models.CharField(max_length=25, blank=True, null=True)
    data_abertura = models.DateField()
    data_criacao = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pesjur'
        ordering = ['fantasia']

    def __str__(self):
        return self.fantasia
