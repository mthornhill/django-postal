# django imports
from django.contrib.gis import admin

# lfs imports
from postal.models import PostalAddress

admin.site.register(PostalAddress,admin.GeoModelAdmin)