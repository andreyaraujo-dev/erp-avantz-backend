from django.db import models

# Create your models here.


class ProdGrp(models.Model):
    instit = models.PositiveIntegerField()
    niv = models.PositiveIntegerField()
    nv1 = models.CharField(max_length=25)
    nv2 = models.CharField(max_length=25, blank=True, null=True)
    nv1id = models.PositiveIntegerField(blank=True, null=True)
    nv3 = models.CharField(max_length=25, blank=True, null=True)
    nv2id = models.PositiveIntegerField(blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    data_criacao = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prod_grp'
