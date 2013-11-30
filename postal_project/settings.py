import os

DIRNAME = os.path.dirname(__file__)

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '/tmp/postal.db', # Or path to database file if using sqlite3.
        'USER': '', # Not used with sqlite3.
        'PASSWORD': '', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}

SITE_ID = 1

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
                  'postal', ]
ROOT_URLCONF = 'postal_project.urls'

SECRET_KEY = "abc123"

POSTAL_ADDRESS_L10N = True