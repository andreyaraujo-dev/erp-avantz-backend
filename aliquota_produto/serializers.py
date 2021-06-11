from rest_framework import serializers
from .models import Aliquotas


class AliquotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aliquotas
        fields = ['id', 'instit', 'descr', 'valor', ]
