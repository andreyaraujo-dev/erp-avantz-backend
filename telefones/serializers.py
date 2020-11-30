from rest_framework import serializers
from .models import Telefones


class TelefoneSerializers(serializers.ModelSerializer):
    class Meta:
        model = Telefones
        fields = ['id_telefone', 'id_pessoa_cod_fk', 'situacao', 'tel', ]
