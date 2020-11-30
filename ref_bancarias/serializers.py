from rest_framework import serializers
from .models import Refbanco


class RefBancoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Refbanco
        fields = ['id_banco', 'id_pessoa_cod_fk', 'id_bancos_fk',
                  'situacao', 'agencia', 'conta', 'abertura', 'tipo', ]
