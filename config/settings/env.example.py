from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG:
    # configuration for django debug toolbar
    INTERNAL_IPS = [
        '127.0.0.1',
    ]
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware'  # django debug toolbar middleware
    ]
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = []

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_sb7l*jg2bhk=bp1hfas2q45#iv6ph_u^@dc%*jz&89(q%*!6(fzn'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ASSETS_MEDIA_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'awiskaar',
#         'USER': 'awiskaar',
#         'PASSWORD': 'Awiskaar@123$$',
#     }
# }

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'sheamuskhan48@gmail.com'
EMAIL_HOST_PASSWORD = 'Sheamus@123'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
