"""
Django settings for avantz project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
from decouple import config
from dj_database_url import parse as dburl
import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['localhost', 'https://gcomdev.herokuapp.com',
                 'http://dev-gcom.avantz.com.br', ]

# Application definition

INSTALLED_APPS = [
    # 3rd party apps
    'corsheaders',
    'rest_framework',
    'cloudinary',
    'django_rest_passwordreset',
    'storages',
    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # project apps
    'contasfin.apps.ContasFinConfig',
    'contasmv.apps.ContasMvConfig',
    'emails.apps.EmailsConfig',
    'enderecos.apps.EnderecosConfig',
    'instituicao.apps.InstituicaoConfig',
    'itenspedido.apps.ItPedConfig',
    'pedidos.apps.PedidosConfig',
    'pescod.apps.PescodConfig',
    'pessoa_fisica.apps.PessoaFisicaConfig',
    'pessoa_juridica.apps.PessoaJuridicaConfig',
    'permissions.apps.PermissionsConfig',
    'telefones.apps.TelefonesConfig',
    'ref_bancarias.apps.RefBancariasConfig',
    'referencias.apps.ReferenciasConfig',
    'users.apps.UsersConfig',
    'users_groups.apps.UsersGroupsConfig'
    'bancos.apps.BancosConfig'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'avantz.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'avantz.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

default_db = {
    'ENGINE': config('ENGINE'),
    'NAME': config('NAME'),
    'HOST': config('HOST'),
    'USER': config('USER'),
    'PASSWORD': config('PASSWORD'),
    'PORT': config('PORT'),
}

default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = {
    'default': config('DATABASE_URL', default=default_dburl, cast=dburl)
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# rest framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'users.authentication.SafeJWTAuthentication',
        # 'rest_framework.authentication.SessionAuthentication' ,
        # 'rest_framework.authentication.BasicAuthentication' ,
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,
}

REFRESH_TOKEN_SECRET = config('REFRESH_TOKEN_SECRET')

# cors headers
CORS_ALLOW_CREDENTIALS = True  # to accept cookies via ajax request
CORS_ORIGIN_WHITELIST = [
    # the domain for front-end app(you can add more than 1)
    'http://localhost:3000',
    'http://localhost:8000',
    'https://gcomdev.herokuapp.com',
    'http://dev-gcom.avantz.com.br',
]
# CORS URLS settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8000",
    'https://gcomdev.herokuapp.com',
    'http://dev-gcom.avantz.com.br',
]

CSRF_TRUSTED_ORIGINS = [
    'localhost:3000',
    'localhost:8000',
    'gcomdev.herokuapp.com',
    'dev-gcom.avantz.com.br',
]

# List of HTTP verbs
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

# ALLOWED_HOSTS = [
#     '127.0.0.1',
#     'localhost',
#     # other allowed hosts...
# ]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'refresh_token',
    'X-CSRFToken',
    'withcredentials',
    'x-requested-with',
]

# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SAMESITE = 'None'
# CSRF_HEADER_NAME = 'X_CSRFToken'
# CSRF_COOKIE_NAME = 'csrftoken'

# Email Settings
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = config('EMAIL_USE_TLS')
# EMAIL_USE_SSL
# EMAIL_TIMEOUT
# EMAIL_SSL_KEYFILE
# EMAIL_SSL_CERTFILE

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'pt-BR'
LANGUAGES = [
    ('pt-br', 'Brazilian Portuguese'),
]

TIME_ZONE = 'America/Fortaleza'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# user model
AUTH_USER_MODEL = 'users.Users'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'templates/static'),)
# static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Activate Django-Heroku.
django_heroku.settings(locals())

#del DATABASES['default']['OPTIONS']['sslmode']
