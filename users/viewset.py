from rest_framework import viewsets
from .serializers import UsersSerializers
from .models import Users


class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Users.objects.all()
    serializer_class = UsersSerializers
    # permission_classes = [IsAccountAdminOrReadOnly]
