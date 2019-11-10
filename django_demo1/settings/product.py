from .base import *  # NOQA

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']


DATABASES = {
'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_demo1',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'CONN_MAX_AGE': 5 * 60,
        'OPTIONS': {'charset': 'utf8mb4'}
    }
}