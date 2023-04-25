"""
Django settings for Project project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-wc-t9-#7!zfmnq8o3iz3n0b3#^bs=51+xo&-*jgf4i63(kfzr='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'news.apps.NewsConfig',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    'django_apscheduler',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
]

ROOT_URLCONF = 'Project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'Project.wsgi.application'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

LOGIN_REDIRECT_URL = "/news"

LOGOUT_REDIRECT_URL = '/accounts/login/'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}
ACCOUNT_CONFIRM_EMAIL_ON_GET = True

SITE_URL = 'http://127.0.0.1:8000'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "ana.rewv"
EMAIL_HOST_PASSWORD = "ecqixnwxahfsrxbz"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = "ana.rewv@yandex.ru"

APSCHEDULER_DATETIME_FORMAT = 'N j, Y, f:s a'

APSCHEDULER_RUN_NOW_TIMEOUT = 25

SERVER_EMAIL = "ana.rewv@yandex.ru"
MANAGERS = (
    ('Anastasiya', 'ana.kushu@yandex.ru'),
    ('Anna', 'ana.rewv@yandex.ru'),
)

EMAIL_SUBJECT_PREFIX = 'Новостной портал: '

ADMINS = (
    ('Anna', 'ana.rewv@yandex.ru'),
)

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        'django': {
            'handlers': ['console', 'general'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['warning', 'error', 'mistakes', 'mail_admins'],
            'level': 'WARNING',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['mistakes', 'mail_admins'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.template': {
            'handlers': ['mistakes'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['mistakes'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.security': {
            'handlers': ['warning', 'error', 'security'],
            'level': 'INFO',
            'propagate': False,
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'filters': ['require_debug_true'],
            'formatter': 'myform'
        },
        'warning': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'filters': ['require_debug_true', 'filter_warning_level'],
            'formatter': 'myform_warning'
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'filters': ['require_debug_true', 'filter_error_level'],
            'formatter': 'myform_error'
        },
        'general': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': './logs/general.log',
            'filters': ['require_debug_false'],
            'formatter': 'general'
        },
        'mistakes': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': './logs/errors.log',
            'formatter': 'myform_error'
        },
        'security': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': './logs/security.log',
            'formatter': 'general'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
            'formatter': 'myform_warning'
        },
    },
    'formatters': {
        'myform': {
            'format': '{asctime} {levelname} {message}',
            'datetime': '%Y-%m-%d %H:%M:%S',
            'style': '{',
        },
        'myform_warning': {
            'format': '{asctime} {levelname} {message} \n{pathname}',
            'datetime': '%Y-%m-%d %H:%M:%S',
            'style': '{',
        },
        'myform_error': {
            'format': '{asctime} {levelname} {message} \n{pathname} \n{exc_info}',
            'datetime': '%Y-%m-%d %H:%M:%S',
            'style': '{',
        },
        'general': {
            'format': '{asctime} {levelname} {module} {message}',
            'datetime': '%Y-%m-%d %H:%M:%S',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'filter_warning_level': {
            '()': 'logs.logs.FilterLevels',
            'filter_levels': ['WARNING']
        },
        'filter_error_level': {
            '()': 'logs.logs.FilterLevels',
            'filter_levels': ['ERROR', 'CRITICAL']
        },
    },
}
