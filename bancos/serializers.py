from rest_framework import serializers
from .models import Bancos


class BancoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bancos
        fields = ['id_bancos', 'cod', 'banco', 'isbp', 'compens']
