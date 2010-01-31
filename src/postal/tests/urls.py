from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

import os
DIRNAME = os.path.dirname(__file__)

urlpatterns = patterns("",
    (r'^$', 'postal.tests.views.test_postal'),
)

urlpatterns += patterns("",
    (r'^admin/(.*)', admin.site.root),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(DIRNAME, "media"), 'show_indexes': True }),
)