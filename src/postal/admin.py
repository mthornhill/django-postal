# django imports
from django.contrib import admin
from postal.models import PostalAddress

class PostalAddressAdmin(admin.ModelAdmin):
    list_display = ['line1', 'line2', 'city', 'state', 'code', 'country']
    list_filter = ['state', 'country']

admin.site.register(PostalAddress, PostalAddressAdmin)
