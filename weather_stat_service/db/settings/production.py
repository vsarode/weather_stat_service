from weather_stat_service.db.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'weather',
        'USER': 'root',
        'PASSWORD': 'as2d2pagro',
        'HOST': 'mysql-singapore.cqxj2zlihho6.ap-southeast-1.rds.amazonaws.com',
        'PORT': '3306',
    },
    'agrostar_catalog': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'agrostar_catalog',
        'USER': 'root',
        'PASSWORD': 'as2d2pagro',
        'HOST': 'mysql-singapore.cqxj2zlihho6.ap-southeast-1.rds.amazonaws.com',
        'PORT': '3306',
    }
}
