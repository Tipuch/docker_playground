from .settings import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'docker_playground',
        'USER': 'docker_playground',
        'PASSWORD': '12345',
        'HOST': 'db',
        'PORT': '5432',
    }
}