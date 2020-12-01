from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from datetime import datetime
from django.utils import timezone

from users.authentication import SafeJWTAuthentication
from .serializers import PescodSerializer
from .models import Pescod
from pessoa_fisica.models import Pesfis
from pessoa_juridica.models import Pesjur


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def index(request):
    id_institution = request.user.instit_id
    try:
        persons = Pescod.objects.filter(
            id_instituicao_fk=id_institution, sit=1)
        persons_serialized = PescodSerializer(persons, many=True)
        return Response(persons_serialized.data)
    except:
        raise exceptions.APIException


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def store_person_physical(request):
    id_institution = request.user.instit_id
    type_person = request.data.get('personType')
    provider = request.data.get('personIsProvider')
    cpf_cnpj = request.data.get('cpfCnpj')
    name_or_company_name = request.data.get('nameOrCompanyName')
    person_photo = request.data.get('personPhoto')
    person_limit = request.data.get('personLimit')
    person_balance = request.data.get('personBalance')

    person = Pescod(id_instituicao_fk=id_institution, tipo=type_person, sit=1, forn=provider, cpfcnpj=cpf_cnpj,
                    nomeorrazaosocial=name_or_company_name, foto=person_photo, img_bites=0, limite=person_limit, saldo=person_balance, data_criacao=timezone.now())
    try:
        person.save()
    except:
        raise exceptions.APIException(
            'Não foi possível cadastrar o registro da pessoa. Verifique os dados inseridos.')

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
