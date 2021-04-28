from django.db import models


class Fabpro(models.Model):
    instit = models.PositiveIntegerField()
    marca = models.CharField(max_length=25)
    fabr = models.CharField(max_length=40, blank=True, null=True)
    data_criacao = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fabpro'
        ordering = ['marca', ]
