from django.db import models

class Pedidos(models.Model):
    class Pedidos(models.Model):
        id = models.PositiveIntegerField(primary_key=True)
        sit = models.PositiveSmallIntegerFieldd()           # 0=venda 1=cancelado 2=servicos
        instit = models.PositiveIntegerField()
        codped = models.PositiveIntegerField()              # cod pedido da instit
        dat = models.DateTimeField()
        tven = models.PositiveIntegerField()                # tabela de preço utilizada no pedido
        tcli = models.PositiveSmallIntegerField()           # tipo de cliente 1=avulso 2=pesfis 3=pesjur 4=transf
        ccli = models.PositiveIntegerField()                # idpescod a partir 26maio2020
        cli = models.CharField(max_length=50)
        tend = models.PositiveIntegerField()                # tipo de endereço (em desuso)
        end = models.CharField(max_length=40, blank=True, null=True)
        endnum = models.CharField(max_length=6, blank=True, null=True)
        endcompl = models.CharField(max_length=30, blank=True, null=True)
        bairro = models.CharField(max_length=30, blank=True, null=True)
        cep = models.CharField(max_length=10, blank=True, null=True)
        idmunicipio = models.PositiveIntegerField()         # id tabela municipio
        idpais = models.PositiveIntegerField()              # id tabela pais
        tel1 = models.CharField(max_length=14, blank=True, null=True)
        tel2 = models.CharField(max_length=14, blank=True, null=True)
        ptref = models.CharField(max_length=30, blank=True, null=True)
        tot = models.DecimalField(max_digits=10, decimal_places=2)
        vacr = models.DecimalField(max_digits=10, decimal_places=2)
        vdesc = models.DecimalField(max_digits=10, decimal_places=2)
        totpg = models.DecimalField(max_digits=10, decimal_places=2)
        codusu = models.PositiveIntegerField()
        msg = models.CharField(max_length=30, blank=True, null=True)
        msg2 = models.CharField(max_length=200, blank=True, null=True)

        class Meta:
            managed = False
            db_table = 'pedidos'
            unique_together = (('instit', 'codped'),('instit','ccli','cli','dat','codusu'))
