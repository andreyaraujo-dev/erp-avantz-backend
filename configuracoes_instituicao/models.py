from django.db import models


class Configs(models.Model):
    cfg1 = models.CharField(max_length=1)
    cfg2 = models.CharField(max_length=1)
    cfg3 = models.CharField(max_length=30)
    cfg4 = models.CharField(max_length=30)
    cfg5 = models.CharField(max_length=1)
    cfg6 = models.CharField(max_length=8)
    cfg7 = models.CharField(max_length=4)
    cfg8 = models.CharField(max_length=60, blank=True, null=True)
    cfg9 = models.CharField(max_length=4)
    cfg10 = models.CharField(max_length=2)
    cfg11 = models.CharField(max_length=15)
    cfg12 = models.CharField(max_length=3)
    cfg13 = models.CharField(max_length=1)
    cfg14 = models.CharField(max_length=1)
    cfg15 = models.CharField(max_length=4)
    cfg16 = models.CharField(max_length=20)
    cfg17 = models.CharField(max_length=5)
    cfg18 = models.CharField(max_length=100)
    cfg19 = models.CharField(max_length=10)
    cfg20 = models.CharField(max_length=10)
    cfg21 = models.CharField(max_length=10)
    cfg22 = models.CharField(max_length=8)
    cfg23 = models.CharField(max_length=1)
    cfg24 = models.CharField(max_length=8)
    cfg25 = models.CharField(max_length=1)
    cfg26 = models.CharField(max_length=8)
    cfg27 = models.CharField(max_length=8)
    cfg28 = models.CharField(max_length=8)
    cfg29 = models.CharField(max_length=8)
    cfg30 = models.CharField(max_length=8)
    cfg31 = models.CharField(max_length=8)
    cfg32 = models.CharField(max_length=8, blank=True, null=True)
    data_criacao = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'configs'
