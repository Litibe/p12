"""
Django settings for epic_events_crm project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from datetime import timedelta
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-joi$_g%^3zhc$10_x_&fvp0@a3+j&^manxa)t--5--c+))od17'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'authentication',
    'crm'
]

REST_FRAMEWORK = {
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',)
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=55),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'epic_events_crm.urls'

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

WSGI_APPLICATION = 'epic_events_crm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ocr_12', 
        'USER': 'epic_events_django', 
        'PASSWORD': 'DNRnnb61695',
        'HOST': 'node91402-env-ocr12-litibe.jcloud-ver-jpe.ik-server.com', 
        'PORT': '5432',
    }
}  


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

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'Europe/Paris'

DATETIME_FORMAT = '%Y-%m-%d %H:%M'

DATETIME_INPUT_FORMAT = ['%Y-%m-%d %H:%M']

USE_I18N = True

USE_TZ = False

SITE_ID = 1


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = "authentication.User"


LOG_PATH = os.path.join(BASE_DIR, "log/")
if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'crm': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': LOG_PATH + "crm.log",
            'formatter': 'verbose',
        },
        'crm_API': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': LOG_PATH + "crm_api.log",
            'formatter': 'verbose',
        },
        'db': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': LOG_PATH + "db.log",
            'formatter': 'verbose',
        },
        'other': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': LOG_PATH + "django.log",
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'authentication.views': {
            'handlers': ['crm_API'],
            'level': 'INFO',
            'propagate': False,
        },
        'crm.views': {
            'handlers': ['crm'],
            'level': 'INFO',
            'propagate': False,
        },
        'crm.views_API': {
            'handlers': ['crm_API'],
            'level': 'INFO',
            'propagate': False,
        },
        '': {
            'handlers': ['other'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.server': {
            'handlers': ['other'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['db'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
    'formatters': {
        'verbose': {
            'format': '{name} {levelname} {asctime} {message}',
            'style': '{',
        },
    }
}
