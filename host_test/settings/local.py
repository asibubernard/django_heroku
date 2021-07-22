from .base import *
import os

SECRET_KEY = 'django-insecure-tgz1hoqe2^bht#lexr&6415-b@#mcxj%0f8pbmkatr42xra9a*'


DEBUG = True

ALLOWED_HOSTS = ['*']


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'host_test',
#         'USER': 'host_test',
#         ''
#         'HOST': 'localhost',
#         'PORT': 5432,
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}

# INSTALLED_APPS += ['debug_toolbar',]