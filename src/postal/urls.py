from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns("postal",
            url(r'^update_postal_address/$', 'views.changed_country', name="changed_country"),
        )