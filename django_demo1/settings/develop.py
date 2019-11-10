from .base import *  # NOQA

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# DATABASES = {
# 'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'django_demo1',
#         'USER': 'root',
#         'PASSWORD': '123456',
#         'HOST': '127.0.0.1',
#         'PORT': 3306,
#         # 'CONN_MAX_AGE': 5 * 60,
#         # 'OPTIONS': {'charset': 'utf8mb4'}
#     }
# }


# INSTALLED_APPS +=[
#     'debug_toolbar',
# ]
#
# MIDDLEWARE +=[
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
# ]
#
# INTERNAL_IPS = ['127.0.0.1']