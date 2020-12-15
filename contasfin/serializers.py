from rest_framework import serializers
from .models import ContasFin


class ContasFinSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContasFin
        fields = '__all__'