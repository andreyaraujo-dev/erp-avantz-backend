from django.db import models

# Create your models here.


class Funcio(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    instit = models.PositiveIntegerField()
    idpescod = models.PositiveIntegerField()
    iduser = models.PositiveIntegerField()
    nome = models.CharField(max_length=60)
    sit = models.PositiveIntegerField()
    dtadm = models.DateTimeField(blank=True, null=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    comissao = models.DecimalField(max_digits=7, decimal_places=4)
    gratif = models.DecimalField(max_digits=10, decimal_places=2)
    adiant = models.DecimalField(max_digits=10, decimal_places=2)
    inss = models.DecimalField(max_digits=7, decimal_places=3)
    obs = models.CharField(max_length=100, blank=True, null=True)
    ativo = models.PositiveIntegerField(default=1)

    class Meta:
        managed = False
        db_table = 'funcio'
        unique_together = (('instit', 'nome'), ('instit', 'idpescod'),)
        ordering = ['nome', ]
