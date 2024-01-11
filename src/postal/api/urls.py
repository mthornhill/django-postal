from django.conf.urls import *
from ..resource import Resource
from postal.api.handlers import PostalHandler

postal_handler = Resource(PostalHandler)

urlpatterns = patterns(
    "",
    url(r"^country/$", postal_handler, name="postal-api-country"),
)
