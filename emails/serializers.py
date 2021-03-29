from rest_framework import serializers
from .models import Mails


class EmailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mails
        fields = ['id_mails', 'id_pessoa_cod_fk', 'situacao', 'email', ]
