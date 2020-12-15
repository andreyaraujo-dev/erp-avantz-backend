from django.db import models

class ContasFin(models.Model):
    id = models.IntegerField(primary_key=True)
    instit_id = models.PositiveIntegerField()
    sit = models.PositiveSmallIntegerField() # 1=ativa 2=desativada
    tipo = models.PositiveSmallIntegerField(blank=True, null=True) # 1=dinheiro 2=ct corr 3=ct ppça 4=cartao cred 5=chq
    idsecao = models.PositiveIntegerField()
    nome = models.CharField(max_length=30)
    dtabr = models.DateTimeField(blank=True, null=True)
    saldoini = models.DecimalField(max_digits=10, decimal_places=2)
    cobr = models.PositiveIntegerField() # utilizada na cobrança: 1=não 2=sim
    idbco = models.PositiveIntegerField()
    conv = models.CharField(max_length=20, blank=True, null=True)
    convdig = models.CharField(max_length=1, blank=True, null=True)
    cedente = models.CharField(max_length=40, blank=True, null=True)
    ced_endlogr = models.CharField(max_length=60, blank=True, null=True)
    ced_endnum = models.CharField(max_length=8, blank=True, null=True)
    ced_endcomp = models.CharField(max_length=30, blank=True, null=True)
    ced_endbairro = models.CharField(max_length=30, blank=True, null=True)
    ced_endcep = models.CharField(max_length=9, blank=True, null=True)
    ced_endcidade = models.CharField(max_length=35, blank=True, null=True)
    ced_enduf = models.CharField(max_length=2, blank=True, null=True)
    cpfcnpj = models.CharField(max_length=18, blank=True, null=True)
    cedcod = models.CharField(max_length=8, blank=True, null=True)
    cedagenc = models.CharField(max_length=4, blank=True, null=True)
    cedagd = models.CharField(max_length=1, blank=True, null=True)
    cedconta = models.CharField(max_length=10, blank=True, null=True)
    cedctdig = models.CharField(max_length=1, blank=True, null=True)
    oper = models.CharField(max_length=3, blank=True, null=True)
    carteira = models.CharField(max_length=3, blank=True, null=True)
    variacao = models.CharField(max_length=2, blank=True, null=True)
    idbolesp = models.PositiveIntegerField()
    instr1 = models.CharField(max_length=80, blank=True, null=True)
    instr2 = models.CharField(max_length=80, blank=True, null=True)
    instr3 = models.CharField(max_length=80, blank=True, null=True)
    idmoeda = models.PositiveSmallIntegerField()
    taxa = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    gerente = models.CharField(max_length=25, blank=True, null=True)
    tel = models.CharField(max_length=14, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    mora_mes = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True) # percentual
    dias_protesto = models.PositiveSmallIntegerField()
    multa_atraso = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contasfin'
        unique_together = (('instit_id', 'tipo', 'cedagenc', 'cedconta'),)
        unique_together = (('instit_id', 'idsecao'),)