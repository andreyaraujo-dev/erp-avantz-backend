from rest_framework import serializers
from .models import UsersGrp


class UserGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersGrp
        fields = ['grupo', 'acess']
