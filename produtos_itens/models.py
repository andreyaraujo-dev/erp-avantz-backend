from django.db import models

# Create your models here.


class ProdItens(models.Model):
    id_produtos = models.PositiveIntegerField()
    id_instit = models.PositiveIntegerField()
    id_matriz = models.PositiveIntegerField()
    codprod = models.PositiveIntegerField()
    ativo = models.PositiveIntegerField(blank=True, null=True)
    bxest = models.PositiveIntegerField()
    est_minimo = models.DecimalField(max_digits=12, decimal_places=3)
    est_fiscal = models.DecimalField(max_digits=12, decimal_places=3)
    est_frente = models.DecimalField(max_digits=12, decimal_places=3)
    est_dep1 = models.DecimalField(max_digits=12, decimal_places=3)
    est_dep2 = models.DecimalField(max_digits=12, decimal_places=3)
    est_dep3 = models.DecimalField(max_digits=12, decimal_places=3)
    compra = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    frete = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    ipi = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    aliq = models.PositiveIntegerField()
    custo = models.DecimalField(max_digits=10, decimal_places=2)
    lucro = models.DecimalField(max_digits=10, decimal_places=2)
    prvenda1 = models.DecimalField(max_digits=10, decimal_places=2)
    prvenda2 = models.DecimalField(max_digits=10, decimal_places=2)
    prvenda3 = models.DecimalField(max_digits=10, decimal_places=2)
    locavel = models.PositiveIntegerField()
    prloc = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    vdatac = models.PositiveIntegerField()
    qtdatac = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True)
    pratac = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    loc_frente = models.CharField(max_length=20, blank=True, null=True)
    loc_dep1 = models.CharField(max_length=20, blank=True, null=True)
    loc_dep2 = models.CharField(max_length=20, blank=True, null=True)
    loc_dep3 = models.CharField(max_length=20, blank=True, null=True)
    comissao_atv = models.PositiveIntegerField()
    comissao_val = models.DecimalField(max_digits=7, decimal_places=3)
    datatz = models.DateTimeField(blank=True, null=True)
    usuatz = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'prod_itens'
        ordering = ['codprod', ]
        unique_together = (('id_instit', 'codprod'),)
