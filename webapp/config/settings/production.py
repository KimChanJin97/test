from .base import *

DEBUG = False
ALLOWED_HOSTS = ['13.125.43.154']
# CSRF_TRUSTED_ORIGINS = ['https://api.ibelievesurvey.com']


STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    STATIC_DIR,
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')