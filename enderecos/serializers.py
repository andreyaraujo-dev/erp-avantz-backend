from rest_framework import serializers
from .models import Enderecos


class EnderecosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Enderecos
        fields = ['id_enderecos', 'situacao', 'origem', 'id_pessoa_cod_fk', 'endtip',
                  'rua', 'numero', 'complemento', 'bairro', 'cep', 'cidade', 'estado_endereco']
