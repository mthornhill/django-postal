import os

from django.conf.urls import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns("",
    (r'^admin/(.*)', include(admin.site.urls)),
    (r'^postal/', include('postal.urls')),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.DIRNAME, "media"), 'show_indexes': True }),
    url(r'^$', 'postal_project.views.test_postal', name="postal-home"),
    url(r'^json$', 'postal_project.views.test_postal_json', name="postal-home"),

)
