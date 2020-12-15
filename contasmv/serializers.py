from rest_framework import serializers
from .models import ContasMv
from django.db.models import Sum


class ContasMvSerializers(serializers.ModelSerializer):
    soma_saldo = serializers.SerializerMethodField()
#    saldo = 1

    class Meta:
        model = ContasMv
        fields = ['dat', 'descr', 'tipo', 'valor']

    def get_soma_saldo(self, soma):
        return soma.ContasMv.aggregate(Sum(1))

