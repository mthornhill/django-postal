from django.conf.urls import *

urlpatterns = patterns("",
            (r'^api/', include('postal.api.urls')),
            url(r'^update_postal_address/$', 'postal.views.changed_country', name="changed_country"),
        )