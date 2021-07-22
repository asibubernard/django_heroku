from .base import *

import dj_database_url


env = os.environ.copy()

DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY', default='pskdjg-34098e-340t98dsgljsfladf09we87n8kj786876@@@@khjhlkafadljad')

ALLOWED_HOSTS = ['']

# serving staticfiles through Whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  # new



# Database configuration through dj-database-url

# db_from_env = dj_database_url.config(conn_max_age=600)
# DATABASES['default'].update(db_from_env)

DATABASE_URL = os.environ.get("DATABASE_URL")
db_from_env = dj_database_url.config(default=DATABASE_URL, conn_max_age=500, ssl_require=True)
DATABASES["default"].update(db_from_env)

# Deployment checklist 
SECURE_SSL_REDIRECT = True # new
SECURE_HSTS_SECONDS = 3600 # new
SECURE_HSTS_INCLUDE_SUBDOMAINS = True # new
SECURE_HSTS_PRELOAD = True # new
SECURE_CONTENT_TYPE_NOSNIFF = True # new
SESSION_COOKIE_SECURE = True # new
CSRF_COOKIE_SECURE = True # new 
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https') # new
