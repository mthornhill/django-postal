# django imports
from django.contrib import admin

# lfs imports
from postal.models import PostalAddress

admin.site.register(PostalAddress)