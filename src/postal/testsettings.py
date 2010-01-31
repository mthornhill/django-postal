DEBUG=True
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = '/tmp/postal.db'
INSTALLED_APPS = ['django.contrib.admin',
                  'django.contrib.auth',
                  'django.contrib.contenttypes',
                  'django.contrib.sessions',
                  'countries',
                  'postal',]
ROOT_URLCONF = 'postal.tests.urls'
