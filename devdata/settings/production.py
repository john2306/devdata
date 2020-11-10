from .base import *

DEBUG = True

ALLOWED_HOSTS = ['devdata.com.pe','www.devdata.com.pe','64.225.41.98']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dreamdb',
        'USER': 'dream_admin',
        'PASSWORD': 'DEVDATAIS100%SUPER',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATICFILES_DIRS = (BASE_DIR, 'static')