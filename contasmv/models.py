from django.db import models

class ContasMv(models.Model):
    id = models.IntegerField(primary_key=True)
    instit_id = models.PositiveIntegerField()
    idctfin = models.PositiveIntegerField()
    idsecao = models.PositiveIntegerField()
    tipo = models.PositiveIntegerField() # 0=abert 1=cred 2=deb
    descr = models.CharField(max_length=60, blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    dat = models.DateTimeField(blank=True, null=True)
    idorigem = models.PositiveIntegerField()
    usuario = models.PositiveIntegerField()
    mcx = models.PositiveIntegerField()
    sit = models.PositiveIntegerField()                                # 1=atv 2=delete
    saldocons = models.DecimalField(max_digits=10, decimal_places=2)   # saldo consolidado

    class Meta:
        managed = False
        db_table = 'contasmv'