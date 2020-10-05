from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import UsersSerializers
from .models import Users


class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    # User = get_user_model()
    queryset = Users.objects.all()
    serializer_class = UsersSerializers
    # permission_classes = [IsAccountAdminOrReadOnly]
