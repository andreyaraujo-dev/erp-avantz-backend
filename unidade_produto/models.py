from django.db import models


class Unidades(models.Model):
    instit = models.PositiveIntegerField()
    ativo = models.PositiveIntegerField()
    und = models.CharField(max_length=2)
    descr = models.CharField(max_length=12)
    tipo = models.PositiveIntegerField()
    data_criacao = models.DateTimeField()
    data_atualizacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidades'
        ordering = ['und', ]
