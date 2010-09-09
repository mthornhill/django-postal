import os
DIRNAME = os.path.dirname(__file__)

DEBUG=True
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = '/tmp/postal.db'

MEDIA_ROOT = DIRNAME + "/tests/media"
MEDIA_URL = '/site_media/'

INSTALLED_APPS = ['django.contrib.admin',
                  'django.contrib.auth',
                  'django.contrib.contenttypes',
                  'django.contrib.sessions',
                  'django_countries',
                  'postal',]
ROOT_URLCONF = 'postal.tests.urls'

