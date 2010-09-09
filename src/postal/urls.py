from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns("",
    url(r'^update_postal_address/$', 'postal.views.changed_country', name="postal_changed_country"),
)
