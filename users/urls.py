from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import profile, login, register, ChangePasswordView, edit, list_all, admin_edit, disabled_user, details
from .viewset import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('profile', profile, name='profile'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('password_reset/', include('django_rest_passwordreset.urls',
                                    namespace='password_reset')),
    path('edit', edit, name='edit_user'),
    path('list', list_all, name='list_all'),
    path('admin_edit', admin_edit, name='admin_edit'),
    path('delete', disabled_user, name='disabled_user'),
    path('details', details, name='details'),
]

urlpatterns += router.urls
