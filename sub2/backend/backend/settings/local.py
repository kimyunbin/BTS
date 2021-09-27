from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'ssafy_web_db',
        'USER':'root',
        'PASSWORD':'root1234',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }
}