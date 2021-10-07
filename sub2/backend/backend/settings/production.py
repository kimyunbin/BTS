from .base import *

DEBUG = False

ALLOWED_HOSTS = [
 # lightsail public_ip 주소
    'j5c104.p.ssafy.io',
    '127.0.0.1',
    'localhost',
    
]
DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'ssafy_web_db',
        'USER':'root',
        'PASSWORD':'root1234',
        'HOST':'j5c203.p.ssafy.io',
        'PORT':'3306',
    }
}