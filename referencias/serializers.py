from rest_framework import serializers
from .models import Referencias


class ReferenciasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Referencias
        fields = ['id_referencia', 'id_pessoa_cod_fk',
                  'situacao', 'tipo', 'nome', 'tel', 'endereco']
