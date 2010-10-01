from django.conf.urls.defaults import *
from django.conf import settings

urls = (
        patterns("",
            url(r'^update_postal_address/$', 'postal.views.changed_country', name="changed_country"),
        ),
        "postal",
        "postal2",
    )