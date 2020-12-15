from django.db import models

class It_Ped(models.Model):
    class It_Ped(models.Model):
        id = models.PositiveIntegerField(primary_key=True)
        id_pedido = models.PositiveIntegerField()
        cpro =  models.PositiveIntegerField()
        prod = models.CharField(max_length=50, blank=True, null=True)
        und = models.CharField(max_length=2, blank=True, null=True)
        qtd = models.DecimalField(max_digits=10, decimal_places=2)
        valor = models.DecimalField(max_digits=10, decimal_places=2)
        valtab = models.DecimalField(max_digits=10, decimal_places=2) # valor preço tabela
        id_produtos = models.PositiveIntegerField()

        class Meta:
            managed = False
            db_table = 'it_ped'
            unique_together = (('id'),('id_pedido'))
