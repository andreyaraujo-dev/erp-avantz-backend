from .viewset import UserViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import profile, login, register, ChangePasswordView, edit, list_all, admin_edit, disabled_user, details, upload_image, delete, get_access

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
    path('edit/image', upload_image, name='edit_user_image'),
    path('list', list_all, name='list_all'),
    path('list/<str:userName>', list_all, name='find_by_name'),
    path('admin_edit/<int:id>', admin_edit, name='admin_edit'),
    path('delete/<int:id>', delete, name='delete_user'),
    path('disable/<int:id>', disabled_user, name='disable_user'),
    path('details/<int:id>', details, name='details'),
    path('access', get_access, name='get_access'),
]

urlpatterns += router.urls
