from django.db import models


class Pescod(models.Model):
    id_pessoa_cod = models.AutoField(primary_key=True)
    id_instituicao_fk = models.IntegerField()
    tipo = models.PositiveIntegerField()
    sit = models.PositiveIntegerField()
    forn = models.PositiveIntegerField()
    cpfcnpj = models.CharField(max_length=18, blank=True, null=True)
    # Field name made lowercase.
    nomeorrazaosocial = models.CharField(
        db_column='nomeOrRazaoSocial', unique=True, max_length=100, blank=True, null=True)
    foto = models.CharField(max_length=25)
    img_bites = models.PositiveIntegerField()
    limite = models.DecimalField(max_digits=10, decimal_places=2)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    data_criacao = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pescod'
        ordering = ['nomeorrazaosocial']

    def __str__(self):
        return self.nomeorrazaosocial
