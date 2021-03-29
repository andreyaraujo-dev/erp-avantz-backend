from rest_framework.serializers import ModelSerializer
from .models import Pescod


class PescodSerializer(ModelSerializer):
    class Meta:
        model = Pescod
        fields = ['id_pessoa_cod', 'id_instituicao_fk', 'tipo', 'sit', 'forn',
                  'cpfcnpj', 'nomeorrazaosocial', 'foto', 'img_bites', 'limite', 'saldo']
