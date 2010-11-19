import os
DIRNAME = os.path.dirname(__file__)

DEBUG=True
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = '/tmp/postal.db'

SITE_ID=1

MEDIA_ROOT = DIRNAME + "/media"
MEDIA_URL = '/site_media/'

TEMPLATE_DIRS = (
    os.path.join(DIRNAME, "templates"),
)

INSTALLED_APPS = ['django.contrib.admin',
                  'django.contrib.auth',                  
                  'django.contrib.contenttypes',
                  'django.contrib.sessions',
                  'django.contrib.sites',
                  'django_countries',
                  'postal',]
ROOT_URLCONF = 'postal_project.urls'

