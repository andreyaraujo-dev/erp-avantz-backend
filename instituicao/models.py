from django.db import models


class Instit(models.Model):
    id_instituicao = models.AutoField(primary_key=True)
    idmatriz = models.PositiveIntegerField()
    idpjur = models.PositiveIntegerField()
    ativo = models.PositiveIntegerField()
    nome = models.CharField(max_length=40)
    razsoc = models.CharField(max_length=80, blank=True, null=True)
    endtip = models.PositiveIntegerField()
    end = models.CharField(max_length=50, blank=True, null=True)
    endnum = models.CharField(max_length=8, blank=True, null=True)
    endcompl = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=40, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    id_uf = models.PositiveIntegerField()
    id_municipio = models.PositiveIntegerField()
    cnpj = models.CharField(max_length=18, blank=True, null=True)
    iest = models.CharField(max_length=25, blank=True, null=True)
    imun = models.CharField(max_length=10, blank=True, null=True)
    mail1 = models.CharField(max_length=60)
    mail2 = models.CharField(max_length=60, blank=True, null=True)
    tel1 = models.CharField(max_length=14, blank=True, null=True)
    tel2 = models.CharField(max_length=14, blank=True, null=True)
    tel3 = models.CharField(max_length=14, blank=True, null=True)
    fax = models.CharField(max_length=13, blank=True, null=True)
    slogan = models.CharField(max_length=60, blank=True, null=True)
    modulos = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instit'
        ordering = ['nome', ]

    def __str__(self):
        return self.nome
