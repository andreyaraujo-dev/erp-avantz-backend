from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status
from datetime import datetime
from django.utils import timezone
from django.db import transaction

from users.authentication import SafeJWTAuthentication
from .serializers import PescodSerializer
from .models import Pescod
from pessoa_fisica.models import Pesfis
from pessoa_fisica.serializers import PessoaFisicaSerializers
from pessoa_juridica.models import Pesjur
from pessoa_juridica.serializers import PessoaJuridicaSerializer
from enderecos.models import Enderecos
from enderecos.serializers import EnderecosSerializers
from telefones.models import Telefones
from telefones.serializers import TelefoneSerializers
from emails.models import Mails
from emails.serializers import EmailSerializers
from referencias.models import Referencias
from referencias.serializers import ReferenciasSerializers
from ref_bancarias.models import Refbanco
from ref_bancarias.serializers import RefBancoSerializers


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def index(request):
    id_institution = request.user.instit_id
    try:
        persons = Pescod.objects.filter(
            id_instituicao_fk=id_institution, sit=2)
        persons_serialized = PescodSerializer(persons, many=True)
        return Response(persons_serialized.data)
    except:
        raise exceptions.APIException


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def find_physical_persons(request):
    id_institution = request.user.instit_id
    try:
        persons = Pescod.objects.filter(
            id_instituicao_fk=id_institution, sit=2, tipo=1)
        persons_serialized = PescodSerializer(persons, many=True)
        return Response(persons_serialized.data)
    except:
        raise exceptions.APIException


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def find_legal_persons(request):
    id_institution = request.user.instit_id
    try:
        persons = Pescod.objects.filter(
            id_instituicao_fk=id_institution, sit=2, tipo=2)
        persons_serialized = PescodSerializer(persons, many=True)
        return Response(persons_serialized.data)
    except:
        raise exceptions.APIException


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
@transaction.atomic
def store_person_physical(request):
    id_institution = request.user.instit_id
    cpf = request.data.get('personCPF')
    """  
    FIND CPF ON DATABASE. IF EXIST, NO REGISTER AND RETURN
    """
    person = Pescod.objects.filter(
        id_instituicao_fk=id_institution, cpfcnpj=cpf, sit=2)
    if person:
        return Response({'detail': 'Já existe um registro ativo com este CPF. Por favor revise os dados.'}, status=status.HTTP_400_BAD_REQUEST)

    """  
    REGISTER PESCOD
    """
    provider = request.data.get('personIsProvider')
    name = request.data.get('personName')
    person_photo = request.data.get('personPhoto')
    person_limit = request.data.get('personLimit')
    person_balance = request.data.get('personBalance')

    try:
        person = Pescod(id_instituicao_fk=id_institution, tipo=1, sit=1, forn=provider, cpfcnpj=cpf,
                        nomeorrazaosocial=name, foto=person_photo, img_bites=0, limite=person_limit, saldo=person_balance, data_criacao=timezone.now())
        person.save()
    except:
        raise exceptions.APIException(
            'Não foi possível cadastrar o registro da pessoa. Verifique os dados inseridos.')

    """  
    REGISTER PHYSICAL PERSON
    """
    person_registred_id = person.id_pessoa_cod
    identity = request.data.get('personIdentity')
    issuer_identity = request.data.get('issuerIdentity')
    id_municipality = request.data.get('personMunicipality')
    id_uf = request.data.get('personUF')
    date_of_birth = request.data.get('personBirth')
    treatment = request.data.get('personTreatment')
    nickname = request.data.get('personNickname')
    sex = request.data.get('personSex')
    father = request.data.get('personFather')
    mother = request.data.get('personMother')
    profession = request.data.get('personProfession')
    ctps = request.data.get('ctps')
    salary = request.data.get('personSalary')
    company = request.data.get('personCompany')
    company_responsible = request.data.get('companyResponsible')
    company_cnpj = request.data.get('companyCnpj')
    state_registration = request.data.get('stateRegistrationCompany')
    municipal_registration = request.data.get('municipalRegistrationCompany')
    company_adress = request.data.get('companyAdress')
    other_income = request.data.get('otherIncome')
    income_value = request.data.get('incomeValue')
    irpf = request.data.get('irpf')
    marital_status = request.data.get('maritalStatus')
    dependents = request.data.get('personDependents')
    pension = request.data.get('pension')
    spouse = request.data.get('spouse')
    spouse_cpf = request.data.get('spouseCpf')
    spouse_profession = request.data.get('spouseProfession')
    spouse_company = request.data.get('spouseCompany')
    spouse_income = request.data.get('spouseIncome')
    spouse_phone = request.data.get('spousePhone')
    spouse_mail = request.data.get('spouseMail')

    person_physical = Pesfis(id_pessoa_cod_fk=person_registred_id, identidade=identity, emissor_identidade=issuer_identity, id_municipio_fk=id_municipality,
                             id_uf_municipio_fk=id_uf, data_de_nascimento=date_of_birth, tratam=treatment, apelido=nickname, sexo=sex, pai=father, mae=mother,
                             profissao=profession, ctps=ctps, salario=salary, empresa=company, resp=company_responsible, cnpj=company_cnpj, iest=state_registration,
                             imun=municipal_registration, emprend=company_adress, orendas=other_income, vrendas=income_value, irpf=irpf, estcivil=marital_status,
                             depend=dependents, pensao=pension, conjuge=spouse, cpfconj=spouse_cpf, profconj=spouse_profession, emprconj=spouse_company,
                             rendaconj=spouse_income, telconj=spouse_phone, mailconj=spouse_mail, data_criacao=timezone.now())

    try:
        person_physical.save()
    except:
        raise exceptions.APIException(
            'Não foi possível cadastrar os dados de pessoa física')

    """ 
    REGISTER ADRESS
    """
    adresses_array = request.data.get('adresses')
    for adress in adresses_array:
        try:
            adress_registred = Enderecos(situacao=1, origem=1, id_pessoa_cod_fk=person_registred_id, endtip=1, rua=adress['street'],
                                         numero=adress['numberHouse'], complemento=adress['complement'], bairro=adress['neighborhood'],
                                         cep=adress['zipCode'], cidade=adress['city'], estado_endereco=adress['stateAdress'], data_criacao=timezone.now())
            adress_registred.save()
        except:
            raise exceptions.APIException(
                'Não foi possível salvar todos os dados de endereço')

    """  
    REGISTER PHONE
    """
    phones_array = request.data.get('phones')
    for phone in phones_array:
        try:
            phone_registered = Telefones(id_pessoa_cod_fk=person_registred_id,
                                         situacao=1, tel=phone['phoneNumber'], data_criacao=timezone.now())
            phone_registered.save()
        except:
            raise exceptions.APIException(
                'Não foi possível salvar os dados de contato')

    """ 
    REGISTER MAIL    
    """
    mails_array = request.data.get('mails')
    for mail in mails_array:
        try:
            mail_registered = Mails(
                id_pessoa_cod_fk=person_registred_id, situacao=1, email=mail['userMail'], data_criacao=timezone.now())
            mail_registered.save()
        except:
            raise exceptions.APIException(
                'Não foi possível salvar os dados de email')

    """  
    REGISTER REFERENCES
    """
    references_array = request.data.get('personReferences')
    for reference in references_array:
        try:
            references_registered = Referencias(id_pessoa_cod_fk=person_registred_id,
                                                situacao=1, tipo=reference['referenceType'], nome=reference['referenceName'],
                                                tel=reference['referencePhone'], endereco=reference['referenceAdress'], data_criacao=timezone.now())
            references_registered.save()
        except:
            raise exceptions.APIException(
                'Não foi possível salvar os dados da referência')

    """  
    REGISTER BANK
    """
    banking_references_array = request.data.get('bankingReferences')
    for banking_reference in banking_references_array:
        try:
            banking_reference_registred = Refbanco(id_pessoa_cod_fk=person_registred_id, id_bancos_fk=banking_reference['idBanking'], situacao=1,
                                                   agencia=banking_reference['agency'], conta=banking_reference['account'],
                                                   abertura=banking_reference['opening'], tipo=banking_reference['type'], data_criacao=timezone.now())
            banking_reference_registred.save()
        except:
            raise exceptions.APIException(
                'Não foi possível salvar os dados de refenrências bancárias')

    return Response({'detail': 'Cadastro feito com sucesso'})


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def delete(request, id_person):
    try:
        person = Pescod.objects.get(pk=id_person)
        person.sit = 0
        person.save()
        return Response({'detail': 'Apagado com sucesso!'})
    except:
        raise exceptions.APIException('Não foi possível deletar o registro')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def details_physical_person(request, id_person):
    # LIST OF THE POSSIBLE SEARCH ERRORS IN THE DATA OF THE PERSON SEARCHED
    details = []

    try:
        person = Pescod.objects.get(pk=id_person)
        person_serialized = PescodSerializer(person)
    except:
        raise exceptions.APIException(
            'Não foi possível pesquisar os dados do registro.')

    # FIND PHYSICAL PERSON DATA
    person_physical = Pesfis.objects.get(id_pessoa_cod_fk=id_person)
    if not person_physical:
        details.append(
            'Não foi possível encontrar os dados deste registro.')
    person_physical_serialized = PessoaFisicaSerializers(
        person_physical)

    # FIND ADRESS DATA THIS PERSON
    person_adress = Enderecos.objects.filter(id_pessoa_cod_fk=id_person)
    if not person_adress:
        details.append(
            'Não foi possível encontrar os dados de endereço deste registro.')
    person_adress_serialized = EnderecosSerializers(
        person_adress, many=True)

    # FIND PHONE DATA THIS PERSON
    person_phone = Telefones.objects.filter(id_pessoa_cod_fk=id_person)
    if not person_phone:
        details.append(
            'Não foi possível encontrar os dados de contato deste registro.')
    person_phone_serialized = TelefoneSerializers(person_phone, many=True)

    # FIND MAIL DATA THIS PERSON
    person_mail = Mails.objects.filter(id_pessoa_cod_fk=id_person)
    if not person_physical:
        details.append(
            'Não foi possível encontrar os dados de e-mail deste registro.')
    person_mail_serialized = EmailSerializers(person_mail, many=True)

    # FIND REFERENCES DATA THIS PERSON
    person_references = Referencias.objects.filter(
        id_pessoa_cod_fk=id_person)
    if not person_references:
        details.append(
            'Não foi possível encontrar os dados de referência deste registro.')
    person_references_serialized = ReferenciasSerializers(
        person_references, many=True)

    # FIND BANKING REFERENCES DATA THIS PERSON
    banking_references = Refbanco.objects.filter(
        id_pessoa_cod_fk=id_person)
    if not banking_references:
        details.append(
            'Não foi possível encontrar os dados bancários deste registro.')
    banking_references_serialized = RefBancoSerializers(
        banking_references, many=True)

    return Response({
        'person': person_serialized.data,
        'personPhysical': person_physical_serialized.data,
        'personAdress': person_adress_serialized.data,
        'personPhone': person_phone_serialized.data,
        'personMail': person_mail_serialized.data,
        'personReferences': person_references_serialized.data,
        'bankingReferences': banking_references_serialized.data,
        'details': details
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
@transaction.atomic
def store_legal_person(request):
    id_institution = request.user.instit_id
    cnpj = request.data.get('personCNPJ')
    """  
    FIND CPF ON DATABASE. IF EXIST, NO REGISTER AND RETURN
    """
    person = Pescod.objects.filter(
        id_instituicao_fk=id_institution, cpfcnpj=cnpj, sit=2)
    if person:
        return Response({'detail': 'Já existe um registro ativo com este CNPJ. Por favor revise os dados.'}, status=status.HTTP_400_BAD_REQUEST)

    """  
    REGISTER PESCOD
    """
    provider = request.data.get('personIsProvider')
    company_name = request.data.get('companyName')
    person_photo = request.data.get('personPhoto')
    person_limit = request.data.get('personLimit')
    person_balance = request.data.get('personBalance')

    try:
        person = Pescod(id_instituicao_fk=id_institution, tipo=2, sit=2, forn=provider, cpfcnpj=cnpj,
                        nomeorrazaosocial=company_name, foto=person_photo, img_bites=0, limite=person_limit, saldo=person_balance, data_criacao=timezone.now())
        person.save()
    except:
        raise exceptions.APIException(
            'Não foi possível cadastrar o registro da pessoa. Verifique os dados inseridos.')

    """  
    REGISTER LEGAL PERSON
    """
    person_registred_id = person.id_pessoa_cod
    fantasy_name = request.data.get('fantasyName')
    branch = request.data.get('branch')
    company_type = request.data.get('companyType')
    share_capital = request.data.get('shareCapital')
    revenues = request.data.get('revenues')
    taxation = request.data.get('taxation')
    contact = request.data.get('contact')
    open_date = request.data.get('openDate')
    state_registration = request.data.get('stateRegistrationCompany')
    municipal_registration = request.data.get('municipalRegistrationCompany')

    try:
        legal_person = Pesjur(id_pessoa_cod_fk=person_registred_id, fantasia=fantasy_name, ramo=branch, inscricao_estadual=state_registration,
                              inscricao_municipal=municipal_registration, tipo_empresa=company_type, capsocial=share_capital, faturamento=revenues,
                              tribut=taxation, contato=contact, data_abertura=open_date, data_criacao=timezone.now())
        legal_person.save()
    except:
        raise exceptions.APIException(
            'Não foi possível cadastrar os dados de pessoa jurídica')

    """ 
    REGISTER ADRESS
    """
    adresses_array = request.data.get('adresses')
    for adress in adresses_array:
        try:
            adress_registred = Enderecos(situacao=1, origem=1, id_pessoa_cod_fk=person_registred_id, endtip=1, rua=adress['street'],
                                         numero=adress['numberHouse'], complemento=adress['complement'], bairro=adress['neighborhood'],
                                         cep=adress['zipCode'], cidade=adress['city'], estado_endereco=adress['stateAdress'], data_criacao=timezone.now())
            adress_registred.save()
        except:
            raise exceptions.APIException(
                'Não foi possível salvar todos os dados de endereço')

    """  
    REGISTER PHONE
    """
    phones_array = request.data.get('phones')
    for phone in phones_array:
        try:
            phone_registered = Telefones(id_pessoa_cod_fk=person_registred_id,
                                         situacao=1, tel=phone['phoneNumber'], data_criacao=timezone.now())
            phone_registered.save()
        except:
            raise exceptions.APIException(
                'Não foi possível salvar os dados de contato')

    """ 
    REGISTER MAIL    
    """
    mails_array = request.data.get('mails')
    for mail in mails_array:
        try:
            mail_registered = Mails(
                id_pessoa_cod_fk=person_registred_id, situacao=1, email=mail['userMail'], data_criacao=timezone.now())
            mail_registered.save()
        except:
            raise exceptions.APIException(
                'Não foi possível salvar os dados de email')

    """  
    REGISTER REFERENCES
    """
    references_array = request.data.get('personReferences')
    for reference in references_array:
        try:
            references_registered = Referencias(id_pessoa_cod_fk=person_registred_id,
                                                situacao=1, tipo=reference['referenceType'], nome=reference['referenceName'],
                                                tel=reference['referencePhone'], endereco=reference['referenceAdress'], data_criacao=timezone.now())
            references_registered.save()
        except:
            raise exceptions.APIException(
                'Não foi possível salvar os dados da referência')

    """  
    REGISTER BANK
    """
    banking_references_array = request.data.get('bankingReferences')
    for banking_reference in banking_references_array:
        try:
            banking_reference_registred = Refbanco(id_pessoa_cod_fk=person_registred_id, id_bancos_fk=banking_reference['idBanking'], situacao=1,
                                                   agencia=banking_reference['agency'], conta=banking_reference['account'],
                                                   abertura=banking_reference['opening'], tipo=banking_reference['type'], data_criacao=timezone.now())
            banking_reference_registred.save()
        except:
            raise exceptions.APIException(
                'Não foi possível salvar os dados de refenrências bancárias')

    return Response({'detail': 'Cadastro feito com sucesso'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def details_legal_person(request, id_person):
    # LIST OF THE POSSIBLE SEARCH ERRORS IN THE DATA OF THE PERSON SEARCHED
    details = []

    # FIND DATA OF THE TABLE PESCOD
    try:
        person = Pescod.objects.get(pk=id_person)
        person_serialized = PescodSerializer(person)
    except:
        raise exceptions.APIException(
            'Não foi possível pesquisar os dados do registro.')

    # FIND LEGAL PERSON DATA
    legal_person = Pesjur.objects.get(id_pessoa_cod_fk=id_person)
    if not legal_person:
        details.append(
            'Não foi possível encontrar os dados deste registro.')
    legal_person_serialized = PessoaJuridicaSerializer(
        legal_person)

    # FIND ADRESS DATA THIS PERSON
    person_adress = Enderecos.objects.filter(id_pessoa_cod_fk=id_person)
    if not person_adress:
        details.append(
            'Não foi possível encontrar os dados de endereço deste registro.')
    person_adress_serialized = EnderecosSerializers(
        person_adress, many=True)

    # FIND PHONE DATA THIS PERSON
    person_phone = Telefones.objects.filter(id_pessoa_cod_fk=id_person)
    if not person_phone:
        details.append(
            'Não foi possível encontrar os dados de contato deste registro.')
    person_phone_serialized = TelefoneSerializers(person_phone, many=True)

    # FIND MAIL DATA THIS PERSON
    person_mail = Mails.objects.filter(id_pessoa_cod_fk=id_person)
    if not person_mail:
        details.append(
            'Não foi possível encontrar os dados de e-mail deste registro.')
    person_mail_serialized = EmailSerializers(person_mail, many=True)

    # FIND REFERENCES DATA THIS PERSON
    person_references = Referencias.objects.filter(
        id_pessoa_cod_fk=id_person)
    if not person_references:
        details.append(
            'Não foi possível encontrar os dados de referência deste registro.')
    person_references_serialized = ReferenciasSerializers(
        person_references, many=True)

    # FIND BANKING REFERENCES DATA THIS PERSON
    banking_references = Refbanco.objects.filter(
        id_pessoa_cod_fk=id_person)
    if not banking_references:
        details.append(
            'Não foi possível encontrar os dados bancários deste registro.')
    banking_references_serialized = RefBancoSerializers(
        banking_references, many=True)

    return Response({
        'person': person_serialized.data,
        'personPhysical': legal_person_serialized.data,
        'personAdress': person_adress_serialized.data,
        'personPhone': person_phone_serialized.data,
        'personMail': person_mail_serialized.data,
        'personReferences': person_references_serialized.data,
        'bankingReferences': banking_references_serialized.data,
        'details': details
    })


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
@transaction.atomic
def edit_legal_person(request, id_person):
    id_institution = request.user.instit_id

    """  
    EDIT PESCOD
    """
    person_is_provider = request.data.get('personIsProvider')
    person_cnpj = request.data.get('personCNPJ')
    company_name = request.data.get('companyName')
    person_photo = request.data.get('personPhoto')
    person_limit = request.data.get('personLimit')
    person_balance = request.data.get('personBalance')
    try:
        """  
        FIND PERSON ON DATABASE. IF NOT EXISTS, NO EDIT AND RETURN
        """
        person = Pescod.objects.get(pk=id_person)
        if not person:
            return Response({'detail': 'Não existe nenhum registro com este CNPJ. Por favor revise os dados.'}, status=status.HTTP_400_BAD_REQUEST)
        print(f'ENCONTROU OS DADOS DA PESSOA', person)

        person.forn = person_is_provider
        print('FORN')
        person.cpfcnpj = person_cnpj
        print('CNPJ')
        person.nomeorrazaosocial = company_name
        print('RAZAO SOCIAL')
        person.foto = person_photo
        print('FOTO')
        person.limite = person_limit
        print('LIMITE')
        person.saldo = person_balance
        print('SALDO')
        person.save()
        print('SALVO')
    except:
        raise exceptions.APIException(
            'Não foi possível editar o registro da pessoa. Verifique os dados inseridos.')

    """  
    REGISTER LEGAL PERSON
    """

    try:
        legal_person = Pesjur.objects.filter(id_pessoa_cod_fk=id_person)
        legal_person.fantasia = request.data.get('fantasyName')
        legal_person.ramo = request.data.get('branch')
        legal_person.tipo_empresa = request.data.get('companyType')
        legal_person.capsocial = request.data.get('shareCapital')
        legal_person.faturamento = request.data.get('revenues')
        legal_person.tribut = request.data.get('taxation')
        legal_person.contato = request.data.get('contact')
        legal_person.data_abertura = request.data.get('openDate')
        legal_person.inscricao_estadual = request.data.get(
            'stateRegistrationCompany')
        legal_person.inscricao_municipal = request.data.get(
            'municipalRegistrationCompany')

        legal_person.save()
    except:
        raise exceptions.APIException(
            'Não foi possível editar os dados de pessoa jurídica')

    """ 
    REGISTER ADRESS
    """
    addresses_array = request.data.get('adresses')
    for address in addresses_array:
        try:
            address_registred = Enderecos.objects.get(pk=address['idAddress'])
            address_registred.rua = address['street']
            address_registred.numero = address['numberHouse']
            address_registred.complemento = address['complement']
            address_registred.bairro = address['neighborhood']
            address_registred.cep = address['zipCode']
            address_registred.city = address['city']
            address_registred.estado_endereco = address['stateAdress']
            address_registred.save()
        except:
            raise exceptions.APIException(
                'Não foi possível atualizar todos os dados de endereço')

    """  
    REGISTER PHONE
    """
    phones_array = request.data.get('phones')
    for phone in phones_array:
        try:
            phone_registered = Telefones.objects.get(pk=phone['idPhone'])
            phone_registered.tel = phone['phoneNumber']
            phone_registered.save()
        except:
            raise exceptions.APIException(
                'Não foi possível atualizar os dados de contato')

    """ 
    REGISTER MAIL    
    """
    mails_array = request.data.get('mails')
    for mail in mails_array:
        try:
            mail_registered = Mails.objects.get(pk=mail['idMail'])
            mail_registered.email = mail['userMail']
            mail_registered.save()
        except:
            raise exceptions.APIException(
                'Não foi possível salvar os dados de email')

    """  
    REGISTER REFERENCES
    """
    references_array = request.data.get('personReferences')
    for reference in references_array:
        try:
            reference_registered = Referencias.objects.get(
                pk=reference['idReference'])
            reference_registered.tipo = reference['referenceType']
            reference_registered.nome = reference['referenceName']
            reference_registered.tel = reference['referencePhone']
            reference_registered.endereco = reference['referenceAdress']
            reference_registered.save()
        except:
            raise exceptions.APIException(
                'Não foi possível atualizar os dados da referência')

    """  
    REGISTER BANK
    """
    banking_references_array = request.data.get('bankingReferences')
    for banking_reference in banking_references_array:
        try:
            banking_reference_registred = Refbanco.objects.get(
                pk=banking_reference['idBankingReference'])
            banking_reference_registred.id_bancos_fk = banking_reference['idBanking']
            banking_reference_registred.agencia = banking_reference['agency']
            banking_reference_registred.conta = banking_reference['account']
            banking_reference_registred.abertura = banking_reference['opening']
            banking_reference_registred.tipo = banking_reference['type']
            banking_reference_registred.save()
        except:
            raise exceptions.APIException(
                'Não foi possível atualizar os dados de refenrências bancárias')

    return Response({'detail': 'Dados atualizados com sucesso'})


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
@transaction.atomic
def edit_person_physical(request, id_person):
    id_institution = request.user.instit_id
    """  
    FIND CPF ON DATABASE. IF NO EXISTS, NO UPDATE AND RETURN
    """
    person = Pescod.objects.filter(pk=id_person, sit=1)
    if not person:
        return Response({'detail': 'Não existe nenhum registro ativo com este CPF. Por favor revise os dados.'}, status=status.HTTP_400_BAD_REQUEST)

    """  
    UPDATE PESCOD
    """
    try:
        person.cpfcnpj = request.data.get('personCPF')
        person.forn = request.data.get('personIsProvider')
        person.cpfcnpj = request.data.get('personCPF')
        person.nomeorrazaosocial = request.data.get('personName')
        person.foto = request.data.get('personPhoto')
        person.limite = request.data.get('personLimit')
        person.saldo = request.data.get('personBalance')
        person.save()
    except:
        raise exceptions.APIException(
            'Não foi possível atualizar o registro da pessoa. Verifique os dados inseridos.')

    """  
    UPDATE PHYSICAL PERSON
    """
    try:
        person_physical = Pesfis.objects.filter(id_pessoa_cod_fk=id_person)

        person_physical.identidade = request.data.get('personIdentity')
        person_physical.emissor_identidade = request.data.get('issuerIdentity')
        person_physical.id_municipio_fk = request.data.get(
            'personMunicipality')
        person_physical.id_uf_municipio_fk = request.data.get('personUF')
        person_physical.data_de_nascimento = request.data.get('personBirth')
        person_physical.tratam = request.data.get('personTreatment')
        person_physical.apelido = request.data.get('personNickname')
        person_physical.sexo = request.data.get('personSex')
        person_physical.pai = request.data.get('personFather')
        person_physical.mae = request.data.get('personMother')
        person_physical.profissao = request.data.get('personProfession')
        person_physical.ctps = request.data.get('ctps')
        person_physical.salario = request.data.get('personSalary')
        person_physical.empresa = request.data.get('personCompany')
        person_physical.resp = request.data.get('companyResponsible')
        person_physical.cnpj = request.data.get('companyCnpj')
        person_physical.iest = request.data.get('stateRegistrationCompany')
        person_physical.imun = request.data.get('municipalRegistrationCompany')
        person_physical.emprend = request.data.get('companyAdress')
        person_physical.orendas = request.data.get('otherIncome')
        person_physical.vrendas = request.data.get('incomeValue')
        person_physical.irpf = request.data.get('irpf')
        person_physical.estcivil = request.data.get('maritalStatus')
        person_physical.depend = request.data.get('personDependents')
        person_physical.pensao = request.data.get('pension')
        person_physical.conjugue = request.data.get('spouse')
        person_physical.cpfconj = request.data.get('spouseCpf')
        person_physical.profconj = request.data.get('spouseProfession')
        person_physical.emprconj = request.data.get('spouseCompany')
        person_physical.rendaconj = request.data.get('spouseIncome')
        person_physical.telconj = request.data.get('spousePhone')
        person_physical.mailconj = request.data.get('spouseMail')

        person_physical.save()
    except:
        raise exceptions.APIException(
            'Não foi possível atualizar os dados de pessoa física')

    """ 
    UPDATE ADRESS
    """
    addresses_array = request.data.get('adresses')
    for address in addresses_array:
        try:
            address_registred = Enderecos.objects.get(address['idAddress'])
            address_registred.rua = address['street']
            address_registred.numero = address['numberHouse']
            address_registred.complemento = address['complement']
            address_registred.bairro = address['neighborhood']
            address_registred.cep = address['zipCode']
            address_registred.cidade = address['city']
            address_registred.estado_endereco = address['stateAdress']

            address_registred.save()
        except:
            raise exceptions.APIException(
                'Não foi possível atualizar todos os dados de endereço')

    """  
    UPDATE PHONE
    """
    phones_array = request.data.get('phones')
    for phone in phones_array:
        try:
            phone_registered = Telefones.objects.get(pk=phone['idPhone'])
            phone_registered.tel = phone['phoneNumber']

            phone_registered.save()
        except:
            raise exceptions.APIException(
                'Não foi possível atualizar os dados de contato')

    """ 
    UPDATE MAIL    
    """
    mails_array = request.data.get('mails')
    for mail in mails_array:
        try:
            mail_registered = Mails.objects.get(pk=mail['idMail'])
            mail_registered.email = mail['userMail']

            mail_registered.save()
        except:
            raise exceptions.APIException(
                'Não foi possível atualizar os dados de email')

    """  
    UPDATE REFERENCES
    """
    references_array = request.data.get('personReferences')
    for reference in references_array:
        try:
            references_registered = Referencias.objects.get(
                pk=reference['idReference'])
            references_registered.tipo = reference['redferenceType']
            references_registered.nome = reference['referenceName']
            references_registered.tel = reference['referencePhone']
            references_registered.endereco = reference['referenceAdress']

            references_registered.save()
        except:
            raise exceptions.APIException(
                'Não foi possível atualizar os dados da referência')

    """  
    UPDATE BANK
    """
    banking_references_array = request.data.get('bankingReferences')
    for banking_reference in banking_references_array:
        try:
            banking_reference_registred = Refbanco.objects.get(
                pk=banking_reference['idBankingReference'])
            banking_reference_registred.id_bancos_fk = banking_reference['idBanking']
            banking_reference_registred.agencia = banking_reference['agency']
            banking_reference_registred.conta = banking_reference['account']
            banking_reference_registred.abertura = banking_reference['opening']
            banking_reference_registred.tipo = banking_reference['type']

            banking_reference_registred.save()
        except:
            raise exceptions.APIException(
                'Não foi possível atualizar os dados de refenrências bancárias')

    return Response({'detail': 'Atualização feita com sucesso'})
