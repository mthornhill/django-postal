from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns("",
    (r'test_postal', 'postal.views.test_postal'),
)