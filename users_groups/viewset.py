from rest_framework import viewsets
from rest_framework import pagination
from .models import UsersGrp
from .serializers import UserGroupsSerializer
from django.core.paginator import Paginator
from rest_framework.permissions import IsAuthenticated


class UserGroupsViewSet(viewsets.ModelViewSet):
    queryset = UsersGrp.objects.all().order_by('id_grupo')
    serializer_class = UserGroupsSerializer
    permission_classes = [IsAuthenticated, ]
    pagination_class = Paginator(queryset, 20)
