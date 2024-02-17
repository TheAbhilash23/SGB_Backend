"""
Django settings for iam project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from datetime import timedelta
from pathlib import Path
from core import choices
from core.base_settings import *
from core.messagbus.registry import RegistryCollection
from decouple import config

# Load environment variables from .env
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent
SECRET_KEY = 'django-insecure-=uc^wslzb%ckcek0%j#fa133av-77v-02m#eie^00!tj9zm_wb'


# GRPC registration
HANDLER = RegistryCollection('iam')
HANDLER.register('users.service_views.UserServiceView')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# Application definition

DEPENDENCY_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'corsheaders',
    'core.messagbus',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'rest_social_providers',
]

GOOGLE_LOGIN_ENABLED = config('GOOGLE_LOGIN_ENABLED', default=False, cast=bool)
if GOOGLE_LOGIN_ENABLED:
    DEPENDENCY_APPS.append('allauth.socialaccount.providers.google',)

USER_APPS = [
    'users',
]

INSTALLED_APPS = DEPENDENCY_APPS + USER_APPS


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ('*',)

GROUPS_ALLOWED = (choices.UserGroup.ADMIN,
                  choices.UserGroup.BANK_STAFF,
                  choices.UserGroup.BANK_STAFF_MANAGER
                  )


SUB_COMMANDS = ['initial_users',
                ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'core.base.middlewares.TokenAuthenticationMiddleware', # It must be added after the sessions middleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# from django.core.exceptions import
# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = config('STATIC_ROOT', default=os.path.join(BASE_DIR / 'static/'))
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/')]


MEDIA_URL = '/media/'
MEDIA_ROOT = config('MEDIA_ROOT', default=os.path.join(BASE_DIR / 'media/'))
# MEDIA_DIR = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'users.User'

# Add Custom authentications
AUTHENTICATION_BACKENDS = [
    'backends.CustomAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

TOKEN_EXPIRATION_TIMEOUT = 60 * 60  # seconds for dev
COOKIE_EXPIRATION_TIMEOUT = 300  # seconds

# Django Rest Framework settings (importing
# from rest_framework.settings
# from djangorestframework_camel_case.settings
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.JSONParser',
    ],
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    )
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=50),  # Keep this less than 5 min in a production environment
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "UPDATE_LAST_LOGIN": True,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "USER_ID_FIELD": "pk",
    "USER_ID_CLAIM": "UserId",
}

# dj-rest-auth settings
# from dj_rest_auth.app_settings import

REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_HTTPONLY': False,
    'TOKEN_MODEL': 'rest_framework.authtoken.models.Token',
    'TOKEN_CREATOR': 'dj_rest_auth.utils.default_create_token',
    'LOGIN_SERIALIZER': 'rest_social_providers.serializers.CustomLoginSerializer',
}

GOOGLE_CALLBACK_URL = config('GOOGLE_CALLBACK_URL',
                             default='http://localhost:8000/accounts/google/login/callback/')

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
        'FETCH_USERINFO': True
    }
}

SITE_ID = 1
