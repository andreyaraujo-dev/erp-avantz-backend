from rest_framework import serializers
from .models import Rotinas


class RotinasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rotinas
        fields = ['Id', 'descr', ]
