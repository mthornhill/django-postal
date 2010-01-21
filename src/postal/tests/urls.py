from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns("",
    (r'test_postal', 'postal.tests.views.test_postal'),
)