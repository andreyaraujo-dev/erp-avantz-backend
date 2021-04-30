from django.db import models


class Produtos(models.Model):
    id_matriz = models.PositiveIntegerField()
    codprod = models.PositiveIntegerField()
    ativo = models.PositiveIntegerField(blank=True, null=True)
    descr = models.CharField(max_length=50)
    descres = models.CharField(max_length=25, blank=True, null=True)
    und = models.IntegerField()
    grupo = models.PositiveIntegerField()
    tam = models.DecimalField(max_digits=6, decimal_places=3)
    larg = models.DecimalField(max_digits=6, decimal_places=3)
    alt = models.DecimalField(max_digits=6, decimal_places=3)
    cubag = models.DecimalField(max_digits=7, decimal_places=4)
    peso = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    codbarra = models.CharField(max_length=25, blank=True, null=True)
    fabr = models.IntegerField()
    forn = models.PositiveIntegerField(blank=True, null=True)
    caract = models.CharField(max_length=50, blank=True, null=True)
    ncm = models.CharField(max_length=8, blank=True, null=True)
    cest = models.CharField(max_length=8, blank=True, null=True)
    desnf = models.CharField(max_length=40)
    foto = models.CharField(max_length=25)
    img_bites = models.PositiveIntegerField(blank=True, null=True)
    datatz = models.DateTimeField(blank=True, null=True)
    usuatz = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'produtos'
        ordering = ['descres', ]
        unique_together = (('id_matriz', 'descr'),
                           ('id_matriz', 'codbarra'), ('id_matriz', 'codprod'),)
