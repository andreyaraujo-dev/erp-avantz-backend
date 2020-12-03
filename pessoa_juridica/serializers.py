from rest_framework.serializers import ModelSerializer
from .models import Pesjur


class PessoaJuridicaSerializer(ModelSerializer):
    class Meta:
        model = Pesjur
        fields = ['id_pessoa_cod_fk', 'fantasia', 'ramo', 'inscricao_estadual', 'inscricao_municipal',
                  'tipo_empresa', 'capsocial', 'faturamento', 'tribut', 'contato', 'data_abertura', 'data_criacao']
