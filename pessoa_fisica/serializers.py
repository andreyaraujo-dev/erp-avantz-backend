from rest_framework import serializers
from .models import Pesfis


class PessoaFisicaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pesfis
        fields = '__all__'
