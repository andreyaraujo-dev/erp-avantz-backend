from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status
from datetime import datetime
from django.utils import timezone
from django.db import transaction

import sys

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
def find_physical_persons(request, personName=None):
    id_institution = request.user.instit_id
    if personName == None:
        try:
            persons = Pescod.objects.filter(
                id_instituicao_fk=id_institution, sit=2, tipo=1)
            persons_serialized = PescodSerializer(persons, many=True)
            return Response(persons_serialized.data)
        except:
            raise exceptions.APIException
    else:
        try:
            persons = Pescod.objects.filter(
                id_instituicao_fk=id_institution, sit=2, tipo=1, nomeorrazaosocial__contains=personName)
            persons_serialized = PescodSerializer(persons, many=True)
            return Response(persons_serialized.data)
        except:
            raise exceptions.APIException


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def find_legal_persons(request, personName=None):
    id_institution = request.user.instit_id
    if personName == None:
        try:
            persons = Pescod.objects.filter(
                id_instituicao_fk=id_institution, sit=2, tipo=2)
            persons_serialized = PescodSerializer(persons, many=True)
            return Response(persons_serialized.data)
        except:
            raise exceptions.APIException
    else:
        try:
            persons = Pescod.objects.filter(
                id_instituicao_fk=id_institution, sit=2, tipo=2, nomeorrazaosocial__contains=personName)
            persons_serialized = PescodSerializer(persons, many=True)
            return Response(persons_serialized.data)
        except:
            raise exceptions.APIException


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def find_providers(request):
    id_institution = request.user.instit_id
    try:
        persons = Pescod.objects.filter(
            id_instituicao_fk=id_institution, sit=2, forn=1)
        persons_serialized = PescodSerializer(persons, many=True)
        return Response(persons_serialized.data)
    except:
        raise exceptions.APIException


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
@transaction.atomic
def store_person_physical(request):
    id_institution = request.user.instit_id
    cpf = request.data.get('cpfcnpj')
    """  
    FIND CPF ON DATABASE. IF EXIST, NO REGISTER AND RETURN
    """
    person_already_exists = Pescod.objects.filter(
        id_instituicao_fk=id_institution, cpfcnpj=cpf, sit=2)
    if person_already_exists:
        return Response({'detail': 'Já existe um registro ativo com este CPF. Por favor revise os dados.'}, status=status.HTTP_400_BAD_REQUEST)

    """  
    REGISTER PESCOD
    """
    provider = request.data.get('forn')
    person_photo = request.data.get('foto')
    person_name = request.data.get('nomeorrazaosocial')
    person_limit = request.data.get('limite')
    person_balance = request.data.get('saldo')

    try:
        person = Pescod(id_instituicao_fk=id_institution,
                        tipo=1,
                        sit=2,
                        forn=provider,
                        cpfcnpj=cpf,
                        nomeorrazaosocial=person_name,
                        foto=person_photo,
                        img_bites=0,
                        limite=person_limit,
                        saldo=person_balance,
                        data_criacao=timezone.now())
        person.save()
    except:
        raise exceptions.APIException(
            'Não foi possível cadastrar o registro da pessoa. Verifique os dados inseridos.')

    """  
    REGISTER PHYSICAL PERSON
    """
    person_registred_id = person.id_pessoa_cod
    identity = request.data.get('identidade')
    issuer_identity = request.data.get('emissor_identidade')
    id_municipality = request.data.get('id_municipio_fk')
    id_uf = request.data.get('id_uf_municipio_fk')
    date_of_birth = request.data.get('data_de_nascimento')
    treatment = request.data.get('tratam')
    nickname = request.data.get('apelido')
    sex = request.data.get('sexo')
    father = request.data.get('pai')
    mother = request.data.get('mae')
    profession = request.data.get('profissao')
    ctps = request.data.get('ctps')
    salary = request.data.get('salario')
    company = request.data.get('empresa')
    company_responsible = request.data.get('resp')
    company_cnpj = request.data.get('cnpj')
    state_registration = request.data.get('iest')
    municipal_registration = request.data.get('imun')
    company_adress = request.data.get('emprend')
    other_income = request.data.get('orendas')
    income_value = request.data.get('vrendas')
    irpf = request.data.get('irpf')
    marital_status = request.data.get('estcivil')
    dependents = request.data.get('depend')
    pension = request.data.get('pensao')
    spouse = request.data.get('conjuge')
    spouse_cpf = request.data.get('cpfconj')
    spouse_profession = request.data.get('profconj')
    spouse_company = request.data.get('emprconj')
    spouse_income = request.data.get('rendaconj')
    spouse_phone = request.data.get('telconj')
    spouse_mail = request.data.get('mailconj')

    try:
        person_physical = Pesfis(id_pessoa_cod_fk=person_registred_id, identidade=identity, emissor_identidade=issuer_identity, id_municipio_fk=id_municipality,
                                 id_uf_municipio_fk=id_uf, data_de_nascimento=date_of_birth, tratam=treatment, apelido=nickname, sexo=sex, pai=father, mae=mother,
                                 profissao=profession, ctps=ctps, salario=salary, empresa=company, resp=company_responsible, cnpj=company_cnpj, iest=state_registration,
                                 imun=municipal_registration, emprend=company_adress, orendas=other_income, vrendas=income_value, irpf=irpf, estcivil=marital_status,
                                 depend=dependents, pensao=pension, conjuge=spouse, cpfconj=spouse_cpf, profconj=spouse_profession, emprconj=spouse_company,
                                 rendaconj=spouse_income, telconj=spouse_phone, mailconj=spouse_mail, data_criacao=timezone.now())
        person_physical.save()
    except:
        raise exceptions.APIException(
            'Não foi possível cadastrar os dados de pessoa física.')

    """ 
    REGISTER ADRESS
    """
    addresses_array = request.data.get('addresses')
    for address in addresses_array:
        try:
            address_registred = Enderecos(situacao=1, origem=1, id_pessoa_cod_fk=person_registred_id, endtip=1, rua=address['street'],
                                          numero=address['numberHouse'], complemento=address['complement'], bairro=address['neighborhood'],
                                          cep=address['zipCode'], cidade=address['city'], estado_endereco=address['state'], data_criacao=timezone.now())
            address_registred.save()
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
@csrf_exempt
@transaction.atomic
def delete(request, id_person):
    id_institution = request.user.instit_id

    person = Pescod.objects.filter(id_pessoa_cod=id_person, sit=2).first()
    if not person:
        return Response({'detail': 'Registro não encontrado, tente novamente.'}, status=status.HTTP_404_NOT_FOUND)

    try:
        person.sit = 0
        person.save()

        if person.tipo == 1:
            persons = Pescod.objects.filter(
                id_instituicao_fk=id_institution, sit=2, tipo=1)
            persons_serialized = PescodSerializer(persons, many=True)
            return Response(persons_serialized.data)

        if person.tipo == 2:
            persons = Pescod.objects.filter(
                id_instituicao_fk=id_institution, sit=2, tipo=2)
            persons_serialized = PescodSerializer(persons, many=True)
            return Response(persons_serialized.data)
    except:
        raise exceptions.APIException(
            'Não foi possível deletar o registro, tente novamente.', code=500)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def details_physical_person(request, id_person):
    id_institution = request.user.instit_id

    # LIST OF THE POSSIBLE SEARCH ERRORS IN THE DATA OF THE PERSON SEARCHED
    details = []

    try:
        person = Pescod.objects.filter(
            id_pessoa_cod=id_person, id_instituicao_fk=id_institution, sit=2).get()
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
    person_adress = Enderecos.objects.filter(
        id_pessoa_cod_fk=id_person, situacao=1)
    if not person_adress:
        details.append(
            'Não foi possível encontrar os dados de endereço deste registro.')
    person_adress_serialized = EnderecosSerializers(
        person_adress, many=True)

    # FIND PHONE DATA THIS PERSON
    person_phone = Telefones.objects.filter(
        id_pessoa_cod_fk=id_person, situacao=1)
    if not person_phone:
        details.append(
            'Não foi possível encontrar os dados de contato deste registro.')
    person_phone_serialized = TelefoneSerializers(person_phone, many=True)

    # FIND MAIL DATA THIS PERSON
    person_mail = Mails.objects.filter(id_pessoa_cod_fk=id_person, situacao=1)
    if not person_physical:
        details.append(
            'Não foi possível encontrar os dados de e-mail deste registro.')
    person_mail_serialized = EmailSerializers(person_mail, many=True)

    # FIND REFERENCES DATA THIS PERSON
    person_references = Referencias.objects.filter(
        id_pessoa_cod_fk=id_person, situacao=1)
    if not person_references:
        details.append(
            'Não foi possível encontrar os dados de referência deste registro.')
    person_references_serialized = ReferenciasSerializers(
        person_references, many=True)

    # FIND BANKING REFERENCES DATA THIS PERSON
    banking_references = Refbanco.objects.filter(
        id_pessoa_cod_fk=id_person, situacao=1)
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
@csrf_exempt
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
            'Não foi possível cadastrar os dados de pessoa jurídica.')

    """ 
    REGISTER ADRESS
    """
    adresses_array = request.data.get('adresses')
    for adress in adresses_array:
        try:
            adress_registred = Enderecos(situacao=1, origem=1, id_pessoa_cod_fk=person_registred_id, endtip=1, rua=adress['street'],
                                         numero=adress['numberHouse'], complemento=adress['complement'], bairro=adress['neighborhood'],
                                         cep=adress['zipCode'], cidade=adress['city'], estado_endereco=adress['state'], data_criacao=timezone.now())
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
    person_adress = Enderecos.objects.filter(
        id_pessoa_cod_fk=id_person, situacao=1)
    if not person_adress:
        details.append(
            'Não foi possível encontrar os dados de endereço deste registro.')
    person_adress_serialized = EnderecosSerializers(
        person_adress, many=True)

    # FIND PHONE DATA THIS PERSON
    person_phone = Telefones.objects.filter(
        id_pessoa_cod_fk=id_person, situacao=1)
    if not person_phone:
        details.append(
            'Não foi possível encontrar os dados de contato deste registro.')
    person_phone_serialized = TelefoneSerializers(person_phone, many=True)

    # FIND MAIL DATA THIS PERSON
    person_mail = Mails.objects.filter(id_pessoa_cod_fk=id_person, situacao=1)
    if not person_mail:
        details.append(
            'Não foi possível encontrar os dados de e-mail deste registro.')
    person_mail_serialized = EmailSerializers(person_mail, many=True)

    # FIND REFERENCES DATA THIS PERSON
    person_references = Referencias.objects.filter(
        id_pessoa_cod_fk=id_person, situacao=1)
    if not person_references:
        details.append(
            'Não foi possível encontrar os dados de referência deste registro.')
    person_references_serialized = ReferenciasSerializers(
        person_references, many=True)

    # FIND BANKING REFERENCES DATA THIS PERSON
    banking_references = Refbanco.objects.filter(
        id_pessoa_cod_fk=id_person, situacao=1)
    if not banking_references:
        details.append(
            'Não foi possível encontrar os dados bancários deste registro.')
    banking_references_serialized = RefBancoSerializers(
        banking_references, many=True)

    return Response({
        'person': person_serialized.data,
        'legalPerson': legal_person_serialized.data,
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
@csrf_exempt
@transaction.atomic
def edit_legal_person(request, id_person):
    id_institution = request.user.instit_id

    """  
    FIND PERSON ON DATABASE. IF NOT EXISTS, NO EDIT AND RETURN
    """
    try:
        person = Pescod.objects.get(pk=id_person, sit=2)
    except:
        raise exceptions.NotFound(
            'Não existe nenhum registro com este CNPJ. Por favor revise os dados.', code=404)

    """  
    EDIT PESCOD
    """
    try:
        person.forn = request.data.get('forn')
        person.cpfcnpj = request.data.get('cpfcnpj')
        person.nomeorrazaosocial = request.data.get('nomeorrazaosocial')
        person.foto = request.data.get('foto')
        person.limite = request.data.get('limite')
        person.saldo = request.data.get('saldo')

        person.save()
    except:
        raise exceptions.APIException(
            'Não foi possível editar o registro da pessoa. Verifique os dados inseridos.')

    """  
    UPDATE LEGAL PERSON
    """
    try:
        legal_person = Pesjur.objects.filter(
            id_pessoa_cod_fk=id_person).first()
        legal_person.fantasia = request.data.get('fantasia')
        legal_person.ramo = request.data.get('ramo')
        legal_person.tipo_empresa = request.data.get('tipo_empresa')
        legal_person.capsocial = request.data.get('capsocial')
        legal_person.faturamento = request.data.get('faturamento')
        legal_person.tribut = request.data.get('tribut')
        legal_person.contato = request.data.get('contato')
        legal_person.data_abertura = request.data.get('data_abertura')
        legal_person.inscricao_estadual = request.data.get(
            'inscricao_estadual')
        legal_person.inscricao_municipal = request.data.get(
            'inscricao_municipal')

        legal_person.save()
    except:
        raise exceptions.APIException(
            'Não foi possível editar os dados de pessoa jurídica')

    """ 
    UPDATE ADRESS
    """
    addresses_array = request.data.get('adresses')
    for address in addresses_array:
        try:
            address_registred = Enderecos.objects.get(
                pk=address['id_enderecos'])
            address_registred.rua = address['rua']
            address_registred.numero = address['numero']
            address_registred.complemento = address['complemento']
            address_registred.bairro = address['bairro']
            address_registred.cep = address['cep']
            address_registred.city = address['cidade']
            address_registred.estado_endereco = address['estado_endereco']
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
            phone_registered = Telefones.objects.get(pk=phone['id_telefone'])
            phone_registered.tel = phone['tel']
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
            mail_registered = Mails.objects.get(pk=mail['id_mails'])
            mail_registered.email = mail['email']
            mail_registered.save()
        except:
            raise exceptions.APIException(
                'Não foi possível salvar os dados de email')

    """  
    UPDATE REFERENCES
    """
    references_array = request.data.get('personReferences')
    for reference in references_array:
        try:
            reference_registered = Referencias.objects.get(
                pk=reference['id_referencia'])
            reference_registered.tipo = reference['tipo']
            reference_registered.nome = reference['nome']
            reference_registered.tel = reference['tel']
            reference_registered.endereco = reference['endereco']
            reference_registered.save()
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
                pk=banking_reference['id_banco'])
            banking_reference_registred.id_bancos_fk = banking_reference['id_bancos_fk']
            banking_reference_registred.agencia = banking_reference['agencia']
            banking_reference_registred.conta = banking_reference['conta']
            banking_reference_registred.abertura = banking_reference['abertura']
            banking_reference_registred.tipo = banking_reference['tipo']
            banking_reference_registred.save()
        except:
            raise exceptions.APIException(
                'Não foi possível atualizar os dados de refenrências bancárias')

    return Response({'detail': 'Dados atualizados com sucesso'})


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
@transaction.atomic
def edit_person_physical(request, id_person):
    id_institution = request.user.instit_id
    """  
    FIND CPF ON DATABASE. IF NO EXISTS, NO UPDATE AND RETURN
    """
    try:
        person = Pescod.objects.filter(pk=id_person, sit=2).first()
    except:
        raise exceptions.NotFound(
            'Não existe nenhum registro ativo com este CPF. Por favor revise os dados.', code=404)

    """  
    UPDATE PESCOD
    """
    try:
        person.forn = request.data.get('forn')
        person.cpfcnpj = request.data.get('cpfcnpj')
        person.nomeorrazaosocial = request.data.get('nomeorrazaosocial')
        person.foto = request.data.get('foto')
        person.limite = request.data.get('limite')
        person.saldo = request.data.get('saldo')

        person.save()
    except:
        raise exceptions.APIException(
            'Não foi possível atualizar o registro da pessoa. Verifique os dados inseridos.')

    """  
    UPDATE PHYSICAL PERSON
    """
    try:
        person_physical = Pesfis.objects.filter(
            id_pessoa_cod_fk=id_person).first()

        person_physical.identidade = request.data.get('identidade')
        person_physical.emissor_identidade = request.data.get(
            'emissor_identidade')
        person_physical.id_municipio_fk = request.data.get(
            'id_municipio_fk')
        person_physical.id_uf_municipio_fk = request.data.get(
            'id_uf_municipio_fk')
        person_physical.data_de_nascimento = request.data.get(
            'data_de_nascimento')
        person_physical.tratam = request.data.get('tratam')
        person_physical.apelido = request.data.get('apelido')
        person_physical.sexo = request.data.get('sexo')
        person_physical.pai = request.data.get('pai')
        person_physical.mae = request.data.get('mae')
        person_physical.profissao = request.data.get('profissao')
        person_physical.ctps = request.data.get('ctps')
        person_physical.salario = request.data.get('salario')
        person_physical.empresa = request.data.get('empresa')
        person_physical.resp = request.data.get('resp')
        person_physical.cnpj = request.data.get('cnpj')
        person_physical.iest = request.data.get('iest')
        person_physical.imun = request.data.get('imun')
        person_physical.emprend = request.data.get('emprend')
        person_physical.orendas = request.data.get('orendas')
        person_physical.vrendas = request.data.get('vrendas')
        person_physical.irpf = request.data.get('irpf')
        person_physical.estcivil = request.data.get('estcivil')
        person_physical.depend = request.data.get('depend')
        person_physical.pensao = request.data.get('pensao')
        person_physical.conjugue = request.data.get('conjugue')
        person_physical.cpfconj = request.data.get('cpfconj')
        person_physical.profconj = request.data.get('profconj')
        person_physical.emprconj = request.data.get('emprconj')
        person_physical.rendaconj = request.data.get('rendaconj')
        person_physical.telconj = request.data.get('telconj')
        person_physical.mailconj = request.data.get('mailconj')

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
            address_registred = Enderecos.objects.get(
                pk=address['id_enderecos'])
            address_registred.rua = address['rua']
            address_registred.numero = address['numero']
            address_registred.complemento = address['complemento']
            address_registred.bairro = address['bairro']
            address_registred.cep = address['cep']
            address_registred.cidade = address['cidade']
            address_registred.estado_endereco = address['estado_endereco']

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
            phone_registered = Telefones.objects.get(pk=phone['id_telefone'])
            phone_registered.tel = phone['tel']

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
            mail_registered = Mails.objects.get(pk=mail['id_mails'])
            mail_registered.email = mail['email']

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
                pk=reference['id_referencia'])
            references_registered.tipo = reference['tipo']
            references_registered.nome = reference['nome']
            references_registered.tel = reference['tel']
            references_registered.endereco = reference['endereco']

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
                pk=banking_reference['id_banco'])
            banking_reference_registred.id_bancos_fk = banking_reference['id_bancos_fk']
            banking_reference_registred.agencia = banking_reference['agencia']
            banking_reference_registred.conta = banking_reference['conta']
            banking_reference_registred.abertura = banking_reference['abertura']
            banking_reference_registred.tipo = banking_reference['tipo']

            banking_reference_registred.save()
        except:
            raise exceptions.APIException(
                'Não foi possível atualizar os dados de refenrências bancárias')

    return Response({'detail': 'Atualização feita com sucesso'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def find_last_physical_person(request):
    id_institution = request.user.instit_id
    try:
        persons = Pescod.objects.filter(
            id_instituicao_fk=id_institution, sit=2, tipo=1).order_by('-id_pessoa_cod')[:5]
        persons_serialized = PescodSerializer(persons, many=True)
        return Response(persons_serialized.data)
    except:
        raise exceptions.APIException


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@csrf_exempt
def find_last_providers(request):
    id_institution = request.user.instit_id
    try:
        persons = Pescod.objects.filter(
            id_instituicao_fk=id_institution, sit=2, forn=1).order_by('-id_pessoa_cod')[:5]
        persons_serialized = PescodSerializer(persons, many=True)
        return Response(persons_serialized.data)
    except:
        raise exceptions.APIException
