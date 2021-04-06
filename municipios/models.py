from django.db import models


class Municipios(models.Model):
    id_municipios = models.IntegerField(primary_key=True)
    descr = models.CharField(max_length=35)
    uf_sigla = models.CharField(max_length=2)
    coduf = models.PositiveIntegerField()
    ibge = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'municipios'
        ordering = ['descr']

    def __str__(self):
        return self.descr
