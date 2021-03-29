# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountAccount(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=15)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=255)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    is_trusty = models.IntegerField()
    idpescod = models.PositiveIntegerField(blank=True, null=True)
    instit = models.PositiveIntegerField(blank=True, null=True)
    ativo = models.PositiveIntegerField(blank=True, null=True)
    idgrp = models.PositiveIntegerField(blank=True, null=True)
    login = models.CharField(max_length=25)
    nome = models.CharField(max_length=25, blank=True, null=True)
    numlog = models.PositiveIntegerField(blank=True, null=True)
    senha = models.CharField(max_length=20)
    acess = models.CharField(max_length=255)
    desenv = models.PositiveIntegerField(blank=True, null=True)
    datsenha = models.DateTimeField(blank=True, null=True)
    data_criacao = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)
    data_de_exclusao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_account'


class AccountAccountGroups(models.Model):
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_groups'
        unique_together = (('account', 'group'),)


class AccountAccountUserPermissions(models.Model):
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_user_permissions'
        unique_together = (('account', 'permission'),)


class Acessos(models.Model):
    instit = models.PositiveIntegerField()
    iduser = models.PositiveIntegerField()
    user = models.CharField(max_length=10, blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    rotina = models.IntegerField(blank=True, null=True)
    acess = models.CharField(max_length=50, blank=True, null=True)
    data_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acessos'


class Aliquotas(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    instit = models.PositiveIntegerField()
    descr = models.CharField(max_length=6)
    bematech = models.CharField(max_length=2)
    valor = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aliquotas'
        unique_together = (('instit', 'descr'),)


class Audit(models.Model):
    id = models.IntegerField(primary_key=True)
    loja = models.PositiveIntegerField(blank=True, null=True)
    codpro = models.PositiveIntegerField()
    frtold = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True)
    frtnew = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True)
    depold = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True)
    depnew = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True)
    fscold = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True)
    fscnew = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True)
    usuario = models.CharField(max_length=10, blank=True, null=True)
    datatz = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audit'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class Bancos(models.Model):
    id_bancos = models.IntegerField(primary_key=True)
    cod = models.PositiveIntegerField()
    banco = models.CharField(max_length=50)
    # Field name made lowercase.
    ispb = models.PositiveIntegerField(db_column='ISPB')
    compens = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'bancos'


