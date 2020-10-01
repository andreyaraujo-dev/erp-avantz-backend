from rest_framework import serializers
from .models import Users


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model: Users
        fields: ['id', 'username', 'email', 'nome',
                 'login', 'instit', 'idpescod', 'acess']
