import os

from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns("",
    (r'^admin/(.*)', admin.site.root),
    (r'^postal/', include('postal.urls')),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.DIRNAME, "tests", "media"), 'show_indexes': True }),
    url(r'^$', 'postal.tests.views.test_postal', name="postal-home"),
    
)