class Bancosextr(models.Model):
    id = models.IntegerField(primary_key=True)
    idcontas = models.PositiveIntegerField()
    dtmov = models.DateTimeField(blank=True, null=True)
    dtbal = models.DateTimeField(blank=True, null=True)
    agorig = models.CharField(max_length=4, blank=True, null=True)
    lote = models.CharField(max_length=5, blank=True, null=True)
    doc = models.CharField(max_length=17, blank=True, null=True)
    codhist = models.CharField(max_length=3, blank=True, null=True)
    hist = models.CharField(max_length=25, blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.PositiveIntegerField()
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    fav = models.CharField(max_length=38, blank=True, null=True)
    dtimp = models.DateTimeField(blank=True, null=True)
    usuario = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'bancosextr'


class BoletoCbRemessa(models.Model):
    id_boleto_cb_remessa = models.AutoField(primary_key=True)
    id_banco_fk = models.ForeignKey(
        Bancos, models.DO_NOTHING, db_column='id_banco_fk', blank=True, null=True)
    id_remessa_banco = models.IntegerField(blank=True, null=True)
    situacao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'boleto_cb_remessa'


class BoletoCbRetorno(models.Model):
    id_boleto_sit = models.AutoField(primary_key=True)
    idbanco = models.PositiveIntegerField()
    id_retorno_banco = models.CharField(max_length=11)
    situacao = models.CharField(max_length=40)
    edit = models.PositiveIntegerField()
    baixado = models.PositiveIntegerField()
    codret = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'boleto_cb_retorno'


class BoletoEsp(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    cod = models.CharField(max_length=3)
    especie = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'boleto_esp'


class BoletoRet(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    instit = models.IntegerField()
    data = models.DateTimeField()
    arquivo = models.CharField(max_length=30)
    banco = models.CharField(max_length=3)
    convenio = models.CharField(max_length=20)
    agencia = models.CharField(max_length=5)
    agcdig = models.CharField(max_length=1, blank=True, null=True)
    conta = models.CharField(max_length=12)
    cntdig = models.CharField(max_length=1)
    dtret = models.DateTimeField()
    nosson = models.CharField(max_length=20)
    valpg = models.DecimalField(max_digits=10, decimal_places=2)
    valliq = models.DecimalField(max_digits=10, decimal_places=2)
    datpg = models.DateTimeField()
    taxas = models.DecimalField(max_digits=10, decimal_places=2)
    acresc = models.DecimalField(max_digits=10, decimal_places=2)
    descont = models.DecimalField(max_digits=10, decimal_places=2)
    abatim = models.DecimalField(max_digits=10, decimal_places=2)
    iof = models.DecimalField(max_digits=10, decimal_places=2)
    dtcred = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'boleto_ret'


class Boletos(models.Model):
    id_boletos = models.AutoField(primary_key=True)
    instit = models.PositiveIntegerField()
    idbolsit = models.PositiveIntegerField()
    id_remessa_cb_fk = models.IntegerField()
    id_conta_fin_fk = models.IntegerField(blank=True, null=True)
    baixado = models.IntegerField()
    datbx = models.DateTimeField()
    valpg = models.DecimalField(max_digits=10, decimal_places=2)
    valliq = models.DecimalField(max_digits=10, decimal_places=2)
    usubx = models.PositiveIntegerField()
    tipcli = models.PositiveIntegerField()
    codcli = models.PositiveIntegerField()
    nomecli = models.CharField(max_length=60)
    cnpjcli = models.CharField(max_length=18, blank=True, null=True)
    tendcli = models.PositiveIntegerField()
    endcli = models.CharField(max_length=40)
    nendcli = models.CharField(max_length=10, blank=True, null=True)
    cendcli = models.CharField(max_length=30, blank=True, null=True)
    cepcli = models.CharField(max_length=10)
    baircli = models.CharField(max_length=30, blank=True, null=True)
    cidcli = models.PositiveIntegerField()
    ufcli = models.PositiveIntegerField()
    bcocod = models.CharField(max_length=3)
    bcodig = models.CharField(max_length=1)
    bconome = models.CharField(max_length=30)
    conv = models.CharField(max_length=20)
    convdig = models.CharField(max_length=1, blank=True, null=True)
    cedente = models.CharField(max_length=40)
    cedend = models.CharField(max_length=60)
    cpfcnpj = models.CharField(max_length=18)
    cedcod = models.CharField(max_length=10)
    cedagenc = models.CharField(max_length=4)
    cedagd = models.CharField(max_length=1)
    cedconta = models.CharField(max_length=10, blank=True, null=True)
    cedctdig = models.CharField(max_length=1, blank=True, null=True)
    ced_rua = models.CharField(max_length=100, blank=True, null=True)
    ced_numero = models.CharField(max_length=45, blank=True, null=True)
    ced_bairro = models.CharField(max_length=45, blank=True, null=True)
    ced_cidade = models.CharField(max_length=25, blank=True, null=True)
    ced_cep = models.CharField(max_length=11, blank=True, null=True)
    ced_uf = models.CharField(max_length=4, blank=True, null=True)
    ced_complemento = models.CharField(max_length=100, blank=True, null=True)
    carteira = models.CharField(max_length=4, blank=True, null=True)
    variacao = models.CharField(max_length=2, blank=True, null=True)
    esptit = models.CharField(max_length=2, blank=True, null=True)
    moeda = models.CharField(max_length=1, blank=True, null=True)
    moedasimb = models.CharField(max_length=3, blank=True, null=True)
    jurosdia = models.DecimalField(max_digits=10, decimal_places=2)
    multa = models.DecimalField(max_digits=10, decimal_places=2)
    diasprot = models.PositiveIntegerField()
    aceite = models.PositiveIntegerField()
    desconto = models.DecimalField(max_digits=10, decimal_places=2)
    dtemis = models.DateTimeField(blank=True, null=True)
    taxa = models.DecimalField(max_digits=10, decimal_places=2)
    nosson = models.CharField(max_length=20)
    numdoc = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status_retorno = models.CharField(max_length=100, blank=True, null=True)
    dtvenc = models.DateField()
    localpg = models.CharField(max_length=60)
    instr1 = models.CharField(max_length=60, blank=True, null=True)
    instr2 = models.CharField(max_length=60, blank=True, null=True)
    instr3 = models.CharField(max_length=60, blank=True, null=True)
    instr4 = models.CharField(max_length=60, blank=True, null=True)
    instr5 = models.CharField(max_length=60, blank=True, null=True)
    instr6 = models.CharField(max_length=60, blank=True, null=True)
    data_atualizacao = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'boletos'


class CDele(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    origem = models.PositiveIntegerField()
    idorigem = models.PositiveIntegerField()
    motivo = models.CharField(max_length=40)
    iduser = models.PositiveIntegerField()
    data = models.DateTimeField()
    instit = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'c_dele'


class Cartaocred(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    instit = models.PositiveIntegerField()
    sit = models.PositiveIntegerField()
    nome = models.CharField(max_length=20)
    titular = models.CharField(max_length=30)
    num = models.CharField(max_length=16)
    emissor = models.CharField(max_length=20, blank=True, null=True)
    band = models.PositiveIntegerField()
    valid = models.CharField(max_length=5)
    portad = models.CharField(max_length=30)
    diavenc = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cartaocred'


class Cartaoextr(models.Model):
    id = models.IntegerField(primary_key=True)
    idcartao = models.PositiveIntegerField()
    idcontapg = models.PositiveIntegerField()
    sit = models.PositiveIntegerField()
    transac = models.CharField(max_length=35, blank=True, null=True)
    refnum = models.CharField(max_length=15, blank=True, null=True)
    fav = models.CharField(max_length=40, blank=True, null=True)
    descr = models.CharField(max_length=40, blank=True, null=True)
    emissao = models.DateTimeField()
    venc = models.DateTimeField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    secao = models.PositiveIntegerField()
    usuario = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cartaoextr'


class Ccaixa(models.Model):
    id = models.IntegerField(primary_key=True)
    instit = models.PositiveIntegerField()
    status = models.PositiveIntegerField()
    dtabr = models.DateTimeField()
    iduserabr = models.PositiveIntegerField()
    dtfech = models.DateTimeField(blank=True, null=True)
    iduserfech = models.PositiveIntegerField()
    totcx = models.DecimalField(max_digits=10, decimal_places=2)
    totpg = models.DecimalField(max_digits=10, decimal_places=2)
    difcx = models.DecimalField(max_digits=10, decimal_places=2)
    conferido = models.PositiveIntegerField()
    dtconf = models.DateTimeField(blank=True, null=True)
    idusuconf = models.PositiveIntegerField()
    revisado = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ccaixa'


class Ceps(models.Model):
    # Field name made lowercase.
    id = models.IntegerField(db_column='Id', primary_key=True)
    cep = models.PositiveIntegerField(unique=True)
    idmunic = models.PositiveIntegerField()
    iduf = models.PositiveIntegerField()
    idlogr = models.IntegerField()
    end = models.CharField(max_length=50)
    bairro = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ceps'


class Cnae(models.Model):
    # Field name made lowercase.
    id = models.PositiveIntegerField(db_column='Id', primary_key=True)
    cnae20 = models.CharField(max_length=9, blank=True, null=True)
    descr = models.CharField(max_length=170, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cnae'


class CodigoCfop(models.Model):
    # Field name made lowercase.
    cfop = models.IntegerField(db_column='CFOP', blank=True, null=True)
    inicio_vigencia = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'codigo_cfop'


class CodigoPaises(models.Model):
    id_pais = models.AutoField(primary_key=True)
    codigo_pais = models.IntegerField()
    nome_pais = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'codigo_paises'


class CodigoStcofins(models.Model):
    codigo = models.CharField(max_length=3, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'codigo_stcofins'


class CodigoStipi(models.Model):
    codigo = models.CharField(max_length=3, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'codigo_stipi'


class CodigoStpis(models.Model):
    codigo = models.CharField(max_length=3, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'codigo_stpis'


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


class Contasfin(models.Model):
    instit = models.IntegerField()
    sit = models.IntegerField()
    tipo = models.IntegerField(blank=True, null=True)
    idsecao = models.IntegerField()
    nome = models.CharField(max_length=30)
    dtabr = models.DateTimeField(blank=True, null=True)
    saldoini = models.DecimalField(max_digits=10, decimal_places=2)
    cobr = models.IntegerField()
    idbco = models.IntegerField()
    conv = models.CharField(max_length=20, blank=True, null=True)
    convdig = models.CharField(max_length=1, blank=True, null=True)
    cedente = models.CharField(max_length=40, blank=True, null=True)
    cedend = models.CharField(max_length=60, blank=True, null=True)
    cpfcnpj = models.CharField(max_length=18, blank=True, null=True)
    cedcod = models.CharField(max_length=8, blank=True, null=True)
    cedagenc = models.CharField(max_length=4, blank=True, null=True)
    cedagd = models.CharField(max_length=1, blank=True, null=True)
    cedconta = models.CharField(max_length=10, blank=True, null=True)
    cedctdig = models.CharField(max_length=1, blank=True, null=True)
    oper = models.CharField(max_length=3, blank=True, null=True)
    carteira = models.CharField(max_length=2, blank=True, null=True)
    variacao = models.CharField(max_length=2, blank=True, null=True)
    idbolesp = models.PositiveIntegerField()
    instr1 = models.CharField(max_length=80, blank=True, null=True)
    instr2 = models.CharField(max_length=80, blank=True, null=True)
    instr3 = models.CharField(max_length=80, blank=True, null=True)
    idmoeda = models.PositiveIntegerField()
    taxa = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    gerente = models.CharField(max_length=25, blank=True, null=True)
    tel = models.CharField(max_length=14, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contasfin'
        unique_together = (('instit', 'tipo', 'cedagenc', 'cedconta'),)


class Contasmv(models.Model):
    id = models.IntegerField(primary_key=True)
    instit = models.PositiveIntegerField()
    idctfin = models.PositiveIntegerField()
    idsecao = models.PositiveIntegerField()
    tipo = models.PositiveIntegerField()
    descr = models.CharField(max_length=50, blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    dat = models.DateTimeField(blank=True, null=True)
    idorigem = models.PositiveIntegerField()
    usuario = models.PositiveIntegerField()
    mcx = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'contasmv'


class Contaspg(models.Model):
    id = models.IntegerField(primary_key=True)
    instit = models.PositiveIntegerField(blank=True, null=True)
    sit = models.CharField(max_length=1)
    origem = models.PositiveIntegerField()
    fav = models.CharField(max_length=40, blank=True, null=True)
    doc = models.CharField(max_length=35, blank=True, null=True)
    descr = models.CharField(max_length=40)
    idsecdsp = models.PositiveIntegerField()
    emissao = models.DateTimeField()
    venc = models.DateTimeField()
    valdoc = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    dtpg = models.DateTimeField(blank=True, null=True)
    valor = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    valpg = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    pago = models.PositiveIntegerField(blank=True, null=True)
    idsecfav = models.PositiveIntegerField()
    idctfin = models.PositiveIntegerField()
    usuario = models.PositiveIntegerField(blank=True, null=True)
    idccx = models.PositiveIntegerField()
    obs = models.CharField(max_length=30, blank=True, null=True)
    acresc = models.DecimalField(max_digits=10, decimal_places=2)
    vdesc = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'contaspg'


class Contasrc(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    sit = models.PositiveIntegerField()
    dat = models.DateTimeField()
    tcli = models.PositiveIntegerField()
    ccli = models.PositiveIntegerField(blank=True, null=True)
    cli = models.CharField(max_length=50)
    idped = models.PositiveIntegerField()
    instit = models.PositiveIntegerField()
    obs = models.CharField(max_length=30)
    vencim = models.DateTimeField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    pago = models.PositiveIntegerField()
    dtpg = models.DateTimeField(blank=True, null=True)
    valpg = models.DecimalField(max_digits=10, decimal_places=2)
    idformpg = models.PositiveIntegerField()
    idccx = models.PositiveIntegerField()
    identpg = models.CharField(max_length=40, blank=True, null=True)
    idsecao = models.PositiveIntegerField()
    codusu = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'contasrc'


class Devpro(models.Model):
    # Field name made lowercase.
    id = models.PositiveIntegerField(db_column='Id', primary_key=True)
    forn = models.PositiveIntegerField(blank=True, null=True)
    valor = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    gera_crd = models.PositiveIntegerField(blank=True, null=True)
    qtd = models.DecimalField(
        max_digits=9, decimal_places=3, blank=True, null=True)
    dtz = models.DateTimeField(blank=True, null=True)
    usuario = models.PositiveIntegerField()
    loja = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'devpro'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AccountAccount, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ECarousel(models.Model):
    id_e_carousel = models.AutoField(primary_key=True)
    e_carouselordem = models.IntegerField(blank=True, null=True)
    imagem = models.CharField(max_length=100)
    status = models.IntegerField(blank=True, null=True)
    data_de_criacao = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_carousel'


class EPermissao(models.Model):
    ide_permissao = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'e_permissao'


class EProdutoDestaque(models.Model):
    # Field name made lowercase.
    id_e_produtodest = models.AutoField(
        db_column='id_e_produtoDest', primary_key=True)
    id_produto_fk = models.IntegerField()
    status = models.IntegerField()
    data_de_criacao = models.DateTimeField()
    data_atualizacao = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_produto_destaque'


class EUsuario(models.Model):
    id_e_usuario = models.AutoField(primary_key=True)
    id_e_permissao_fk = models.ForeignKey(
        EPermissao, models.DO_NOTHING, db_column='id_e_permissao_fk')
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    data_de_criacao = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_usuario'


class Ecaixa(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    instit = models.PositiveIntegerField()
    idctrec = models.PositiveIntegerField()
    dat = models.DateTimeField()
    val = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    idfpgt = models.PositiveIntegerField()
    idccx = models.PositiveIntegerField()
    ref = models.CharField(max_length=60)
    usuario = models.PositiveIntegerField()
    local = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'ecaixa'
        unique_together = (('id', 'dat', 'ref'),)


class Enderecos(models.Model):
    id_enderecos = models.AutoField(primary_key=True)
    situacao = models.IntegerField()
    origem = models.PositiveIntegerField()
    id_pessoa_cod_fk = models.IntegerField()
    endtip = models.PositiveIntegerField()
    rua = models.CharField(max_length=100, blank=True, null=True)
    numero = models.CharField(max_length=8, blank=True, null=True)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=40, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    cidade = models.CharField(max_length=20, blank=True, null=True)
    estado_endereco = models.CharField(max_length=3, blank=True, null=True)
    data_criacao = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enderecos'


class Fabpro(models.Model):
    instit = models.PositiveIntegerField()
    marca = models.CharField(max_length=25)
    fabr = models.CharField(max_length=40, blank=True, null=True)
    data_criacao = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fabpro'


class Feriados(models.Model):
    # Field name made lowercase.
    id = models.IntegerField(db_column='Id', primary_key=True)
    data = models.DateTimeField()
    ativo = models.PositiveIntegerField()
    descr = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feriados'


class Folhapg(models.Model):
    id = models.IntegerField(primary_key=True)
    instit = models.PositiveIntegerField()
    data = models.DateTimeField(blank=True, null=True)
    tipo = models.PositiveIntegerField()
    mcxini = models.PositiveIntegerField(blank=True, null=True)
    mcxfim = models.PositiveIntegerField(blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'folhapg'


class Formpg(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    instit = models.PositiveIntegerField()
    sit = models.PositiveIntegerField()
    nome = models.CharField(max_length=25)
    edit = models.PositiveIntegerField()
    receb = models.PositiveIntegerField()
    desat = models.PositiveIntegerField()
    caixa = models.PositiveIntegerField()
    fiscal = models.PositiveIntegerField()
    idsecao = models.PositiveIntegerField()
    obs = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'formpg'


class Fotos(models.Model):
    id_foto = models.AutoField(primary_key=True)
    id_instituicao = models.ForeignKey(
        'Instit', models.DO_NOTHING, db_column='id_instituicao')
    id_produto = models.ForeignKey(
        'Produtos', models.DO_NOTHING, db_column='id_produto')
    nome_arquivo = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fotos'


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

    class Meta:
        managed = False
        db_table = 'funcio'
        unique_together = (('instit', 'idpescod'), ('instit', 'nome'),)


class Gcom(models.Model):
    # Field name made lowercase.
    id = models.IntegerField(db_column='Id', primary_key=True)
    descr = models.CharField(max_length=50, blank=True, null=True)
    valor = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gcom'


class GcomBtns(models.Model):
    # Field name made lowercase.
    id = models.IntegerField(db_column='Id', primary_key=True)
    ativo = models.PositiveIntegerField()
    ordem = models.PositiveIntegerField()
    tipo = models.PositiveIntegerField()
    rotulo = models.CharField(max_length=50, blank=True, null=True)
    nome = models.CharField(max_length=10, blank=True, null=True)
    action = models.CharField(max_length=40, blank=True, null=True)
    img = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gcom_btns'


class GcomMenu(models.Model):
    # Field name made lowercase.
    id = models.IntegerField(db_column='Id', primary_key=True)
    ativo = models.PositiveIntegerField()
    ordem = models.PositiveIntegerField()
    tipo = models.PositiveIntegerField()
    rotulo = models.CharField(max_length=50, blank=True, null=True)
    nome = models.CharField(max_length=10, blank=True, null=True)
    action = models.CharField(max_length=40, blank=True, null=True)
    img = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gcom_menu'


class Imprfisc(models.Model):
    # Field name made lowercase.
    id = models.IntegerField(db_column='Id', primary_key=True)
    loja = models.PositiveIntegerField()
    nome = models.CharField(max_length=20)
    monitor = models.CharField(max_length=15)
    status = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'imprfisc'


class Imprfiscfila(models.Model):
    # Field name made lowercase.
    id = models.IntegerField(db_column='Id', primary_key=True)
    fila = models.IntegerField()
    data = models.DateTimeField()
    texto = models.TextField()

    class Meta:
        managed = False
        db_table = 'imprfiscfila'


class Infpatrim(models.Model):
    # Field name made lowercase.
    id = models.IntegerField(db_column='Id', primary_key=True)
    deleted = models.PositiveIntegerField()
    idpescod = models.PositiveIntegerField()
    tipo = models.PositiveIntegerField()
    registro = models.CharField(max_length=20, blank=True, null=True)
    descr = models.CharField(max_length=80)
    valor = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    debito = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    prestacao = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    data = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'infpatrim'


class Instit(models.Model):
    id_instituicao = models.IntegerField(primary_key=True)
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
    cidade = models.PositiveIntegerField()
    uf = models.PositiveIntegerField()
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


class ItCcx(models.Model):
    # Field name made lowercase.
    id = models.IntegerField(db_column='Id', primary_key=True)
    idccx = models.PositiveIntegerField()
    tipo = models.PositiveIntegerField()
    descr = models.CharField(max_length=30, blank=True, null=True)
    idfpgt = models.PositiveIntegerField()
    val = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'it_ccx'


class ItDev(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    iddev = models.PositiveIntegerField(blank=True, null=True)
    idprod = models.PositiveIntegerField()
    codprod = models.PositiveIntegerField(blank=True, null=True)
    forn = models.PositiveIntegerField(blank=True, null=True)
    qtd = models.DecimalField(max_digits=9, decimal_places=3)
    custo = models.DecimalField(max_digits=9, decimal_places=2)
    local = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'it_dev'


class ItLoc(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    loc = models.PositiveIntegerField()
    item = models.PositiveIntegerField()
    cpro = models.PositiveIntegerField(blank=True, null=True)
    prod = models.CharField(max_length=50)
    und = models.CharField(max_length=2)
    qtd = models.DecimalField(max_digits=10, decimal_places=3)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    valtab = models.DecimalField(max_digits=10, decimal_places=2)
    dtloc = models.DateTimeField(blank=True, null=True)
    dtdev = models.DateTimeField(blank=True, null=True)
    entr = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'it_loc'


class ItLocDev(models.Model):
    # Field name made lowercase.
    id = models.IntegerField(db_column='Id', primary_key=True)
    identr = models.PositiveIntegerField()
    qtd = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True)
    dtentr = models.DateTimeField(blank=True, null=True)
    dtdev = models.DateTimeField(blank=True, null=True)
    val = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    idloc = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'it_loc_dev'


class ItLocEnt(models.Model):
    # Field name made lowercase.
    id = models.IntegerField(db_column='Id', primary_key=True)
    idloc = models.PositiveIntegerField()
    prod = models.CharField(max_length=40, blank=True, null=True)
    qtd = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True)
    dtentr = models.DateTimeField(blank=True, null=True)
    dev = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True)
    valor = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    dtdev = models.DateTimeField(blank=True, null=True)
    cprod = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'it_loc_ent'


class ItOrcam(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    idorigem = models.PositiveIntegerField()
    item = models.PositiveIntegerField()
    cpro = models.PositiveIntegerField(blank=True, null=True)
    prod = models.CharField(max_length=50)
    und = models.CharField(max_length=2)
    qtd = models.DecimalField(max_digits=10, decimal_places=3)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    valtab = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'it_orcam'


class ItPed(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    idorigem = models.PositiveIntegerField()
    cpro = models.PositiveIntegerField(blank=True, null=True)
    prod = models.CharField(max_length=50)
    und = models.CharField(max_length=2)
    qtd = models.DecimalField(max_digits=10, decimal_places=3)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    valtab = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'it_ped'


class ItRec(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    instit = models.PositiveIntegerField()
    idrec = models.PositiveIntegerField(blank=True, null=True)
    idprod = models.PositiveIntegerField(blank=True, null=True)
    codprod = models.PositiveIntegerField()
    idpescod = models.PositiveIntegerField(blank=True, null=True)
    nf = models.DecimalField(max_digits=9, decimal_places=3)
    frente = models.DecimalField(max_digits=9, decimal_places=3)
    dep = models.DecimalField(max_digits=9, decimal_places=3)
    compra = models.DecimalField(max_digits=9, decimal_places=2)
    icms = models.PositiveIntegerField()
    ipi = models.DecimalField(max_digits=6, decimal_places=2)
    frete = models.DecimalField(max_digits=9, decimal_places=2)
    custo = models.DecimalField(max_digits=9, decimal_places=2)
    lucro = models.DecimalField(max_digits=7, decimal_places=2)
    venda1 = models.DecimalField(max_digits=9, decimal_places=2)
    venda2 = models.DecimalField(max_digits=9, decimal_places=2)
    venda3 = models.DecimalField(max_digits=9, decimal_places=2)
    data = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'it_rec'


class ItTrf(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    trf_itf = models.CharField(max_length=8)
    cpr_itf = models.CharField(max_length=6)
    pro_itf = models.CharField(max_length=40)
    und_itf = models.CharField(max_length=2)
    qtd_itf = models.DecimalField(max_digits=9, decimal_places=2)
    val_itf = models.DecimalField(max_digits=9, decimal_places=2)
    vtb_itf = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'it_trf'
        unique_together = (('id', 'trf_itf'),)


class Locs(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    dat = models.DateTimeField()
    tcli = models.PositiveIntegerField()
    ccli = models.PositiveIntegerField()
    cli = models.CharField(max_length=50)
    tend = models.PositiveIntegerField()
    end = models.CharField(max_length=40, blank=True, null=True)
    endnum = models.CharField(max_length=6, blank=True, null=True)
    endcompl = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=30, blank=True, null=True)
    cidade = models.CharField(max_length=30, blank=True, null=True)
    uf = models.PositiveIntegerField()
    tel1 = models.CharField(max_length=13, blank=True, null=True)
    tel2 = models.CharField(max_length=13, blank=True, null=True)
    ptref = models.CharField(max_length=30, blank=True, null=True)
    tot = models.DecimalField(max_digits=10, decimal_places=2)
    vacr = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    vdesc = models.DecimalField(max_digits=10, decimal_places=2)
    totpg = models.DecimalField(max_digits=10, decimal_places=2)
    codusu = models.PositiveIntegerField()
    msg = models.CharField(max_length=30, blank=True, null=True)
    loja = models.PositiveIntegerField()
    situacao = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'locs'


class Logradouros(models.Model):
    # Field name made lowercase.
    id = models.IntegerField(db_column='Id', primary_key=True)
    logr = models.CharField(max_length=20, blank=True, null=True)
    abrev = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logradouros'


class Mails(models.Model):
    id_mails = models.AutoField(primary_key=True)
    id_pessoa_cod_fk = models.IntegerField()
    situacao = models.IntegerField()
    email = models.CharField(max_length=45, blank=True, null=True)
    data_criacao = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mails'


class Moedas(models.Model):
    id = models.IntegerField(primary_key=True)
    moeda = models.CharField(max_length=20)
    simbolo = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moedas'


class Municipios(models.Model):
    id_municipios = models.IntegerField(primary_key=True)
    descr = models.CharField(max_length=35)
    uf_sigla = models.CharField(max_length=2)
    coduf = models.PositiveIntegerField()
    ibge = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'municipios'


class MunicipiosIbge(models.Model):
    id = models.IntegerField(blank=True, null=True)
    codigo_uf = models.IntegerField(blank=True, null=True)
    nome_uf = models.TextField(blank=True, null=True)
    sigla_uf = models.TextField(blank=True, null=True)
    codigo_municipio = models.IntegerField(blank=True, null=True)
    nome_municipio = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'municipios_ibge'


class Nfserv(models.Model):
    # Field name made lowercase.
    id = models.IntegerField(db_column='Id', primary_key=True)
    instit = models.PositiveIntegerField(blank=True, null=True)
    sit = models.PositiveIntegerField()
    tcli = models.PositiveIntegerField()
    codcli = models.PositiveIntegerField(blank=True, null=True)
    cnpjcli = models.CharField(max_length=18, blank=True, null=True)
    cli = models.CharField(max_length=50, blank=True, null=True)
    tend = models.PositiveIntegerField()
    end = models.CharField(max_length=40, blank=True, null=True)
    endnum = models.CharField(max_length=6, blank=True, null=True)
    endcompl = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=30, blank=True, null=True)
    cidade = models.PositiveIntegerField()
    email = models.CharField(max_length=50, blank=True, null=True)
    numnf = models.PositiveIntegerField(blank=True, null=True)
    emissao = models.DateTimeField(blank=True, null=True)
    compet = models.CharField(max_length=7, blank=True, null=True)
    local = models.PositiveIntegerField()
    nfsubst = models.PositiveIntegerField()
    rps = models.CharField(max_length=15, blank=True, null=True)
    verif = models.CharField(max_length=15, blank=True, null=True)
    descr = models.CharField(max_length=255, blank=True, null=True)
    cnae = models.PositiveIntegerField()
    obra = models.CharField(max_length=15, blank=True, null=True)
    art = models.CharField(max_length=15, blank=True, null=True)
    pis = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    cofins = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    ir = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    inss = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    csll = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    valor = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    desci = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    descc = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    issqn = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True, null=True)
    retid = models.PositiveIntegerField()
    quit = models.PositiveIntegerField(blank=True, null=True)
    dtquit = models.DateTimeField(blank=True, null=True)
    valpg = models.DecimalField(max_digits=10, decimal_places=2)
    fpgto = models.PositiveIntegerField()
    idconta = models.PositiveIntegerField(blank=True, null=True)
    usuario = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'nfserv'
        unique_together = (('instit', 'cnpjcli', 'numnf', 'emissao'),)


class Obs(models.Model):
    # Field name made lowercase.
    id = models.IntegerField(db_column='Id', primary_key=True)
    deleted = models.PositiveIntegerField()
    idpescod = models.PositiveIntegerField()
    data = models.DateTimeField()
    obs = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'obs'


class Orcamentos(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    sit = models.PositiveIntegerField()
    instit = models.PositiveIntegerField()
    codorc = models.PositiveIntegerField()
    dat = models.DateTimeField()
    tven = models.PositiveIntegerField()
    tcli = models.PositiveIntegerField()
    ccli = models.PositiveIntegerField()
    cli = models.CharField(max_length=50)
    tend = models.PositiveIntegerField()
    end = models.CharField(max_length=40, blank=True, null=True)
    endnum = models.CharField(max_length=6, blank=True, null=True)
    endcompl = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=30, blank=True, null=True)
    cidade = models.CharField(max_length=30, blank=True, null=True)
    uf = models.PositiveIntegerField()
    cep = models.CharField(max_length=10, blank=True, null=True)
    tel1 = models.CharField(max_length=14, blank=True, null=True)
    tel2 = models.CharField(max_length=14, blank=True, null=True)
    ptref = models.CharField(max_length=30, blank=True, null=True)
    tot = models.DecimalField(max_digits=10, decimal_places=2)
    vacr = models.DecimalField(max_digits=6, decimal_places=2)
    vdesc = models.DecimalField(max_digits=6, decimal_places=2)
    totpg = models.DecimalField(max_digits=10, decimal_places=2)
    codusu = models.PositiveIntegerField()
    msg = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orcamentos'
        unique_together = (('instit', 'codorc'),)


class Pedidos(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    sit = models.PositiveIntegerField()
    instit = models.PositiveIntegerField()
    codped = models.PositiveIntegerField()
    dat = models.DateTimeField()
    tven = models.PositiveIntegerField()
    tcli = models.PositiveIntegerField()
    ccli = models.PositiveIntegerField()
    cli = models.CharField(max_length=50)
    tend = models.PositiveIntegerField()
    end = models.CharField(max_length=40, blank=True, null=True)
    endnum = models.CharField(max_length=6, blank=True, null=True)
    endcompl = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=30, blank=True, null=True)
    cidade = models.CharField(max_length=35, blank=True, null=True)
    uf = models.PositiveIntegerField()
    cep = models.CharField(max_length=10, blank=True, null=True)
    tel1 = models.CharField(max_length=14, blank=True, null=True)
    tel2 = models.CharField(max_length=13, blank=True, null=True)
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
        unique_together = (('instit', 'codped'),)


class Permissao(models.Model):
    id_permissao = models.IntegerField(primary_key=True)
    descricao_permissao = models.CharField(
        max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissao'


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


class Pesjur(models.Model):
    id_pessoa_juridica = models.AutoField(primary_key=True)
    id_pessoa_cod_fk = models.IntegerField()
    fantasia = models.CharField(max_length=50, blank=True, null=True)
    ramo = models.CharField(max_length=255, blank=True, null=True)
    inscricao_estadual = models.CharField(max_length=20, blank=True, null=True)
    inscricao_municipal = models.CharField(
        max_length=20, blank=True, null=True)
    tipo_empresa = models.CharField(max_length=100, blank=True, null=True)
    capsocial = models.DecimalField(max_digits=15, decimal_places=2)
    faturamento = models.DecimalField(max_digits=15, decimal_places=2)
    tribut = models.PositiveIntegerField()
    contato = models.CharField(max_length=25, blank=True, null=True)
    data_abertura = models.DateField()
    data_criacao = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pesjur'


class PesjurSoc(models.Model):
    # Field name made lowercase.
    id = models.IntegerField(db_column='Id', primary_key=True)
    deleted = models.PositiveIntegerField()
    idpescod = models.PositiveIntegerField()
    nome = models.CharField(max_length=60, blank=True, null=True)
    funcao = models.CharField(max_length=30, blank=True, null=True)
    cotas = models.DecimalField(max_digits=9, decimal_places=5)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    data = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pesjur_soc'


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


class Produtos(models.Model):
    instit = models.PositiveIntegerField()
    matriz = models.PositiveIntegerField(blank=True, null=True)
    codprod = models.PositiveIntegerField()
    nome = models.CharField(max_length=45)
    ativo = models.PositiveIntegerField()
    descr = models.CharField(max_length=50, blank=True, null=True)
    descres = models.CharField(max_length=25, blank=True, null=True)
    und = models.IntegerField()
    grupo = models.PositiveIntegerField(blank=True, null=True)
    tam = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    larg = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    alt = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    cubag = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    peso_bruto = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    peso_liquido = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    codbarra = models.CharField(max_length=25, blank=True, null=True)
    fabr = models.IntegerField(blank=True, null=True)
    forn = models.PositiveIntegerField(blank=True, null=True)
    caract = models.CharField(max_length=50, blank=True, null=True)
    ncm = models.CharField(max_length=20, blank=True, null=True)
    cest = models.CharField(max_length=20, blank=True, null=True)
    bxest = models.PositiveIntegerField()
    minimo = models.PositiveIntegerField(blank=True, null=True)
    fiscal = models.IntegerField(blank=True, null=True)
    frente = models.IntegerField(blank=True, null=True)
    deposito = models.IntegerField(blank=True, null=True)
    compra = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    frete = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    ipi = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    aliq = models.PositiveIntegerField(blank=True, null=True)
    custo = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    lucro = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    prvenda1 = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    prvenda2 = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    prvenda3 = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    locavel = models.PositiveIntegerField()
    prloc = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    vdatac = models.PositiveIntegerField()
    qtdatac = models.PositiveIntegerField(blank=True, null=True)
    pratac = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    local = models.CharField(max_length=50, blank=True, null=True)
    desnf = models.CharField(max_length=40, blank=True, null=True)
    foto = models.CharField(max_length=25)
    img_bites = models.PositiveIntegerField(blank=True, null=True)
    datatz = models.DateTimeField(blank=True, null=True)
    usuatz = models.PositiveIntegerField()
    deletado = models.IntegerField()
    data_criacao = models.DateTimeField()
    data_atualizacao = models.DateTimeField(blank=True, null=True)
    ean_tributavel = models.CharField(max_length=45, blank=True, null=True)
    ex_tipi = models.CharField(max_length=45, blank=True, null=True)
    estoque_maximo = models.IntegerField(blank=True, null=True)
    qtd_tributavel = models.IntegerField(blank=True, null=True)
    valor_uni_tributavel = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    qtd_comercial = models.IntegerField(blank=True, null=True)
    valor_uni_comercial = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    icms_situacao_tributaria = models.IntegerField(blank=True, null=True)
    icms_origem = models.IntegerField(blank=True, null=True)
    id_pis = models.IntegerField(blank=True, null=True)
    id_cofins = models.IntegerField(blank=True, null=True)
    id_ipi = models.IntegerField(blank=True, null=True)
    status_destaque = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'produtos'
        unique_together = (('codprod', 'instit'),)


class Recpro(models.Model):
    # Field name made lowercase.
    id = models.PositiveIntegerField(db_column='Id', primary_key=True)
    instit = models.PositiveIntegerField()
    idpescod = models.PositiveIntegerField(blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    valor = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    qtd = models.DecimalField(
        max_digits=9, decimal_places=3, blank=True, null=True)
    g_con = models.PositiveIntegerField(blank=True, null=True)
    p_dat = models.DateTimeField(blank=True, null=True)
    p_num = models.CharField(max_length=20, blank=True, null=True)
    p_val = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    p_ven = models.CharField(max_length=20, blank=True, null=True)
    n_dat = models.DateTimeField(blank=True, null=True)
    n_num = models.CharField(max_length=20, blank=True, null=True)
    n_val = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    dtz = models.DateTimeField(blank=True, null=True)
    usuario = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recpro'


class Refbanco(models.Model):
    id_banco = models.AutoField(primary_key=True)
    id_pessoa_cod_fk = models.IntegerField()
    id_bancos_fk = models.IntegerField()
    situacao = models.IntegerField()
    agencia = models.CharField(max_length=6, blank=True, null=True)
    conta = models.CharField(max_length=10, blank=True, null=True)
    abertura = models.DateTimeField(blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    data_criacao = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'refbanco'


class Referencias(models.Model):
    id_referencia = models.AutoField(primary_key=True)
    id_pessoa_cod_fk = models.IntegerField()
    situacao = models.IntegerField()
    tipo = models.CharField(max_length=15, blank=True, null=True)
    nome = models.CharField(max_length=50, blank=True, null=True)
    tel = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    data_criacao = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'referencias'


class Rotinas(models.Model):
    # Field name made lowercase.
    id = models.IntegerField(db_column='Id', primary_key=True)
    descr = models.CharField(max_length=40)
    sit = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'rotinas'


class Sac(models.Model):
    # Field name made lowercase.
    id = models.IntegerField(db_column='Id', primary_key=True)
    cliente = models.CharField(max_length=50, blank=True, null=True)
    ref = models.CharField(max_length=20, blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    valor = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    contato = models.CharField(max_length=150, blank=True, null=True)
    atendente = models.CharField(max_length=20, blank=True, null=True)
    instit = models.PositiveIntegerField(blank=True, null=True)
    dtsac = models.DateTimeField(blank=True, null=True)
    usuario = models.CharField(max_length=20, blank=True, null=True)
    resultado = models.PositiveIntegerField(blank=True, null=True)
    obs = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sac'


class Sangria(models.Model):
    # Field name made lowercase.
    id = models.IntegerField(db_column='Id', primary_key=True)
    instit = models.PositiveIntegerField()
    dat = models.DateTimeField()
    emi = models.CharField(max_length=40)
    obs = models.CharField(max_length=40, blank=True, null=True)
    val = models.DecimalField(max_digits=10, decimal_places=2)
    codusu = models.PositiveIntegerField(blank=True, null=True)
    idccaixa = models.PositiveIntegerField()
    idformpg = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'sangria'


class Secoes(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    instit = models.PositiveIntegerField()
    codconta = models.CharField(max_length=20)
    ativo = models.PositiveIntegerField()
    secao = models.CharField(max_length=60)
    tipocod = models.PositiveIntegerField()
    tipoconta = models.PositiveIntegerField()
    reduzido = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'secoes'


class TableTests(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'table_tests'


class Telefones(models.Model):
    id_telefone = models.AutoField(primary_key=True)
    id_pessoa_cod_fk = models.IntegerField()
    situacao = models.IntegerField()
    tel = models.CharField(max_length=20, blank=True, null=True)
    data_criacao = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'telefones'


class Temp(models.Model):
    # Field name made lowercase.
    id = models.IntegerField(db_column='Id', primary_key=True)
    v1 = models.CharField(max_length=5, blank=True, null=True)
    v2 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp'


class TransfI(models.Model):
    id = models.IntegerField(primary_key=True)
    prod = models.PositiveIntegerField()
    loja = models.PositiveIntegerField()
    frente = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True)
    deposito = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True)
    dat = models.DateTimeField()
    user = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'transf_i'


class Unidades(models.Model):
    instit = models.PositiveIntegerField()
    ativo = models.PositiveIntegerField()
    und = models.CharField(max_length=2)
    descr = models.CharField(max_length=12)
    tipo = models.PositiveIntegerField()
    data_criacao = models.DateTimeField()
    data_atualizacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidades'


class UserSenha(models.Model):
    id = models.IntegerField(db_column='Id')  # Field name made lowercase.
    iduser = models.PositiveIntegerField(blank=True, null=True)
    senha = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_senha'


class Users(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    idpescod = models.PositiveIntegerField()
    instit = models.PositiveIntegerField()
    ativo = models.PositiveIntegerField()
    idgrp = models.PositiveIntegerField()
    login = models.CharField(unique=True, max_length=25)
    nome = models.CharField(max_length=25, blank=True, null=True)
    numlog = models.PositiveIntegerField()
    senha = models.CharField(max_length=20)
    acess = models.CharField(max_length=255)
    desenv = models.PositiveIntegerField()
    datsenha = models.DateTimeField(blank=True, null=True)
    data_criacao = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)
    data_de_exclusao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Users2(models.Model):
    id_usuario = models.IntegerField()
    nome = models.CharField(max_length=255)
    identificacao = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    id_permissao_fk = models.IntegerField()
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    situacao = models.IntegerField()
    data_criacao = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)
    data_de_exclusao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_2'


class UsersGrp(models.Model):
    id_grupo = models.AutoField(primary_key=True)
    grupo = models.CharField(max_length=15)
    instit = models.IntegerField()
    acess = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_grp'
        unique_together = (('instit', 'grupo'),)


class Vales(models.Model):
    id = models.IntegerField(db_column='Id')  # Field name made lowercase.
    instit = models.PositiveIntegerField()
    dat = models.DateTimeField()
    emi = models.CharField(max_length=40)
    descr = models.CharField(max_length=50)
    val = models.DecimalField(max_digits=10, decimal_places=2)
    usu = models.PositiveIntegerField()
    idccx = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'vales'


class Xml(models.Model):
    id_xml = models.AutoField(primary_key=True)
    instituicao = models.IntegerField()
    nome_arquivo = models.CharField(max_length=60)
    nome_emitente = models.CharField(max_length=100, blank=True, null=True)
    nome_destinatario = models.CharField(max_length=100, blank=True, null=True)
    numero_nota = models.CharField(max_length=45, blank=True, null=True)
    data_criacao = models.DateTimeField()
    data_atualizacao = models.DateTimeField(blank=True, null=True)
    deletado = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xml'
