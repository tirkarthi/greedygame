"""
Django settings for greedyapp project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import json
from config import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Settings for Travis

if "TRAVIS" in os.environ:
    SECRET_KEY = "V&uqckyogs4p4rh#@n6j*$^emdpjv+r_kp8fqn)z0engsq7(vk("
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": "./db.sqlite3"
        }
    }
    REST_FRAMEWORK = {
        'PAGE_SIZE' : 3
    }
else:
    SECRET_KEY = config['secret']

    DEBUG = config.get('debug', False)

    ALLOWED_HOSTS = []


    # Application definition

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'music_collection',
        'rest_framework',
        'django_extensions'
    )

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.security.SecurityMiddleware',
    )

    ROOT_URLCONF = 'greedyapp.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [ BASE_DIR + "/static/templates/"],
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

    WSGI_APPLICATION = 'greedyapp.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/1.8/ref/settings/#databases

    DATABASES = config['databases']


    # Internationalization
    # https://docs.djangoproject.com/en/1.8/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.8/howto/static-files/

    STATIC_URL = '/static/'

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static"),
    )

    REST_FRAMEWORK = {
        "DEFAULT_PERMISSION_CLASSES" : tuple(config['rest_framework']['DEFAULT_PERMISSION_CLASSES'].split(',')),
        "DEFAULT_FILTER_BACKENDS" : tuple(config['rest_framework']['DEFAULT_FILTER_BACKENDS'].split(',')),
        "PAGE_SIZE" : config['rest_framework']['PAGE_SIZE']
    }
