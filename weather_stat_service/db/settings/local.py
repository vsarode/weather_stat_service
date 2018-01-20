

from weather_stat_service.db.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'weather',
        'USER': 'root',
        'PASSWORD': 'as2d2p',
        'HOST': 'localhost',
        'PORT': '',
    },
    'agrostar_crm': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'agrostar_crm',
        'USER': 'root',
        'PASSWORD': 'as2d2p',
        'HOST': 'localhost',
        'PORT': '',
    },
}



