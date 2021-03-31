from django.db import models


class Pesfis(models.Model):
    id_pessoa_fisica = models.AutoField(primary_key=True)
    id_pessoa_cod_fk = models.IntegerField()
    identidade = models.CharField(max_length=20)
    emissor_identidade = models.CharField(max_length=50)
    id_municipio_fk = models.IntegerField()
    id_uf_municipio_fk = models.IntegerField()
    data_de_nascimento = models.DateField(blank=True, null=True)
    tratam = models.PositiveIntegerField()
    apelido = models.CharField(max_length=25, blank=True, null=True)
    sexo = models.CharField(max_length=20)
    pai = models.CharField(max_length=60, blank=True, null=True)
    mae = models.CharField(max_length=60, blank=True, null=True)
    profissao = models.CharField(max_length=30, blank=True, null=True)
    ctps = models.CharField(max_length=15, blank=True, null=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    empresa = models.CharField(max_length=50, blank=True, null=True)
    resp = models.CharField(max_length=25, blank=True, null=True)
    cnpj = models.CharField(max_length=18, blank=True, null=True)
    iest = models.CharField(max_length=20, blank=True, null=True)
    imun = models.CharField(max_length=15, blank=True, null=True)
    emprend = models.CharField(max_length=200)
    orendas = models.CharField(max_length=50, blank=True, null=True)
    vrendas = models.DecimalField(max_digits=10, decimal_places=2)
    irpf = models.PositiveIntegerField()
    estcivil = models.PositiveIntegerField()
    depend = models.PositiveIntegerField()
    pensao = models.DecimalField(max_digits=10, decimal_places=2)
    conjuge = models.CharField(max_length=60, blank=True, null=True)
    cpfconj = models.CharField(max_length=14, blank=True, null=True)
    profconj = models.CharField(max_length=30, blank=True, null=True)
    emprconj = models.CharField(max_length=50, blank=True, null=True)
    rendaconj = models.DecimalField(max_digits=10, decimal_places=2)
    telconj = models.CharField(max_length=11, blank=True, null=True)
    mailconj = models.CharField(max_length=50, blank=True, null=True)
    data_criacao = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pesfis'
