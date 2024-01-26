"""
Django settings for shop_ada project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from decouple import config
from datetime import timedelta
import logging
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

# ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*').split()
# ALLOWED_HOSTS =  ['127.0.0.1','7cb8-213-109-66-242.ngrok-free.app']
ALLOWED_HOSTS = ['127.0.0.10' , '34.159.30.89']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    "rest_framework",
    "rest_framework.authtoken",
    "dj_rest_auth",
    "django_filters",
    "drf_yasg",
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'twilio',
    'django_celery_results',
    'drf_api_logger',
    'cachalot',

    'account',
    'category',
    'product',
    'rating',
    'order',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'drf_api_logger.middleware.api_logger_middleware.APILoggerMiddleware',
]

ROOT_URLCONF = 'shop_ada.urls'

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

WSGI_APPLICATION = 'shop_ada.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("NAME"),
        "USER": config("USER"),
        "PASSWORD": config("PASSWORD"),
        "HOST": config("HOST"),
        "PORT": "5432",
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = 'media/'
MEDIAL_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'account.CustomUser'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

SIMPLE_JWT = {
    'ACCES_TOKEN_LIFETINE': timedelta(minutes=10),
    'REFRESH_TOKEN_LIFETINE': timedelta(hours=24),
    'BLACKLIST_AFTER_ROTATION': True,
    
}
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Token': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
        },
    },
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

TWILIO_SID = 'AC272f2d62ac5c648ddfdae66e38df7617'
TWILIO_AUTH_TOKEN = '50b5187f037ed09b960ba0951d3942ac'
TWILIO_SENDER_PHONE = '+17178976115'


CSRF_TRUSTED_ORIGINS = ['https://7cb8-213-109-66-242.ngrok-free.app']

CELERY_BROKER_URL = 'redis://localhost:6379/0'

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://redis:6379",
        # "OPTIONS" : {
        #     'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        # }
    }
}

REDIS_HOST = 'redis'
REDIS_PORT = '6379'

CELERY_BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
# CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'
CELERY_CACHE_BACKEND_OPTIONS = {
    'max_entries': 1000,
    'cull_frequency': 3,
}
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "main_format": {
            "format": "[{asctime}-{levelname}] {module}-{filename}: {message}",
            "style": "{",
        }
    },

    'handlers': {
        'console': {'class': 'logging.StreamHandler',
                    'formatter': 'main_format'},
    },

    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'WARNING'
        },
        # 'product': {
        #     'handlers': ['file'],
        #     'level': 'DEBUG'
        # }
    }
}

DRF_API_LOGGER_DATABASE = True
