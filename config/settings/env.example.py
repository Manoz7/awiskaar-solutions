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


FRONTEND_URL = 'http://localhost:8000/'
DEFAULT_FROM_EMAIL = ''
USE_TEST_PASSWORD = True
TEST_PASSWORD = 'Asd123!@#'

EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = ''
