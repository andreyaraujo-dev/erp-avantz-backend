from rest_framework.serializers import ModelSerializer
from .models import Instit


class InstituicaoSerializer(ModelSerializer):
    class Meta:
        model = Instit
        fields = ['id_instituicao', 'idmatriz', 'idpjur', 'ativo', 'nome', 'razsoc', 'endtip', 'end', 'endcompl', 'bairro',
                  'cep', 'cidade', 'uf', 'cnpj', 'iest', 'imun', 'mail1', 'mail2', 'tel1', 'tel2', 'tel3', 'slogan', 'modulos', ]
